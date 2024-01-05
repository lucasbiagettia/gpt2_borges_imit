from transformers import AutoTokenizer, AutoModelForCausalLM
import torch 
import os

class BorgesModel:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(BorgesModel, cls).__new__(cls)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            model_dir = os.path.join(current_dir, "model")


            if os.path.exists(model_dir):
                cls._instance.model_path =model_dir
                print("lo tenia")
            else:
                cls._instance.model_path = "lucasbiagettia/gpt2-base-borges"
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
        final_length = int(length)

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



