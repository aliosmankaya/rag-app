from transformers import AutoTokenizer, AutoModelForCausalLM


class ModelManager:
    def __init__(self, prompt):
        self.model = AutoModelForCausalLM.from_pretrained(
            "HuggingFaceTB/SmolLM2-135M-Instruct"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            "HuggingFaceTB/SmolLM2-135M-Instruct"
        )
        self.prompt = prompt
        self.inputs = None

    def tokenize(self):
        self.inputs = self.tokenizer.encode(self.prompt, return_tensors="pt")

    def generate(self):
        outputs = self.model.generate(
            self.inputs, max_new_tokens=100, temperature=0.2, top_p=0.9, do_sample=True
        )
        return self.tokenizer.decode(outputs[0])
