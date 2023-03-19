Introdução
Este programa utiliza a biblioteca OpenCV para realizar uma rotação de imagem em tempo real a partir da webcam do seu computador.

Equações implementadas
O programa utiliza as seguintes equações para gerar a rotação da imagem:

Matriz de rotação: para girar a imagem em torno do seu próprio eixo, foi utilizada uma matriz de rotação 3x3 que é composta por uma matriz de rotação em 2D na dimensão XY e uma matriz de identidade na terceira dimensão. A matriz de rotação em 2D é construída a partir do ângulo de rotação theta, utilizando as funções trigonométricas sin e cos.

Matriz de translação: para centralizar a imagem, é aplicada uma translação que move o ponto central da imagem para a origem do sistema de coordenadas. A matriz de translação é definida a partir da metade da altura e largura da imagem.

Matriz cisalhamento: para realizar um cisalhamento na imagem, foi utilizado uma matriz de cisalhamento 3x3 que adiciona uma proporção p1 da coordenada y à coordenada x e uma proporção p2 da coordenada x à coordenada y.
Como usar
Para rodar o programa, execute o arquivo demo.py. O programa é executado em tempo real a partir da webcam do seu computador. As teclas abaixo podem ser usadas para realizar as seguintes ações:

q: encerra o programa.
a: diminui a velocidade de rotação da imagem.
d: aumenta a velocidade de rotação da imagem.
c: realiza um cisalhamento para a direita.
x: realiza um cisalhamento para a esquerda.
v: realiza um cisalhamento para baixo.
b: realiza um cisalhamento para cima.

Além de tudo, ao finalizar o programa com a tecla 'q', o video é salvo e você pode assistir!

Dependências
Este programa foi desenvolvido utilizando a linguagem Python 3 e as bibliotecas OpenCV e NumPy. Certifique-se de que as bibliotecas estão instaladas no seu ambiente antes de executar o programa.