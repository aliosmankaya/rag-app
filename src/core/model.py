from transformers import AutoTokenizer, AutoModelForCausalLM

from .file import FileManager


class ModelManager:
    def __init__(self, name: str, question: str):
        self.name = name
        self.question = question

    def generate(self):
        model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        prompt = FileManager(name=self.name).prompt(question=self.question, limit=3)

        inputs = tokenizer.encode(prompt, return_tensors="pt")

        outputs = model.generate(
            inputs, max_new_tokens=100, temperature=0.2, top_p=0.9, do_sample=True
        )
        output = tokenizer.decode(outputs[0])

        answer_start = output.find("Answer:") + len("Answer:")
        response = output[answer_start:]
        response = " ".join(response.replace("\n", " ").strip().split())

        return response
