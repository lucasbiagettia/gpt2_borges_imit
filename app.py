import textwrap
from borgesModel import BorgesModel

borges_model = BorgesModel()

input = "Empieza desde aqui"

text = borges_model.generate(input)


max_lenght = 70

# Usar textwrap para dividir el string en líneas
lines = textwrap.wrap(text, width=max_lenght)

# Imprimir cada línea
for line in lines:
    print(line)