import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        phsv = fhsv[y, x]
        print(f'Posição ({x}, {y}), HSV: {phsv}')

video = cv2.VideoCapture('./video.mp4')

if (video.isOpened() == False):
    print("Error!") 
else:
    pausa = False  
    contbact = 0  
    tpinicial = time.time() 
    
    cv2.namedWindow('Resultado')
    cv2.setMouseCallback('Resultado', mouse)
    
    tempos = []
    bacterias = [] 
    
    while True:
        if not pausa:
            ret, frame = video.read()
            if not ret:
                break

            fhsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            min = np.array([102, 212, 11])  
            max = np.array([120, 255, 255])

            mask = cv2.inRange(fhsv, min, max)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            result = frame.copy()
            cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

            nbacteris = len(contours)
            cv2.putText(result, f'Bacterias: {nbacteris}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            contbact += nbacteris

            cv2.imshow('Resultado', result)
            
            tempo_atual = time.time() - tpinicial
            
            tempos.append(tempo_atual)
            bacterias.append(contbact)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('e'):
            break
        elif key & 0xFF == ord('q'):
            pausa = not pausa  

    print(f'Total de bactérias encontradas: {contbact}')
    
    plt.plot(tempos, bacterias)
    plt.xlabel('Tempo(s)')
    plt.ylabel('Num. de Bactérias')
    plt.title('Atividade 8\nNum. de Bactérias vs Tempo')
    plt.show()

video.release()
cv2.destroyAllWindows()
