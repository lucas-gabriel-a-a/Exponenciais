# 2 * 4**x = 512
#4**x = 256
#4**x=4**4
#x=4


import math

def calcular_y(a, b, c, x):
    """Calcula f(x) = a * (b^x) + c"""
    return a * (b**x) + c

def calcular_x(a, b, c, y):
    """Calcula x dado f(x) = y: x = log((y - c) / a) / log(b)"""
    termo = (y - c) / a
    if termo <= 0:
        raise ValueError("Não existe valor real de x para este valor de y (argumento do logaritmo <= 0).")
    return math.log(termo) / math.log(b)

# --- Entrada de Parâmetros da Função f(x) = a * b^x + c ---
print("--- Definição da Função Exponencial: f(x) = a * b^x + c ---")
a = float(input("Digite o coeficiente 'a' (padrão 1): ") or 1)
b = float(input("Digite a base 'b' (deve ser > 0 e != 1): "))
c = float(input("Digite o deslocamento 'c' (padrão 0): ") or 0)

# Validação das regras da função exponencial
if b <= 0 or b == 1:
    print("\nErro: A base 'b' deve ser estritamente positiva e diferente de 1.")
elif a == 0:
    print("\nErro: O coeficiente 'a' não pode ser zero.")
else:
    print(f"\nFunção definida: f(x) = {a} * ({b}^x) + {c}")
    print("--------------------------------------------------")
    print("1. Descobrir f(x) dado o valor de x")
    print("2. Descobrir x dado o valor de f(x)")
    opcao = input("Escolha a opção (1 ou 2): ")

    if opcao == '1':
        x = float(input("Digite o valor de x: "))
        y = calcular_y(a, b, c, x)
        print(f"\nResultado: f({x}) = {y}")
        
    elif opcao == '2':
        y = float(input("Digite o valor desejado de f(x): "))
        try:
            x = calcular_x(a, b, c, y)
            print(f"\nResultado: x = {x}")
        except ValueError as e:
            print(f"\nErro no cálculo: {e}")
            
    else:
        print("\nOpção inválida.")