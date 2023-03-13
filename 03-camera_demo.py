import numpy as np

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv

## create a rotation matrix based on the angle
def rotMatrix(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])

## create a translation matrix based on the vector
def transMatrix(vector):
    return np.array([[1, 0, vector[0]], [0, 1, vector[1]], [0, 0, 1]])

## create a function that creates a grid of indices

def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 320
    height = 240

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.

    velocity = 1/60
    R = rotMatrix(velocity)
    R_inv = np.linalg.inv(R)
    T = transMatrix([width, height])
    T_inv = np.linalg.inv(T)
    A = T_inv @ R_inv @ T
    while True:
        
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255
        image_ = np.zeros_like(image)

        ##código daqui para baixo

        Xd = criar_indices(0, width, 0, height)
        Xd = np.vstack( (Xd, np.ones(Xd.shape[1])) )
        X = A @ Xd
        X = X.astype(int)
        # Xd = Xd.astype(int)

        filtro = ((Xd[0,:]>=0) & (Xd[0,:]<image_.shape[0])) & ((Xd[1,:]>=0) & (Xd[1,:]<image_.shape[1]))
        X = X[:, filtro]
        Xd = Xd[:, filtro]

        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]
        

        ##Código daqui para cima

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image)
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
