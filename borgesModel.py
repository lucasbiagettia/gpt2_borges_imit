from transformers import AutoTokenizer, AutoModelForCausalLM
import torch 

class BorgesModel:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(BorgesModel, cls).__new__(cls)
            # Inicialización del modelo y el tokenizer aquí
            cls._instance.model_path = "model"
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")

            cls._instance.device = device
            cls._instance.tokenizer = AutoTokenizer.from_pretrained(cls._instance.model_path)
            cls._instance.model = AutoModelForCausalLM.from_pretrained(cls._instance.model_path)
            cls._instance.model.to(device)
        return cls._instance


    def generate(self, input_text, length):
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long).to(self.device)
        length = int(length)
        words = input_text.split()
        input_length = len(words)
        final_length = input_length + length
        if (final_length > 300):
            final_length = 300
        if (final_length <15):
            final_length = 15

        generated_text = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens =final_length,
            num_return_sequences=1,
            no_repeat_ngram_size=6,
            top_k=35,
            top_p=0.95,
            temperature=0.8,
            pad_token_id=50256,
            do_sample=True,
        )



        final_generated_text = self.tokenizer.decode(generated_text[0], skip_special_tokens=True)
        return final_generated_text



