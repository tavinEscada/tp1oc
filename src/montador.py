import re

class Comando:
    def _innit_(self, funct7, rs2, rs1, funct3, rd, opcode, immediate, tipo):
        self.tipo = tipo
        self.funct7 = funct7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode
        self.immediate = immediate

def indentificaComando(instrucao, c):
    c.immediate = ''
    c.rs2 = ''
    c.funct7 = ''
    c.opcode = ''

    match instrucao[0]:
        case 'add' | 'beq' | 'addi' | 'lb' | 'sb' | 'sub':
            c.funct3 = '000'

        case 'lh' | 'sh' | 'sll':
            c.funct3 = '001'

        case 'lw' | 'sw':
            c.funct3 = '010'

        case 'sd':
            c.funct3 = '011'

        case 'xor':
            c.funct3 = '100'

        case 'srl':
            c.funct3 = '101'

        case 'ori' | 'or':
            c.funct3 = '110'

        case 'andi' | 'and':
            c.funct3 = '111'

    match instrucao[0]:
        case 'add' | 'sll' | 'xor' | 'or' | 'and':
            c.funct7 = '0000000'

        case _:
            c.funct7 = '0100000'

    match instrucao[0]:
        case 'add' | 'and' | 'or' | 'slr' | 'sll' | 'sub' | 'xor':
            c.opcode = '0110011'

        case 'beq' | 'bne':
            c.opcode = '1100011'

        case 'lb' | 'lh' | 'lw':
            c.opcode = '0000011'

        case 'sb' | 'sw' | 'sh':
            c.opcode = '0100011'

        case 'andi' | 'ori' | 'addi':
            c.opcode = '0010011'

    
    for i in range(3):
        instrucao[i+1] = instrucao[i+1].replace("x", "")

    if(c.tipo == 'r'):

        c.rd = format(int(instrucao[1]), '05b')
        c.rs1 = format(int(instrucao[2]), '05b')
        c.rs2 = format(int(instrucao[3]), '05b')
    

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
    
    instrucao = linha.replace(",", "")
    instrucao = instrucao.split()

    #print(instrucao)
    c = Comando()
    

    #definir formato a partir da primeira palavra
    match instrucao[0]:
        case 'add' | 'and' | 'or' | 'sub' | 'sll' | 'xor' | 'srl':
            
            c.tipo = 'r'

            #identifica inst
            

        case 'addi' | 'andi' | 'ori' | 'lb' | 'lw' | 'lh':
            
            c.tipo = 'i'


        case 'sw' | 'sh' | 'sb':
            
            c.tipo = 's'

        case _:
            
            c.tipo = 'b'

    indentificaComando(instrucao, c)
    if(c.tipo == 'r'):
        print(c.funct7 + c.rs2 + c.rs1 + c.funct3 + c.rd + c.opcode)

