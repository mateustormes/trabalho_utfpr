# trabalho_utfpr
O programa roda em Python 3 (https://www.python.org/downloads/). 

Conteúdo/estrutura (mínima):
Título do projeto
	Treinamento e Geração de Histograma com Detecção de Imagem para Jokempô
Equipe
	Mateus Tormes Gervazioni
Dataset
	https://github.com/mateustormes/trabalho_utfpr
Descrição do projeto
	Primeiramente ele faz o treinamento através de um conjunto de imagens, depois executa um conjunto de teste
	e obtém a acurácia do modelo, armazena em uma imagem e salva em results, após ele utiliza o mesmo conjunto de imagem e verifica oque a imagem_escolhida representa se é uma (tesoura, papel ou pedra)(jogador),
	após o reconhecimento é sorteado um numero aleatorio para o computador, e logo após é definido quem venceu,perdeu ou se houve empate.

As limitações e restrições do projeto incluem:
    1-Tamanho e qualidade das imagens: O desempenho do classificador pode ser afetado pela qualidade das imagens de entrada, como baixa resolução, ruído ou problemas de iluminação. Imagens de tamanho muito pequeno também podem prejudicar a precisão do modelo.

    2-Variação de fundo e posição: O classificador pode ser sensível a variações no fundo das imagens e na posição dos objetos (pedra, papel, tesoura). Se as imagens de treinamento não abrangerem uma ampla variedade de fundos e posições, o desempenho do classificador pode ser reduzido em situações reais.

    3-Limitação a três classes: O projeto está restrito às três classes específicas: pedra, papel e tesoura. Não é capaz de reconhecer outros objetos ou realizar classificações mais amplas.

    4-Dependência de colorimétricas: O método de extração de características utilizado (histograma de cores) é sensível às informações de cor das imagens. Isso significa que objetos com cores semelhantes podem ser confundidos pelo classificador, mesmo que tenham formas diferentes.

    5-Limitação do algoritmo de classificação: O uso de um classificador de Floresta Aleatória pode apresentar limitações em relação a outros algoritmos mais avançados de aprendizado de máquina. Embora o Random Forest seja um bom classificador geral, ele pode não ser adequado para todas as situações e pode não atingir a mesma precisão que métodos mais sofisticados.

    6-Dependência de um conjunto de dados específico: O projeto foi treinado e testado com um conjunto de dados específico, fornecido na pasta "Rock-Paper-Scissors". Para aplicar o classificador a outros conjuntos de dados ou objetos, pode ser necessário coletar, rotular e preparar um novo conjunto de dados de treinamento.

    7-Restrição à linguagem Python: O projeto foi implementado na linguagem Python e depende de bibliotecas específicas para funcionar corretamente. Se você deseja utilizar o projeto em outra linguagem de programação, será necessário reimplementá-lo e adaptá-lo de acordo.
Repositório do projeto
	https://github.com/mateustormes/trabalho_utfpr
Classificador e acurácia
	O código fornecido utiliza um classificador de Floresta Aleatória (Random Forest) para realizar 
	o reconhecimento de imagens do jogo "Pedra, Papel e Tesoura". Ele divide o processo em duas fases:
	treinamento e teste.
	O classificador utilizado é o Random Forest Classifier (da biblioteca Scikit-learn). A acurácia obtida 
	não é mencionada explicitamente no código fornecido, mas é calculada internamente durante a fase
	 de teste e exibida na matriz de confusão.

Instalação de Bibliotecas/Dependências:
    Recomendado adicionar o Python ao PATH do sistema, bem como instalar o pip. Ambas as opções estão disponíveis no instalador da versão mais recente.
    Além do python precisamos das seguintes bibliotecas abaixo: 
    Para instalar essas bibliotecas, é necessário utilizar os seguintes comandos num terminal com acesso elevado (cmd, executar como administrador ou sudo nas distribuições do Linux):

	pip3 install opencv-python
    pip3 install numpy
    pip3 install matplotlib
    pip3 install scikit-learn
    pip3 install progress
Estrutura de Pastas:
- Pasta do projeto
  - Rock-Paper-Scissors
    - train
      - Imagens de treinamento
    - test
      - Imagens de teste
  - imagem_escolhida.png / imagem_escolhida2.png / imagem_escolhida3.png
  - main.py (código fornecido)

Instalação e Execução
	Para executar o código, salve-o como main.py na pasta do seu projeto. Certifique-se de ter a estrutura 
	de pastas mencionada acima, com as imagens de treinamento e teste no diretório apropriado.

    Em seguida, você pode executar o script main.py. Ele realizará o treinamento do classificador,
    exibirá a acurácia, plotará a matriz de confusão e, finalmente, realizará a previsão para a imagem
    imagem_escolhida.png, exibindo o resultado do jogo. Certifique-se de ter todas as bibliotecas instaladas
    corretamente antes de executar o código.
Como jogar o Jokempo?
    Execute o main.py
    Dentro da pasta Rock-Paper-Scissors tem o conjunto de imagens que serão utilizados no teste e no treino
    Dentro da pasta results é salvo o histograma gerados

    As 3 imagens escolhidas: serão utilizadas para colocar na linha 31 
    (image_path = 'imagem_escolhida.png' #'imagem_escolhida2.png' ou 'imagem_escolhida3.png')

    O sistema irá identificar qual a imagem e transformar em texto, se for a imagem de um papel, ele irá anotar papel, e irá fazer um sorteio entre (paper, scissor e rock), e após irá dar o resultado do Jokempo

    Para fazer funcionar somente executar o main.py, caso queira trocar sua imagem do Jokempo é só alterar a linha 31