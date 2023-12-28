from transformers import GPTNeoForCausalLM, GPT2Tokenizer

def generar_texto_creativo(prompt, modelo, tokenizer, max_length=100, temperatura=1.0):
    entrada_codificada = tokenizer.encode(prompt, return_tensors="pt")

    salida = modelo.generate(
        input_ids=entrada_codificada,
        max_length=max_length,
        temperature=temperatura,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        early_stopping=True
    )

    texto_generado = tokenizer.decode(salida[0], skip_special_tokens=True)
    return texto_generado

# Cargar el modelo preentrenado GPT-Neo y su tokenizer
modelo = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

# Generar texto creativo a partir de un prompt
prompt = "En un mundo donde los robots han conquistado la Tierra"
texto_generado = generar_texto_creativo(prompt, modelo, tokenizer, max_length=150, temperatura=0.7)

print(texto_generado)
