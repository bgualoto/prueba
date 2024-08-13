# producer.py
import pika

# Conectar a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Crear una cola llamada 'hello'
channel.queue_declare(queue="hello")

# Enviar un mensaje a la cola
channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")

# Cerrar la conexión
connection.close()
