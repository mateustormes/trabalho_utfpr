# trabalho_utfpr
O programa roda em Python 3 (https://www.python.org/downloads/). 

Recomendado adicionar o Python ao PATH do sistema, bem como instalar o pip. Ambas as opções estão disponíveis no instalador 
da versão mais recente.
Além do python precisamos das seguintes bibliotecas: OpenCV, numpy e matplotlib
Para instalar essas bibliotecas, é necessário utilizar os seguintes comandos num terminal com acesso elevado (cmd, executar como administrador ou sudo nas distribuições do Linux):

pip3 install opencv-python
pip3 install numpy
pip3 install matplotlib
pip3 install scikit-learn
pip3 install progress

Execute o main.py
Dentro da pasta Rock-Paper-Scissors tem o conjunto de imagens que serão utilizados no teste e no treino
Dentro da pasta results é salvo o histograma gerados

As 3 imagens escolhidas: serão utilizadas para colocar na linha 31 
(image_path = 'imagem_escolhida.png' #'imagem_escolhida2.png' ou 'imagem_escolhida3.png')

O sistema irá identificar qual a imagem e transformar em texto, se for a imagem de um papel, ele irá anotar papel, e irá fazer um sorteio entre (paper, scissor e rock), e após irá dar o resultado do Jokempo


Para fazer funcionar somente executar o main.py, caso queira trocar sua imagem do Jokempo é só alterar a linha 31