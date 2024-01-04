from transformers import AutoTokenizer, AutoModelForCausalLM
import torch 
import textwrap

class SingletonModel:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonModel, cls).__new__(cls)
            # Inicialización del modelo y el tokenizer aquí
            cls._instance.model_path = "model"
            cls._instance.device = "cpu"
            cls._instance.tokenizer = AutoTokenizer.from_pretrained(cls._instance.model_path)
            cls._instance.model = AutoModelForCausalLM.from_pretrained(cls._instance.model_path)
        return cls._instance


    def generate(self, input_text):
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long).to(self.device)

        generated_text = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=4,
            top_k=50,
            top_p=0.95,
            temperature=0.2,
            pad_token_id=50256,
            do_sample=True
        )

        final_generated_text = self.tokenizer.decode(generated_text[0], skip_special_tokens=True)
        return final_generated_text


# Definir el ancho máximo de cada línea
max_lenght = 70

# Usar textwrap para dividir el string en líneas
lines = textwrap.wrap(final_generated_text, width=max_lenght)

# Imprimir cada línea
for line in lines:
    print(line)
