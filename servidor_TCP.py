import socket
from datetime import datetime
import os
import platform

host = "localhost"
port = 9999

#crear objeto server, AF_INET = IpV4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host,port))

server.listen(1)

print("Servidor listo")

active, addr = server.accept()

#creamos el bucle infinito para conexión

while True:
    #utilizamos la primitiva recv para recibir la información del cliente
    recibido = active.recv(1024).decode(encoding = "ascii", errors = "ignore")
    print("Cliente: ", recibido)


    if recibido == "date":
        enviar = str(datetime.now())
        active.send(enviar.encode(encoding = "ascii", errors = "ignore"))

    if recibido == "os":
        enviar = str(os.name) + " " + str(platform.system()) + " " + str(platform.release()) + " " + str(platform.processor())
        active.send(enviar.encode(encoding = "ascii", errors = "ignore"))

    if recibido == "ls":
        enviar = str(os.listdir())
        active.send(enviar.encode(encoding = "ascii", errors = "ignore"))


#cerramos la conexión
active.close()