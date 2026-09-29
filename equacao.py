# 4**x == 16**2
# 4**x == 4**4
# x == 4

# calculador de equações exponenciais

import math

# Entrada de dados
base = float(input('Base do termo com expoente desconhecido (a): '))
base_contraria = float(input('Base do termo conhecido (b): '))
expoente_contrario = float(input('Expoente do termo conhecido (y): '))

# Validação das bases para logaritmo (base deve ser > 0 e != 1)
if base <= 0 or base == 1 or base_contraria <= 0:
    print("Erro: A base deve ser um número positivo e diferente de 1.")
else:
    # Cálculo do expoente desconhecido usando logaritmos
    # a^x = b^y  =>  x = log(b^y) / log(a)
    expoente = (expoente_contrario * math.log(base_contraria)) / math.log(base)
    
    print(f"\nO expoente desconhecido é: {expoente}")