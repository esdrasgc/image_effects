# Image effects
## efeitos de imagem à moda antiga e raiz

### Introdução  
Este programa utiliza a biblioteca OpenCV para realizar uma rotação de imagem em tempo real a partir da webcam do seu computador, além de permitir aplicar cisalhamento de forma dinâmica.

### Equações implementadas  
O programa utiliza as seguintes equações para gerar a rotação da imagem:

#### Matriz de rotação:  
Para girar a imagem em torno do seu próprio eixo, foi utilizada uma matriz de rotação 3x3 que é composta por uma matriz de rotação em 2D na dimensão XY e uma matriz de identidade na terceira dimensão. A matriz de rotação em 2D é construída a partir do ângulo de rotação theta, utilizando as funções trigonométricas sin e cos. A razão de a matriz ser 3x3, é para permitir translações a partir de multiplicação matricial, tópico do próximo ponto.

#### Matriz de translação:  
para centralizar a imagem, é aplicada uma translação que move o ponto central da imagem para a origem do sistema de coordenadas. A matriz de translação é definida a partir da metade da altura e largura da imagem. Essa matriz é formada por uma matriz identidade 3x3 com uma alterção nas componentes da última coluna, responsável por determinar a rotação. O vetor coluna para isso é [ deltaX, deltaY, 1], permitindo transladar a imagem em relação a origem (0,0) para (deltaX, deltaY). 

#### Matriz cisalhamento:  
para realizar um cisalhamento na imagem, foi utilizado uma matriz de cisalhamento 3x3 que adiciona uma proporção p1 da coordenada y à coordenada x e uma proporção p2 da coordenada x à coordenada y.

### Como usar?  
Para rodar o programa, execute o arquivo demo.py. O programa é executado em tempo real a partir da webcam do seu computador. As teclas abaixo podem ser usadas para realizar as seguintes ações:

q: encerra o programa.
a: diminui a velocidade de rotação da imagem.
d: aumenta a velocidade de rotação da imagem.
c: realiza um cisalhamento para a direita.
x: realiza um cisalhamento para a esquerda.
v: realiza um cisalhamento para baixo.
b: realiza um cisalhamento para cima.

Além de tudo, ao finalizar o programa com a tecla 'q', o video é salvo e você pode assistir!

### Diferencial  
Para evitar falhas na imagem apresentada, é utilizada a estratégia de, ao invés de aplicar as transformações da imagem de origem para gerar a de destino, ou seja, realizar a transformação linear do espaço vetorial dos pixels de origem para os de destino, foi realizado o caminho inverso.  
Dessa forma, evitasse perda de informação ao realizar a transformação por questões de arrendodamento, tendo em vista que não existe "meio pixel". Com isso todos os pontos da imagem de destino são mapeados para algum ponto da imagem de origem (ainda que haja repetição). Segue abaixo as equações matemáticas:
Xd = (T)^-1 @ C @ R @ T @ Xo 
Em que Xd é a matriz de destino (imagem apresentada em tela), T é a matriz de translação, C é a matriz de cisalhamento, R é a matriz de rotação e Xo é a matriz de origem (a imagem capturada pela camêra). 
Essa equação pode ser representada por Xd = A @ Xo, em que A seria a multiplicação das matrizes de transformação. 
Têm-se então que, multiplicando por (A)^-1 do lado direito de ambos os lados da equação, chega-se à:
(A)^-1 @ Xd = Xo
Com isso, é possível mapear quais pontos da origem vão corresponder a cada ponto da imagem de destino, permitindo assim, a garantia da qualidade de imagem. 

### Como instalar?  
Para garantir o funcionamento da aplicação é recomedado a criação de um ambiente virtual (venv) para instalar as dependência, como apresentado em https://docs.python.org/3/library/venv.html.
Após a criação do ambiente, realizar a instalação das bibliotecas numpy e open-cv, com os seguintes comandos do terminal:
pip install numpy
pip install opencv-python

Protinho agora é só rodar o arquivo, através do comando python/python3 03-camera_demo.py ou sua IDE python de preferência. 
