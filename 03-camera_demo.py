import math
import numpy as np

import cv2 as cv

def rotMatrix(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])

def transMatrix(vector):
    return np.array([[1, 0, vector[0]], [0, 1, vector[1]], [0, 0, 1]])


def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def run():
    cap = cv.VideoCapture(0)

    width = 320
    height = 240
    # width = 1920
    # height = 1080

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.

    velocity = 1/60
    i = 0
    R = rotMatrix(velocity)
    R_inv = np.linalg.inv(R)
    T = transMatrix([-height/2, -width/2])
    T_inv = np.linalg.inv(T)
    A = T_inv @ R @ T
    degree = 0
    
    while True:
        
        # Captura um frame da câmera
        ret, frame = cap.read()

        if not ret:
            print("Não consegui capturar frame!")
            break


        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255
        image_ = np.zeros_like(image)

        ##código daqui para baixo

        Xd = criar_indices(0, image.shape[0], 0, image.shape[1])
        Xd = np.vstack( (Xd, np.ones(Xd.shape[1])) )
        X = np.linalg.inv(A) @ Xd
        # X = Xd
        X = X.astype(int)
        Xd = Xd.astype(int)

        filtro = (X[0,:] >=0) & (X[0,:] < image_.shape[0]) & (X[1,:] >=0) & (X[1,:] < image_.shape[1])
        Xd = Xd[:, filtro]
        X = X[:, filtro]
        

        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]
        
        degree += velocity
        A = T_inv @ rotMatrix((degree)) @ T
        i += 1
        cv.imshow('Minha Imagem!', image_)
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

        elif cv.waitKey(1) == ord('a'):
            velocity = velocity- (1/60)
            print("Velocidade angular: ", velocity)
        elif cv.waitKey(1) == ord('d'): 
            velocity = velocity + (1/60)

        if cv.waitKey(1) == ord('x'):
            # change the collor of the frame to black and white
            image_ = cv.applyColorMap(image_, cv.COLORMAP_WINTER)

            

    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
