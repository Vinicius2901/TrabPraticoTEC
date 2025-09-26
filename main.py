import os

TM_Path = "TM.txt"
TM_Trans_Path = "TM_Translated.txt"
with open(TM_Path, "r") as f_in:
    linha = f_in.readline()
    with open(TM_Trans_Path, "w+") as f_out:
        if "S" in linha:
            # Marca símbolo inicial
            f_out.write("0 0 S R sr0\n")
            f_out.write("0 1 S R sr1\n")
            f_out.write("0 _ S R 0I\n")
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
            f_out.write("ini S S R 0I\n")
            f_out.write("\n")
            
            estadosVisitados = []
            estadosAVisitar = []
            for line in f_in.readlines():
                if(";" in line):
                    line = line.replace("\n", "")
                    f_out.write(f"{line} from Sipser\n")
                    continue
                estados = line.split(" ")
                if (line != "\n"):
                    if estados[0] not in estadosVisitados and estados[4] not in estadosVisitados:
                        estadosVisitados.append(estados[0])
                        
                        # Transição para simular a mola
                        f_out.write(f"{estados[0]}I S S R {estados[0]}I\n")
                        
                        if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                            estadosAVisitar.append(estados[4])
                    estados[0] = f"{estados[0]}I"
                    if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                        estados[4] = estados[4].replace("\n", "")
                        estados[4] = f"{estados[4]}I\n"
                    f_out.write(f"{estados[0]} {estados[1]} {estados[2]} {estados[3]} {estados[4]}")
                else:
                    f_out.write("\n")
            for estado in estadosAVisitar:
                estado = estado.replace("\n", "")
                if estado not in estadosVisitados:
                    f_out.write(f"\n{estado}I S S R {estado}I\n")
        elif "I" in linha:
            # Marca símbolo inicial
            f_out.write("0 0 S R sr0\n")
            f_out.write("0 1 S R sr1\n")
            f_out.write("0 _ S R mf\n")
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
            
            f_out.write("mf _ F L ini\n")
            
            # Volta o cabeçote para a célula mais à esquerda de Sipser
            f_out.write("ini 0 0 L ini\n")
            f_out.write("ini 1 1 L ini\n")
            f_out.write("ini S S R 0S\n")
            f_out.write("\n")
            
            estadosVisitados = []
            estadosAVisitar = []
            for line in f_in.readlines():
                if(";" in line):
                    line = line.replace("\n", "")
                    f_out.write(f"{line} from Double-Infinite tape\n")
                    continue
                estados = line.split(" ")
                if (line != "\n"):
                    if estados[0] not in estadosVisitados and estados[4] not in estadosVisitados:
                        estadosVisitados.append(estados[0])
                        
                        # Mandar para o estado de correção da fita para esquerda e para a direita
                        f_out.write(f"{estados[0]}S S S R ltc_{estados[0]}\n")
                        f_out.write(f"{estados[0]}S F _ R rtc_{estados[0]}\n")
                        
                        if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                            estadosAVisitar.append(estados[4])
                    estados[0] = f"{estados[0]}S"
                    if ("halt" not in estados[4]) and ("halt-accept" not in estados[4]):
                        estados[4] = estados[4].replace("\n", "")
                        estados[4] = f"{estados[4]}S\n"
                    f_out.write(f"{estados[0]} {estados[1]} {estados[2]} {estados[3]} {estados[4]}")
                else:
                    f_out.write("\n")
            for estado in estadosVisitados:
                # Cheguei no limite da fita de Sipser e acessei um branco antes dela
                f_out.write(f"ltc_{estado} 0 _ R sr0_{estado}\n")
                f_out.write(f"ltc_{estado} 1 _ R sr1_{estado}\n")
                f_out.write(f"ltc_{estado} _ _ R sr__{estado}\n")
                f_out.write(f"ltc_{estado} F _ R srF_{estado}\n")
                
                # Shift Right de zeros
                f_out.write(f"\nsr0_{estado} 0 0 R sr0_{estado}\n")
                f_out.write(f"sr0_{estado} 1 0 R sr1_{estado}\n")
                f_out.write(f"sr0_{estado} _ 0 R sr__{estado}\n")
                f_out.write(f"sr0_{estado} F 0 R srF_{estado}\n")
                
                # Shift Right de uns
                f_out.write(f"\nsr1_{estado} 0 1 R sr0_{estado}\n")
                f_out.write(f"sr1_{estado} 1 1 R sr1_{estado}\n")
                f_out.write(f"sr1_{estado} _ 1 R sr__{estado}\n")
                f_out.write(f"sr1_{estado} F 1 R srF_{estado}\n")
                
                # Shift Right de _
                f_out.write(f"\nsr__{estado} 0 _ R sr0_{estado}\n")
                f_out.write(f"sr__{estado} 1 _ R sr1_{estado}\n")
                f_out.write(f"sr__{estado} _ _ R sr__{estado}\n")
                f_out.write(f"sr__{estado} F _ R srF_{estado}\n")
                
                # Shift Right de F
                f_out.write(f"\nsrF_{estado} _ F L ini_{estado}\n")
                
                # Corrigir o cabeçote
                f_out.write(f"\nini_{estado} _ _ L ini_{estado}\n")
                f_out.write(f"ini_{estado} 0 0 L ini_{estado}\n")
                f_out.write(f"ini_{estado} 1 1 L ini_{estado}\n")
                f_out.write(f"ini_{estado} S S R {estado}S\n")
                
                # Correção da fita à direita
                f_out.write(f"\nrtc_{estado} _ F L {estado}S\n")
                
            for estado in estadosAVisitar:
                estado = estado.replace("\n", "")
                if estado not in estadosVisitados:
                    # Cheguei no limite da fita de Sipser e acessei um branco antes dela
                    f_out.write(f"ltc_{estado} 0 _ R sr0_{estado}\n")
                    f_out.write(f"ltc_{estado} 1 _ R sr1_{estado}\n")
                    f_out.write(f"ltc_{estado} _ _ R sr__{estado}\n")
                    f_out.write(f"ltc_{estado} F _ R srF_{estado}\n")
                    
                    # Shift Right de zeros
                    f_out.write(f"\nsr0_{estado} 0 0 R sr0_{estado}\n")
                    f_out.write(f"sr0_{estado} 1 0 R sr1_{estado}\n")
                    f_out.write(f"sr0_{estado} _ 0 R sr__{estado}\n")
                    f_out.write(f"sr0_{estado} F 0 R srF_{estado}\n")
                    
                    # Shift Right de uns
                    f_out.write(f"\nsr1_{estado} 0 1 R sr0_{estado}\n")
                    f_out.write(f"sr1_{estado} 1 1 R sr1_{estado}\n")
                    f_out.write(f"sr1_{estado} _ 1 R sr__{estado}\n")
                    f_out.write(f"sr1_{estado} F 1 R srF_{estado}\n")
                    
                    # Shift Right de _
                    f_out.write(f"\nsr__{estado} 0 _ R sr0_{estado}\n")
                    f_out.write(f"sr__{estado} 1 _ R sr1_{estado}\n")
                    f_out.write(f"sr__{estado} _ _ R sr__{estado}\n")
                    f_out.write(f"sr__{estado} F _ R srF_{estado}\n")
                    
                    # Shift Right de F
                    f_out.write(f"\nsrF_{estado} _ F L ini_{estado}\n")
                    
                    # Corrigir o cabeçote
                    f_out.write(f"\nini_{estado} _ _ L ini_{estado}\n")
                    f_out.write(f"ini_{estado} 0 0 L ini_{estado}\n")
                    f_out.write(f"ini_{estado} 1 1 L ini_{estado}\n")
                    f_out.write(f"ini_{estado} S S R {estado}S\n")
                    
                    # Correção da fita à direita
                    f_out.write(f"\nrtc_{estado} _ F L {estado}S\n")