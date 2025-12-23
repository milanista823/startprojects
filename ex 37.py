codigos = []
pesos = []
alturas = []
codigo = None
while codigo != 0:
    codigo = int(input("Digite seu código: "))
    if codigo == 0:
        break
    codigos.append(codigo)
    altura = int(input("Digite sua altura em cm: "))
    alturas.append(altura)
    peso = float(input("Digite seu peso: "))
    pesos.append(peso)
posicaopesomax = pesos.index(max(pesos))
posicaopesomin = pesos.index(min(pesos))
posicaoalturamax = alturas.index(max(alturas))
posicaoalturamin = alturas.index(min(alturas))
print(f"O aluno mais alto é o {codigos[posicaoalturamax]} com {max(alturas): .1f}")
print(f"O aluno mais baixo é o {codigos[posicaoalturamin]} com {min(alturas): .1f}")
print(f"O aluno mais gordo é o {codigos[posicaopesomax]} com {max(pesos): .1f}")
print(f"O aluno mais leve é o {codigos[posicaopesomin]} com {min(pesos): .1f}")