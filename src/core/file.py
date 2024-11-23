from tqdm import tqdm
from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

from .db import DB


class FileManager:
    def __init__(self, file_name: str, filetype: str):
        self.file_name = file_name
        self.filetype = filetype
        self.files = []
        self.text_lines = []
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        self.prompt = ""

    def load(self):
        loader = {"pdf": PyPDFLoader, "csv": CSVLoader}[self.filetype]
        file_path = f"src/file/{self.file_name}"
        self.files = loader(file_path).load()

    def split(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        chunks = text_splitter.split_documents(self.files)
        self.text_lines = [chunk.page_content for chunk in chunks]

    @staticmethod
    def embed_text(model, text):
        return model.encode([text], normalize_embeddings=True).tolist()[0]

    def embed_texts(self):
        DB.create_collection(name=self.file_name, dim=384)

        data = []
        for i, line in enumerate(tqdm(self.text_lines, desc="Creating embeddings")):
            data.append(
                {
                    "id": i,
                    "vector": self.embed_text(model=self.model, text=line),
                    "text": line,
                }
            )

        DB.insert_collection(name=self.file_name, data=data)

    def prompt(self, question: str, limit: int = 3):
        retrieved = DB.search(
            name=self.file_name,
            data=self.embed_text(model=self.model, text=question),
            limit=limit,
        )

        context = "\n".join([r["entity"]["text"] for r in retrieved[0]])

        self.prompt = """
        Use the following pieces of information enclosed in <context> \
        tags to provide an answer to the question enclosed in <question> \
        tags.
        <context>
        {context}
        </context>
        <question>
        {question}
        </question>
        """.format(
            context=context, question=question
        )
