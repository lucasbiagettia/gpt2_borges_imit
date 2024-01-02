import torch
from transformers import pipeline

generate_text = pipeline(model="PlanTL-GOB-ES/gpt2-base-bne", trust_remote_code=True, device="cpu")

print("Modelo cargado")

res = generate_text("Explain to me the difference between nuclear fission and fusion.")
print(res[0]["generated_text"])

prompt = "nada"

while res != "fin":
  prompt = input("Ingrese un número: ")
  res = generate_text(prompt)
  print(res[0]["generated_text"])

print("fin")
