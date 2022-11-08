import socket

host = "localhost"
port = 9999

#crear objeto socket1
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#recibe una tupa del host y del puerto
socket1.connect((host,port))
print("Inicializando cliente")

#creamos el bucle infinito para conexión
while True:

    #creamos variable enviar y espera al cliente
    enviar = input("Cliente: ")
    
    #utilizamos la primitiva send para enviar la información
    socket1.send(enviar.encode(encoding = "ascii", errors = "ignore"))

    #utilizamos la primitiva recv para recibir la información del cliente
    recibido = socket1.recv(1024)
    print("Servidor: ",recibido.decode(encoding = "ascii", errors = "ignore"))

#cerramos la conexión
socket1.close()