import pika

def publish_event(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='dna_analysis')
    channel.basic_publish(exchange='', routing_key='dna_analysis', body=message)
    connection.close()
