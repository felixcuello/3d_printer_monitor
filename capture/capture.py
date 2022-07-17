import cv2
import time
import sys
import uuid

if len(sys.argv) < 2:
    print("""

    Uso:

    ./capture.py <frame_interval> [frame_name]


    frame_interval -> El espacio en milisegundos para tomar imágenes
    frame_name     -> El nombre del frame (si no se entrega ninguno se asigna un UUID)
                      (La imagen se envia al servicio con este nombre)

""")
    exit

frame_interval = int(sys.argv[1])
frame_name = uuid.uuid4()
if len(sys.argv) >= 3:
    frame_name = sys.argv[2]

print("[INFO] Frame Interval:", sys.argv[1])
print("[INFO] Frame Name: {}".format(frame_name))
print("[INFO] >>>>>>> Presione SPACE para comenzar a monitorear <<<<<<<")

cam = cv2.VideoCapture(0)
cv2.namedWindow("3D Printer Monitor")

contador_imagenes = 0
capturing = False

while True:
    ret, frame = cam.read()
    if not ret:
        print("[ERROR] Al grabar un frame")

    cv2.imshow("3D Printer Monitor", frame)

    k = cv2.waitKey(frame_interval) # https://stackoverflow.com/questions/46671348/make-a-pause-between-images-display-in-opencv

    # SPACE pressed
    if k % 256 == 32:
        print("Iniciando capturas (Presionar ESC para salir)...")
        capturing = True
    elif k%256 == 27:
        # ESC -> apretado
        print("ESC -> SALIENDO....")
        break

    if capturing == True:
        img_name = "{}_{img:010d}.png".format(frame_name, img=contador_imagenes)
        cv2.imwrite(img_name, frame)
        print("{} imagen grabada".format(img_name))
        contador_imagenes += 1

cam.release()

cv2.destroyAllWindows()
