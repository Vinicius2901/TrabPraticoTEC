Trabalho prático desenvolvido por Felipe Godinho Dal Molin e Vinícius Giroti para a matéria de Teoria da Computação (TEC0001) da Universidade de Santa Catarina (UDESC).
O trabalho tem como objetivo realizar um simulador do modelo de Máquina de Turing de Sipser para o modelo de Máquina de Turing com Fita Duplamente Infinita, assim como um simulador do modelo de Máquina de Turing com Fita Duplamente Infinita para o modelo de Máquina de Turing de Sipser.

Sobre a instalação:

Para baixar o código, basta baixar o repositório e extraí-lo na pasta de seu interesse.

Sobre a execução:

O código foi desenvolvido utilizando a versão 3.12.3 do interpretador Python no sistema operacional "Ubuntu 24.04.3 LTS".

Não é necessário criar ou utilizar um ambiente virtual Python para executar o código, uma vez que não se precisa de módulos adicionais além dos que já são inclusos ao baixar o interpretador Python (os e sys).

A primeira linha do arquivo de entrada deve conter ";S" ou ";I" apenas. ;S indica que a máquina de entrada é uma máquina de Sipser que será simulada por uma máquina com fita duplamente infinita. Já ;I indica que a máquina de entrada é uma máquina com fita duplamente infinita que será simulada por uma máquina de Sipser.

Para executar o código, basta digitar "python3 main.py <nomeDoArquivo.ext>" no terminal. (nomeDoArquivo indica o nome do arquivo com a Máquina de Turing de entrada e ext significa extensão do arquivo).

O arquivo de saída da execução terá o nome de "TM_Translated.txt".

Sobre a lógica do código:

Pelo motivo de símbolos como "#" e "&" não pertencerem ao alfabeto da fita da máquina de entrada, "#" foi o símbolo utilizado para marcar o primeiro símbolo da fita tanto na simulação da máquina de Sipser para a Duplamente Infinita, tanto na simulação contrária e "&" foi utilizado para marcar a extremidade à esquerda na simulação da máquina com Fita duplamente infinita para a máquina de Sipser. Esses símbolos são necessários para operações de ajustes.

Para simular a máquina de Sipser na máquina com fita duplamente infinita, bastou marcar o primeiro símbolo da entrada, fazer um "shift right" de toda a entrada e manter os estados originais e transições, com adição da transição
(qx, #) -> (qx, R, #) para todos os estados. Além disso, os estados originais foram renomeados para "xI", sendo x o nome do estado original, para indicar que são estados da máquina com fita duplamente infinita que simula a de Sipser e impedir conflitos com o estado inicial, visto que as máquinas devem ter como estado inicial "0". Já para o contrário, foi necessário marcar tanto o símbolo inicial, tanto o símbolo final, fazendo "shift right" de toda a entrada. Além disso, foi adicionado um procedimento para quando o cabeçote da fita atingisse cada extremidade. Visando manter a máquina determinística, cada estado realiza uma transição para um estado que inicia o procedimento de correção da fita à esquerda para aquele estado caso leia o símbolo ("#") e cada estado envia para um outro estado que inicializa o procedimento de correção da fita à direita caso o cabeçote leia o símbolo ("&"). Quanto aos estados e transições, os nomes dos estados foram alterados para "xS", sendo x o nome do estado original e todas as transições originais foram mantidas.

Para testar se a simulação deu certo, execute a máquina de entrada (<nomeDoArquivo.ext>) e a máquina de saída (<TM_Translated.txt>) no simulador com o link: http://morphett.info/turing/turing.html. Ambas devem retornar o mesmo resultado para uma mesma entrada.
