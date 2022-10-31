import os
import string
a = list(string.ascii_lowercase)

def clear():
    os.system("cls")

def ler_historico():
    try:
        historico = open("historico.txt", "r")
    except:
        historico = open("historico.txt", "w")
        historico.close()
        historico = open("historico.txt", "r")
    dados = historico.readlines()
    historico.close()
    return dados

def salvar_historico(dados):
    historico = open("historico.txt","w")
    historico.writelines(dados)
    historico.close()

def ler_letra():
    while True:
        letra = input("Digite a letra desejada: ").lower()
        if letra in a:
            return letra
        else:
            print("Isso não é uma letra!")