import re

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

def indentificaComando(instrucao, c):
    

    match instrucao[0]:
        case 'add' | 'beq' | 'addi' | 'lb' | 'sb' | 'sub':
            c.funct3 = '000'

        case 'lh' | 'sh' | 'sll':
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
    def regBin(token):
        return format(int(token.replace("x", "")), '05b')
    
    if c.tipo == 'r':
        # add rd, rs1, rs2
        c.rd  = regBin(instrucao[1])
        c.rs1 = regBin(instrucao[2])
        c.rs2 = regBin(instrucao[3])

    elif c.tipo == 'i':
        # addi rd, rs1, imm   OU   lw rd, imm(rs1)
        c.rd  = regBin(instrucao[1])
        c.rs1 = regBin(instrucao[2])
        c.immediate = format(int(instrucao[3]), '012b')

    elif c.tipo == 's':
        # sw rs2, imm(rs1)    — o que é armazenado é rs2; base é rs1
        c.rs2 = regBin(instrucao[1])
        c.rs1 = regBin(instrucao[2])
        c.immediate = format(int(instrucao[3]), '012b')

    elif c.tipo == 'b':
        # beq rs1, rs2, imm
        c.rs1 = regBin(instrucao[1])
        c.rs2 = regBin(instrucao[2])
        # imediato de 13 bits (bit 0 implícito = 0)   FIX 6
        c.immediate = format(int(instrucao[3]), '013b')

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
        print(c.funct7 + c.rs2 + c.rs1 + c.funct3 + c.rd, end="")
    elif(c.tipo == 's'):
        
        print(c.immediate[11:5], c.rs2, c.rs1, c.funct3, c.immediate[4:0], end="")

    elif(c.tipo == 'i'):
        
        print(c.immediate[11:0], c.rs1, c.funct3, c.rd, end="")

    else:
        print(c.immediate[12], c.immediate[10:5], c.rs2, c.rs1, c.funct3, c.immediate[4:1], c.immediate[11], end="")

        
    print(c.opcode)