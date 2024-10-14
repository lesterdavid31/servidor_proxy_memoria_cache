# Proxy Server con Caché

Este proyecto es un **servidor proxy** que permite almacenar en **caché** las respuestas de solicitudes GET realizadas por el cliente. Utiliza **Python** para manejar las solicitudes, enviar respuestas al servidor de origen y retornar la respuesta al cliente desde la caché si ya existe. El proyecto permite realizar solicitudes HTTP y cachear las respuestas para mejorar la eficiencia en solicitudes repetidas.

## Características

- Proxy de almacenamiento en caché para solicitudes GET.
- Las solicitudes que ya se encuentran en la caché son respondidas con rapidez, evitando realizar nuevas solicitudes al servidor real.
- Indicación en la respuesta de si fue servida desde la **caché** o desde el **servidor real**.
- El servidor utiliza **sockets** para manejar las conexiones.
- **CLI** (interfaz de línea de comandos) creada con `Click` para facilitar el inicio del servidor.

## Tecnologías Utilizadas

- **Python 3.9+**
- **Sockets**
- **Requests** para realizar solicitudes HTTP al servidor de origen.
- **Click** para la creación de una interfaz CLI amigable.

## Requisitos

Para ejecutar el proyecto en tu máquina local, necesitarás tener instalados los siguientes paquetes de Python:

```bash
pip install click requests
```
## Ejecucuión del proyecto
  1. Clonar el repositorio en tu máquina local
     
```bash
git clone https://github.com/lesteryuman31/servidor_proxy_memoria_cache.git
cd proxy-server
```

  2. Ejecutar el servidor proxy, debes ejecutar el siguiente comando en la terminal:

```bash
python cli.py run --port 8080 --origin http://jsonplaceholder.typicode.com
```
  - --port: Especifica el puerto en el que se ejecutará el servidor proxy (por defecto: 8080).
  - --origin: La URL del servidor de origen al cual se enviarán las solicitudes.

  Ejemplo:
  ```bash
python cli.py run --port 8080 --origin http://jsonplaceholder.typicode.com
```

  3. Ejecutar el cliente, para enviar una solicitud desde el cliente hacia el servidor poxy, ejecuta el siguiente código en python

```bash
python client.py
```
  Este cliente enviará una solicitud GET a través del proxy para obtener el recurso posts/1 desde el servidor de origen (jsonplaceholder.typicode.com).

  4. Recibir Respuestas
     Dependiendo de si la respuesta está en la caché o no, recibirás una de las siguientes respuestas:
     - Respuesta desde la caché: Si la solicitud ya ha sido realizada anteriormente, la respuesta será obtenida desde la caché local.
     - Respuesta desde el servidor real: Si la solicitud no se encuentra en la caché, el proxy hará la solicitud al servidor de origen y cacheará la respuesta para futuras solicitudes.

## Ejemplo de Ejecución
  Iniciar el servidor proxy:
  ```bash
python cli.py run --port 8080 --origin http://jsonplaceholder.typicode.com
```

  Salida esperada de la terminal: 
  ```bash
Servidor proxy escuchando en 127.0.0.1:8080
Conexión establecida desde ('127.0.0.1', 12345)
solicitud GET http://jsonplaceholder.typicode.com/posts/1 no está en la caché, haciendo la solicitud real...
```

  Ejecutar el cliente:
```bash
python client.py
```

  Salida esperada en el cliente:
```bash
Respuesta enviada desde el servidor real: 
 {
   "userId": 1,
   "id": 1,
   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
   "body": "quia et suscipit..."
}

```

Consideraciones
  - Actualmente, la funcionalidad clear-cache está en desarrollo y no está disponible en esta versión del proyecto.
  - Las respuestas de las solicitudes GET son almacenadas en la caché para mejorar el rendimiento en solicitudes repetidas.
  - El servidor solo maneja solicitudes HTTP GET en este momento.

Contribuciónes 
Si deseas contribuir al proyecto, por favor, sigue los pasos:
  - Haz un fork del repositorio.
  - Crea una nueva rama para tus modificaciones: git checkout -b feature-nueva-funcionalidad.
  - Realiza tus cambios y haz commit: git commit -m "Agregar nueva funcionalidad".
  - Sube tus cambios: git push origin feature-nueva-funcionalidad.
  - Envía un pull request para que revise tus camvios.

https://roadmap.sh/projects/caching-server
