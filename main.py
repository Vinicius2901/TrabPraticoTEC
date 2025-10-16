import os
import sys

def initialize_DInf(f_out):
    # Marca símbolo inicial
    f_out.write("0 0 # R sr0\n")
    f_out.write("0 1 # R sr1\n")
    f_out.write("0 _ # R 0I\n")
    f_out.write("\n")
    
    # Shift Right de zeros
    f_out.write("sr0 0 0 R sr0\n")
    f_out.write("sr0 1 0 R sr1\n")
    f_out.write("sr0 _ 0 L ini\n")
    f_out.write("\n")
    
    #Shift Right de uns
    f_out.write("sr1 0 1 R sr0\n")
    f_out.write("sr1 1 1 R sr1\n")
    f_out.write("sr1 _ 1 L ini\n")
    f_out.write("\n")
    
    # Volta o cabeçote para a célula mais à esquerda de Sipser
    f_out.write("ini 0 0 L ini\n")
    f_out.write("ini 1 1 L ini\n")
    f_out.write("ini # # R 0I\n")
    f_out.write("\n")

def initialize_Sipser(f_out):
    # Marca símbolo inicial
    f_out.write("0 0 # R sr0\n")
    f_out.write("0 1 # R sr1\n")
    f_out.write("0 _ # R mf\n")
    f_out.write("\n")
    
    # Shift Right de zeros
    f_out.write("sr0 0 0 R sr0\n")
    f_out.write("sr0 1 0 R sr1\n")
    f_out.write("sr0 _ 0 R mf\n")
    f_out.write("\n")
    
    #Shift Right de uns
    f_out.write("sr1 0 1 R sr0\n")
    f_out.write("sr1 1 1 R sr1\n")
    f_out.write("sr1 _ 1 R mf\n")
    f_out.write("\n")
    
    f_out.write("mf _ & L ini\n")
    
    # Volta o cabeçote para a célula mais à esquerda de Sipser
    f_out.write("ini 0 0 L ini\n")
    f_out.write("ini 1 1 L ini\n")
    f_out.write("ini # # R 0S\n")
    f_out.write("\n")

def correcao_Sipser(f_out, estado):
    # Cheguei no limite da fita de Sipser e acessei um branco antes dela
    f_out.write(f"ltc_{estado} 0 _ R sr0_{estado}\n")
    f_out.write(f"ltc_{estado} 1 _ R sr1_{estado}\n")
    f_out.write(f"ltc_{estado} _ _ R sr__{estado}\n")
    f_out.write(f"ltc_{estado} & _ R srF_{estado}\n")
    
    # Shift Right de zeros
    f_out.write(f"\nsr0_{estado} 0 0 R sr0_{estado}\n")
    f_out.write(f"sr0_{estado} 1 0 R sr1_{estado}\n")
    f_out.write(f"sr0_{estado} _ 0 R sr__{estado}\n")
    f_out.write(f"sr0_{estado} & 0 R srF_{estado}\n")
    
    # Shift Right de uns
    f_out.write(f"\nsr1_{estado} 0 1 R sr0_{estado}\n")
    f_out.write(f"sr1_{estado} 1 1 R sr1_{estado}\n")
    f_out.write(f"sr1_{estado} _ 1 R sr__{estado}\n")
    f_out.write(f"sr1_{estado} & 1 R srF_{estado}\n")
    
    # Shift Right de _
    f_out.write(f"\nsr__{estado} 0 _ R sr0_{estado}\n")
    f_out.write(f"sr__{estado} 1 _ R sr1_{estado}\n")
    f_out.write(f"sr__{estado} _ _ R sr__{estado}\n")
    f_out.write(f"sr__{estado} & _ R srF_{estado}\n")
    
    # Shift Right de F
    f_out.write(f"\nsrF_{estado} _ & L ini_{estado}\n")
    
    # Corrigir o cabeçote
    f_out.write(f"\nini_{estado} _ _ L ini_{estado}\n")
    f_out.write(f"ini_{estado} 0 0 L ini_{estado}\n")
    f_out.write(f"ini_{estado} 1 1 L ini_{estado}\n")
    f_out.write(f"ini_{estado} # # R {estado}S\n")
    
    # Correção da fita à direita
    f_out.write(f"\nrtc_{estado} _ & L {estado}S\n")

def copy_Sipser_to_DInf(f_in, estadosVisitados, estadosAVisitar, f_out):
    for line in f_in.readlines():
        estados = line.split(" ")
        while "" in estados:
            estados.remove("")
        if(";" in estados[0]):
            line = line.replace("\n", "")
            f_out.write(f"{line} from Sipser\n")
            continue
        if (line != "\n" and estados[0] != ";"):
            if estados[0] not in estadosVisitados and estados[4] not in estadosVisitados:
                estadosVisitados.append(estados[0])
                
                # Transição para simular a mola
                f_out.write(f"{estados[0]}I # # R {estados[0]}I\n")
                
                if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                    estadosAVisitar.append(estados[4])
            estados[0] = f"{estados[0]}I"
            if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                estados[4] = estados[4].replace("\n", "")
                estados[4] = f"{estados[4]}I"
            f_out.write(f"{estados[0]} {estados[1]} {estados[2]} {estados[3]} {estados[4]}")
        if len(estados) > 5:
            if(";" in estados[5]):
                for i in range(5, len(estados)):
                    estados[i] = estados[i].replace("\n", "")
                    f_out.write(f" {estados[i]}")
                f_out.write(" from Sipser")
        f_out.write("\n")

def copy_DInf_to_Sipser(f_in, estadosVisitados, estadosAVisitar, f_out):
    for line in f_in.readlines():
        estados = line.split(" ")
        while "" in estados:
            estados.remove("")
        if(";" in estados[0]):
            line = line.replace("\n", "")
            f_out.write(f"{line} from Double-Infinite tape\n")
            continue
        if (line != "\n" and estados[0] != ";"):
            if estados[0] not in estadosVisitados and estados[4] not in estadosVisitados:
                estadosVisitados.append(estados[0])
                
                # Mandar para o estado de correção da fita para esquerda e para a direita
                f_out.write(f"{estados[0]}S # # R ltc_{estados[0]}\n")
                f_out.write(f"{estados[0]}S & _ R rtc_{estados[0]}\n")
                
                if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                    estadosAVisitar.append(estados[4])
            estados[0] = f"{estados[0]}S"
            if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                estados[4] = estados[4].replace("\n", "")
                estados[4] = f"{estados[4]}S"
            f_out.write(f"{estados[0]} {estados[1]} {estados[2]} {estados[3]} {estados[4]}")
        if len(estados) > 5:
            if(";" in estados[5]):
                for i in range(5, len(estados)):
                    estados[i] = estados[i].replace("\n", "")
                    f_out.write(f" {estados[i]}")
                f_out.write(" from Double-Infinite tape")
        f_out.write("\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        TM_Path = sys.argv[1]
    else:
        raise Exception("Nome do arquivo da máquina que será traduzido deve ser colocado como argumento da execução")
    TM_Trans_Path = "TM_Translated.txt"
    with open(TM_Path, "r") as f_in:
        linha = f_in.readline()
        with open(TM_Trans_Path, "w+") as f_out:
            # Verificação se a formatação de comentário da primeira linha está correta
            verifica_MT = linha.split(" ")
            verifica_MT[-1] = verifica_MT[-1].replace("\n", "")
            while "" in verifica_MT:
                verifica_MT.remove("")
            idx_pv = -1
            idx_si = -1
            if ";" in verifica_MT:
                idx_pv = verifica_MT.index(";")
            if "S" in verifica_MT:
                idx_si = verifica_MT.index("S")
            elif "I" in verifica_MT:
                idx_si = verifica_MT.index("I")

            if(len(verifica_MT) > 2):
                raise Exception("Primeira linha deve conter apenas ';' e 'S' ou ';' e 'I' seguidos")
            elif ";S" in linha or ((idx_pv < idx_si) and "S" in linha):
                initialize_DInf(f_out)
                estadosVisitados = []
                estadosAVisitar = []
                copy_Sipser_to_DInf(f_in, estadosVisitados, estadosAVisitar, f_out)
                for estado in estadosAVisitar:
                    estado = estado.replace("\n", "")
                    if estado not in estadosVisitados:
                        f_out.write(f"\n{estado}I # # R {estado}I\n")
        
            elif ";I" in linha or ((idx_pv < idx_si) and "I" in linha):
                initialize_Sipser(f_out)
                estadosVisitados = []
                estadosAVisitar = []
                copy_DInf_to_Sipser(f_in, estadosVisitados, estadosAVisitar, f_out)

                for estado in estadosVisitados:
                    correcao_Sipser(f_out, estado)
                    
                for estado in estadosAVisitar:
                    estado = estado.replace("\n", "")
                    if estado not in estadosVisitados:
                        correcao_Sipser(f_out, estado)
            else:
                raise Exception("Primeira linha deve conter apenas ';' e 'S' ou ';' e 'I' seguidos")
