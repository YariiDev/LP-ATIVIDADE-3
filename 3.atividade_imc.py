import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def calcular_imc(peso,altura):
    imc= peso / (altura ** 2)
    return imc


def situacao_imc(imc):
    if imc < 18.5:
        situacao = "Abaixo do Peso"
    elif imc >= 18.5 and imc <= 25:
        situacao = "Peso Normal"
    elif imc >= 25 and imc <=30:
        situacao = "Sobrepeso"
    elif imc >= 30 and imc <= 35:
        situacao = "Obesidade Grau I"
    elif imc >= 35 and imc <= 40:
        situacao = "Obesidade Grau II"
    else:
        situacao = "Obseidade Grau III"
    return situacao
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenome = []
idades = []
alturas = []
pesos = []
imc = []
situacao_usuario = []


# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    snome = input("Informe seu sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    imc_ = calcular_imc(peso,altura)
    sit = situacao_imc(imc_)
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenome.append(snome)
    imc.append(imc_)
    situacao_usuario.append(sit)


# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print("\n")
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenome[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC:{imc[i]:.2f}")
    print("Situação:",situacao_usuario[i])