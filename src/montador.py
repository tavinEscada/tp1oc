import re
import sys

class Comando:
    def __init__(self):
        self.tipo = ''
        self.funct7 = ''
        self.rs2 = ''
        self.rs1 = ''
        self.funct3 = ''
        self.rd = ''
        self.opcode = ''
        self.immediate = ''

def binario(n, bits):
    return format(n & (2**bits - 1), f'0{bits}b')

def indentificaComando(instrucao, c):
    

    match instrucao[0]:
        case 'add' | 'beq' | 'addi' | 'lb' | 'sb' | 'sub':
            c.funct3 = '000'

        case 'lh' | 'sh' | 'sll' | 'bne':
            c.funct3 = '001'

        case 'lw' | 'sw':
            c.funct3 = '010'

        case 'xor':
            c.funct3 = '100'

        case 'srl':
            c.funct3 = '101'

        case 'ori' | 'or':
            c.funct3 = '110'

        case 'andi' | 'and':
            c.funct3 = '111'

    match instrucao[0]:
        case 'add' | 'sll' | 'xor' | 'or' | 'and' | 'srl':
            c.funct7 = '0000000'

        case 'sub' | 'sra':
            c.funct7 = '0100000'

    match instrucao[0]:
        case 'add' | 'and' | 'or' | 'slr' | 'sll' | 'sub' | 'xor' | 'srl':
            c.opcode = '0110011'

        case 'beq' | 'bne':
            c.opcode = '1100011'

        case 'lb' | 'lh' | 'lw':
            c.opcode = '0000011'

        case 'sb' | 'sw' | 'sh':
            c.opcode = '0100011'

        case 'andi' | 'ori' | 'addi':
            c.opcode = '0010011'

    for i in range(1,4):
        instrucao[i] = instrucao[i].replace("x", "")
    '''

    c.rs1 = format(int(instrucao[2]), '05b')

    if(c.tipo == 'r' or c.tipo == 'i'):
        c.rd = format(int(instrucao[1]), '05b')
    
    if(c.tipo != 'r'):
        c.immediate = format(int(instrucao[3]), '12b')

    if(c.tipo in ('r', 's', 'b')):
        instrucao[3].replace("x", "")
        c.rs2 = format(int(instrucao[3]), '05b')
    '''
    for i in range (1, 4):
        instrucao[i].replace("x", "")
        
    
    if c.tipo == 'r':
        c.rd  = format(int(instrucao[1]), "05b")
        c.rs1 = format(int(instrucao[2]), "05b")
        c.rs2 = format(int(instrucao[3]), "05b")

    elif c.tipo == 'i':
        c.rd  = format(int(instrucao[1]), "05b")
        c.rs1 = format(int(instrucao[2]), "05b")
        c.immediate = binario(int(instrucao[3]), 12)

    elif c.tipo == 's':
        c.rs2 = format(int(instrucao[1]), "05b")
        c.rs1 = format(int(instrucao[2]), "05b")
        c.immediate = format(int(instrucao[3]), '012b')

    elif c.tipo == 'b':
        c.rs1 = format(int(instrucao[1]), "05b")
        c.rs2 = format(int(instrucao[2]), "05b")
        c.immediate = format(int(instrucao[3]), '013b')

    
def printaResultado(c):
    resultado = ""

    

#ler nome do arquivo
nomeArquivo = nomeArquivo = sys.argv[1]

#ler arquivo de entrada
with open('src/'+nomeArquivo, 'r', encoding='utf-8') as arq:
    instrucoes = arq.read()
    #print(instrucoes)

#dividir linha por \n
vetInstrucoes = instrucoes.split('\n')

if len(sys.argv) > 2:
    saida = open('src/' + sys.argv[2], 'w', encoding='utf-8')
else:
    saida = sys.stdout

#dividir cada linha com , ou ' '
for linha in vetInstrucoes:
    
    instrucao = linha.replace(",", "")
    instrucao = instrucao.split()

    #print(instrucao)
    c = Comando()
    

    #definir formato a partir da primeira palavra
    match instrucao[0]:
        case 'add' | 'and' | 'or' | 'sub' | 'sll' | 'xor' | 'srl':
            
            c.tipo = 'r'

        case 'addi' | 'andi' | 'ori' | 'lb' | 'lw' | 'lh':
            
            c.tipo = 'i'

        case 'sw' | 'sh' | 'sb':
            
            c.tipo = 's'

        case _:
            
            c.tipo = 'b'

    indentificaComando(instrucao, c)

    if(c.tipo == 'r'):
        print(c.funct7 + c.rs2 + c.rs1 + c.funct3 + c.rd, end="", file=saida)
    elif(c.tipo == 's'):
        i = 11
        while(i >= 5):
            print(c.immediate[i], end="", file=saida)
            i = i - 1

        print(c.rs2 + c.rs1 + c.funct3 + c.immediate[4:0], end="", file=saida)
        
        i = 4

        while(i >= 0):
            print(c.immediate[i], end="", file=saida)
            i = i - 1
        

    elif(c.tipo == 'i'):
        
        print(c.immediate + c.rs1 + c.funct3 + c.rd, end="", file=saida)

    else:
        print(c.immediate[12], end="", file=saida)
        i = 10

        while(i >= 5):
            print(c.immediate[i], end="", file=saida)
            i = i - 1

        print(c.rs2 + c.rs1 + c.funct3, end="", file=saida)

        i = 4

        while(i >= 1):
            print(c.immediate[i], end="", file=saida)
            i = i - 1

        print(c.immediate[11], end="", file=saida)

        
    print(c.opcode, file=saida)