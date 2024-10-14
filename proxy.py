import socket
import requests

cache = {}

def iniciar_servidor_proxy(HOST, PORT, origin_url):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Servidor proxy escuchando en {HOST}:{PORT}")
        while True:
            cliente, direccion = server.accept()
            print(f'Conexión establecida desde {direccion}')
            manejar_solicitud(cliente,origin_url)

def manejar_solicitud(cliente, url_origin):
    solicitud = cliente.recv(1024).decode()
    solicitud_cliente = solicitud.split('\n')[0]  # Primera línea: GET /posts/1 HTTP/1.1
    metodo, ruta, _ = solicitud_cliente.split(' ')  # Extraer método, ruta y protocolo

    url = f'{url_origin}{ruta}'

    if (metodo, url) in cache:
        print(f'solicitud {metodo} {url} está en la caché, procediendo a responder...')
        respuesta = cache[(metodo, url)]
        respuesta.headers['X-cache'] = 'HIT'
        enviar = (f'Respuesta enviada desde la caché \ {respuesta.content}').encode()
        cliente.sendall(enviar)
    else:
        print(f'solicitud {metodo} {url} no está en la caché, haciendo la solicitud real...')
        respuesta_real = requests.get(url)
        respuesta_real.headers['X-cache'] = 'MISS'
        
        # Guardar la respuesta en la caché
        cache[(metodo, url)] = respuesta_real
        respuesta_servidor = respuesta_real.content
        enviar = (f'Respuesta enviada desde el servidor real: \ {respuesta_servidor}').encode()
        cliente.sendall(enviar) # Enviar la respuesta al cliente
    cliente.close()  # Cerrar la conexión


