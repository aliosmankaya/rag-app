import os
from tqdm import tqdm
from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

from .db import DB
from ..config import settings


class FileManager:
    def __init__(self, name: str):
        self.name = name
        self.model = SentenceTransformer(settings.file.model)

    @staticmethod
    def embed(model, text):
        return model.encode([text], normalize_embeddings=True).tolist()[0]

    def embed_texts(self):
        filetype = self.name.split("_")[-1]
        loader = {"pdf": PyPDFLoader, "csv": CSVLoader}[filetype]

        filename = "_".join(self.name.split("_")[:-1]) + "." + filetype
        root_path = os.path.abspath(os.curdir)
        file_path = f"{root_path}/{settings.file.path}{filename}"
        files = loader(file_path).load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.file.chunk_size,
            chunk_overlap=settings.file.chunk_overlap,
        )
        chunks = text_splitter.split_documents(files)
        text_lines = [chunk.page_content for chunk in chunks]

        data = []
        for i, line in enumerate(tqdm(text_lines, desc="Creating embeddings")):
            data.append(
                {
                    "id": i,
                    "vector": self.embed(model=self.model, text=line),
                    "text": line,
                }
            )

        DB.insert_collection(name=self.name, data=data)

    def search(self, search: str, limit: int = settings.file.limit):
        return DB.search(
            name=self.name,
            data=self.embed(model=self.model, text=search),
            limit=limit,
        )

    def prompt(self, question: str, limit: int = settings.file.limit):
        retrieved = self.search(search=question, limit=limit)

        context = "\n".join([r["entity"]["text"] for r in retrieved[0]])

        prompt = f"""
        [Instruction]
        You are an assistant designed to help users understand documents by answering their questions based solely on the content of the document. If the answer cannot be found in the document, respond with, "The document does not provide this information."

        [Document Context]
        ---
        {context}
        ---

        [User Query]
        Question: {question}

        [Output Section]
        Answer:
        """

        return prompt
