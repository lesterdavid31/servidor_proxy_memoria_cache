import socket

HOST = "127.0.0.1"  # Dirección del proxy
PORT = 8080         # Puerto del proxy

# Formato de solicitud GET para obtener el recurso desde jsonplaceholder
request = (
    "GET /posts/1 HTTP/1.1\r\n"
    "Host: jsonplaceholder.typicode.com\r\n"
    "Connection: close\r\n"
    "\r\n"
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Conéctate al servidor proxy
    s.sendall(request.encode())  # Envía la solicitud formateada
    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data    

print(response.decode()) 
# print(response.content) # Imprime la respuesta
