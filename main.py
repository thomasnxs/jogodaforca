import os
from funcoes import clear, ler_historico, salvar_historico, ler_letra
tentativas = 0
i = -1
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"
clear()
print(magenta + "_"*20,"JOGO DA FORCA","_"*20,"\n" + reset_color)
nome_desafiante = input(cyan + 'Insira o nome do Desafiante!: ' + reset_color)
nome_competidor = input(cyan + 'Insira o nome do Competidor!: ' + reset_color)
clear()
palavra_chave =input(cyan + 'DESAFIANTE insira a palavra CHAVE!: '+ reset_color).upper()
dica1 = input(cyan + 'DESAFIANTE insira a DICA 1!: ' + reset_color)
dica2 = input(cyan + 'DESAFIANTE insira a DICA 2!: ' + reset_color)
dica3 = input(cyan + 'DESAFIANTE insira a DICA 3!: ' + reset_color)
dica4 = (red + 'Suas dicas acabaram!' + reset_color)
dicas = [dica1, dica2, dica3, dica4]
clear()
numero_letras = ["*"] * len(palavra_chave)
quantia_letras = len(palavra_chave)
letras_escolhidas = []
print(green + 'A palavra contém'+ cyan, numero_letras, red, quantia_letras, green + 'letras!' + reset_color)

while tentativas < 6 and "".join(numero_letras) != palavra_chave:
    if i <=2:
        escolha = input('Digite' + cyan + ' (0) '+ reset_color + 'para Jogar, ou ' + cyan + '(1)' + reset_color +' para pedir uma dica!: ')
        if escolha == '0':
            letra=ler_letra()
            clear()
        elif escolha == '1':
            i = i + 1
            print("A dica é:",blue, dicas[i], reset_color)
            letra=ler_letra()
            clear()
        else:
            print(red + 'Informe corretamente (0) ou (1)' + reset_color)
            continue
    else:
        print(red + 'Suas dicas acabaram!' + reset_color)
        letra = ler_letra()
        clear()

    while letra.upper() in letras_escolhidas:
        print(red + 'Você já escolheu essa LETRA!' + reset_color)
        print('Essas são as letras que já foram escolhidas',cyan, letras_escolhidas,reset_color,'!')
        print(numero_letras)
        letra=ler_letra()
        clear()
    letras_escolhidas.append(letra.upper())
    if letra.upper() in palavra_chave:
        print(green + 'Você acertou uma letra!' + reset_color)
        print('Essas são as letras que já foram escolhidas',cyan, letras_escolhidas,reset_color,'!')
        for item in range(len(palavra_chave)):
            if letra.upper() == palavra_chave[item]:
                numero_letras[item] = letra.upper()
                print(numero_letras)
    else:
        tentativas = tentativas + 1
        print(red + 'Você errou!' + reset_color)
        print('Você já cometeu', red ,tentativas,reset_color,'de',red, '6',reset_color, 'erros!')
        print('Essas são as letras que já foram escolhidas',cyan, letras_escolhidas,reset_color,'!')
        print(numero_letras)

if tentativas == 6:
    print(red, 'Você perdeu! Suas tentativas acabaram!', reset_color)
    dados = ler_historico()
    dados.append("Palavra: "+palavra_chave+" - Vencedor: Desafiante "+nome_desafiante+", Perdedor: Competidor "+nome_competidor+"\n")
    salvar_historico(dados)
else:
    print(yellow + 'Parabéns!! Você ganhou! A palavra era',blue, palavra_chave, yellow,'!', reset_color)
    dados = ler_historico()
    dados.append("Palavra: "+palavra_chave+" - Vencedor: Competidor "+nome_competidor+", Perdedor: Desafiante "+nome_desafiante+"\n")
    salvar_historico(dados)


