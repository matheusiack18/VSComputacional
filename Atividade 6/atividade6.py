import cv2

video = cv2.VideoCapture("video_carro.mp4") 
 
if (video.isOpened() == False):
        print("Error!")

else:
    while video.isOpened():
            ret, frame = video.read()
            frame = cv2.resize(frame, None, fx=0.3, fy=0.3)

            if ret == True:
                for i in range(int(frame.shape[0]*0.7),frame.shape[0]):
                    for j in range(frame.shape[1]):
                        blue, green, red = frame[i, j]
                        if (blue > 165) and (green > 168) and (red > 170):
                                frame[i, j] = (255, 0, 0)
                        elif (blue < 130) and (green > 40) and (red > 155):
                                frame[i, j] = (0, 0, 255)

                cv2.imshow("frame", frame)

                if cv2.waitKey(25) & 0xFF == ord("q"):
                        break

    video.release()
    cv2.destroyAllWindows()     

# Professor eu nao to conseguindo mandar o video por ser um pouco grande ai eu vou estar mandando para o email do senhor        