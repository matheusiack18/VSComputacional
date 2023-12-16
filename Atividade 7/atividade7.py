import cv2
import numpy as np

def processamento(frame):
    cont_area = 0

    min = np.array([5, 50, 30])  
    max = np.array([30, 250, 250]) 

    cor_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    marrom = cv2.inRange(cor_hsv, min, max)

    contorno, _ = cv2.findContours(marrom, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    areatotal = frame.shape[0] * frame.shape[1]
    for cont in contorno:
        cont_area += cv2.contourArea(cont)

    framecont = frame.copy()
    for cont in contorno:
        x, y, w, h = cv2.boundingRect(cont)
        cv2.rectangle(framecont, (x, y), (x + w, y + h), (100, 150, 0), 1)
    
    porcentagem = (cont_area / areatotal) * 100

    cv2.putText(framecont, f'Porcentagem de Desmatamento: {porcentagem:.2f}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, ), 2)

    return framecont

video = cv2.VideoCapture('./video.mp4')

if (video.isOpened() == False):
        print("Error!") 

else:
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

        framecolorido = processamento(frame)

        pretbranc = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pretbranc = cv2.cvtColor(pretbranc, cv2.COLOR_GRAY2BGR)

        stacked_frame = np.vstack((framecolorido, pretbranc))

        cv2.imshow('Resultado', stacked_frame)

        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

video.release()
cv2.destroyAllWindows()
