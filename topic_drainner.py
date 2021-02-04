from kafka import KafkaConsumer
import os

class TopicDrainner:
    def start_drain(self):
        consumer = KafkaConsumer(TOPIC,
                                 group_id=CONSUMER_ID,
                                 bootstrap_servers=BROKER.strip(','))
        counter = 0
        print("Conectado com sucesso! Aguardando mensagens...")
        for message in consumer:
            counter += 1
            print ("%s:%d:%d: key=%s" % (message.topic, message.partition,
                                                  message.offset, message.key))
            print("Total de %d mensagens drenadas!" % (counter))

if __name__ == '__main__':
    NUMBER_OF_REQUESTS = os.getenv("NUMBER_OF_REQUESTS")
    INTERVAL = os.getenv("INTERVAL")
    BROKER = os.getenv("BROKER")
    TOPIC = os.getenv("TOPIC")
    DEFAULT_ENCODING = 'utf-8'
    while True:
        CONSUMER_ID=input("Insira o consumer-group para commitar os offsets: ")
        if CONSUMER_ID != None and CONSUMER_ID != '':
            break
    TopicDrainner().start_drain()