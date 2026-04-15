import os
os.system("cls")

passar_numero_for = 0
cont = 0
numeros_vetor = []
quantidade_pares = 0
quantidade_positivos = 0
quantidade_negativos = 0
quantidade_impares = 0
soma_impares = 0
soma_geral = 0
soma_pares = 0
vetor_par = []
vetor_impar = []


# Variáveis para armazenar os números
while True:
    numero = int(input("Digite um número: "))
    numeros_vetor.append(numero)
    if numero % 2 == 0:
        quantidade_pares +=1
        vetor_par.append(numero)
    else:
        quantidade_impares += 1
        vetor_impar.append(numero)
    if numero > 0:
        quantidade_positivos += 1
    else:
        quantidade_negativos += 1

    cont += 1
    if cont == 5:
        break

# Calculando as médias
soma_par = sum(vetor_par)
soma__impar = sum(vetor_impar)

if quantidade_pares != 0:
    media_par = soma_par / quantidade_pares
else:
    media_par = "Nenhum numero PAR foi DIGITADO"
if quantidade_impares != 0:
    media_impar = soma__impar / quantidade_impares
else:
    media_impar = "Nenhum numero IMPAR foi DIGITADO"

maior = max(numeros_vetor)
menor = min(numeros_vetor)

soma_geral = sum(numeros_vetor)
media_geral = soma_geral / cont
invertido = numeros_vetor[::-1]


# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de numeros PAR: {quantidade_pares} e numeros IMPARES: {quantidade_impares}")
print(f"Quantidade de numeros POSITIVOS: {quantidade_positivos} e numeros NEGATIVOS: {quantidade_negativos}")
print(f"Quantidade de numeros inseridos: {cont}")
print(f"O maior numero: {maior} e menor numero: {menor}")
print(f"A media PAR: {media_par}")
print(f"A media IMPARES: {media_impar}")
print(f"A media GERAL: {media_geral}")
print(f"A ordem inversa: {invertido}")



