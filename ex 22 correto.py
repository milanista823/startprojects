divisores = []
num = int(input("Digite um número inteiro para saber se ele é primo ou não: "))
for i in range (1, num + 1):
    if num%i == 0:
        divisores.append(i)
if len(divisores) == 2:
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")
print(f"Os divisores do {num} são {divisores}")