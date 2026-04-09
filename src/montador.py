import re

#ler nome do arquivo
nomeArquivo = input("")

#ler arquivo de entrada
with open('src/'+nomeArquivo, 'r', encoding='utf-8') as arq:
    instrucoes = arq.read()
    print(instrucoes)

#dividir linha por \n
vetInstrucoes = instrucoes.split('\n')

#dividir cada linha com , ou ' '
for linha in vetInstrucoes:
    
    instrucao = linha.split()

    print(linha.split(" "))

    #definir formato a partir da primeira palavra
    match instrucao[0]:
        case 'add' | 'and' | 'or' | 'sub' | 'sll' | 'xor' | 'srl':
            
            #tipo R
            print("R")


        case 'addi' | 'andi' | 'ori' | 'li' | 'lw' | 'lh':
            
            #I
            print("I")

        case 'sw' | 'sh' | 'sb':
            #S
            print("s")

        case _:
            #B
            print("B")
            
            


#
