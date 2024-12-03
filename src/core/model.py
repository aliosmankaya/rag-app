from transformers import AutoTokenizer, AutoModelForCausalLM

from .file import FileManager
from ..config import settings


class ModelManager:
    def __init__(self, name: str, question: str, limit: int):
        self.name = name
        self.question = question
        self.limit = limit

    def generate(self):
        model_name = settings.model.name
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        prompt = FileManager(name=self.name).prompt(
            question=self.question, limit=self.limit
        )

        inputs = tokenizer.encode(prompt, return_tensors="pt")

        outputs = model.generate(
            inputs,
            max_new_tokens=settings.model.max_new_token,
            temperature=settings.model.temperature,
            top_p=settings.model.top_p,
            do_sample=True,
        )
        output = tokenizer.decode(outputs[0])

        answer_start = output.find("Answer:") + len("Answer:")
        response = output[answer_start:]
        response = " ".join(response.replace("\n", " ").strip().split())

        return response
