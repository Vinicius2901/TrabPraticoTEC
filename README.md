Trabalho prático desenvolvido por Felipe Godinho Dal Molin e Vinícius Giroti para a matéria de Teoria da Computação (TEC0001) da Universidade de Santa Catarina (UDESC).
O trabalho tem como objetivo realizar um simulador do modelo de Máquina de Turing de Sipser para o modelo de Máquina de Turing com Fita Duplamente Infinita, assim como um simulador do modelo de Máquina de Turing com Fita Duplamente Infinita para o modelo de Máquina de Turing de Sipser.

Para baixar o código, basta baixar o repositório e extraí-lo na pasta de seu interesse.

O código foi desenvolvido utilizando a versão 3.12.3 do interpretador Python no sistema operacional "Ubuntu 24.04.3 LTS".

Não é necessário criar ou utilizar um ambiente virtual Python para executar o código, uma vez que não se precisa de módulos adicionais além dos que já são inclusos ao baixar o interpretador Python (os e sys).

A primeira linha do arquivo de entrada deve conter ";S" ou ";I" apenas. ;S indica que a máquina de entrada é uma máquina de Sipser que será simulada por uma máquina com fita duplamente infinita. Já ;I indica que a máquina de entrada é uma máquina com fita duplamente infinita que será simulada por uma máquina de Sipser.

Para executar o código, basta digitar "python3 main.py <nomeDoArquivo.ext>" no terminal. (nomeDoArquivo indica o nome do arquivo com a Máquina de Turing de entrada e ext significa extensão do arquivo).

O arquivo de saída da execução terá o nome de "TM_Translated.txt".

Para testar se a simulação deu certo, execute a máquina de entrada (<nomeDoArquivo.ext>) e a máquina de saída (<TM_Translated.txt>) no simulador com o link: http://morphett.info/turing/turing.html. Ambas devem retornar o mesmo resultado para uma mesma entrada.
