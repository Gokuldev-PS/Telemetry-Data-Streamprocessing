import time
import random
import json
from confluent_kafka import Producer
# Configuration for Confluent Cloud
BOOTSTRAP_SERVERS = ''  # Replace with your Confluent Cloud bootstrap servers
SECURITY_PROTOCOL = 'SASL_SSL'
SASL_MECHANISM = 'PLAIN'
SASL_USERNAME = ''  # Replace with your Confluent Cloud API key
SASL_PASSWORD = ''  # Replace with your Confluent Cloud API secret
TOPIC_NAME = 'telemetry_events'  
def generate_mock_data():
    user_ids = ['user1', 'user2', 'user3', 'user4', 'user5','user6']
    event_types = ['kill', 'death']
    current_time = int(time.time())  # Get the current UNIX timestamp
    data= {
        'player_id': random.choice(user_ids),
        'event_type': random.choice(event_types),
        'timestamp': current_time
    }
    return json.dumps(data)
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
def main():
    conf = {
        'bootstrap.servers': BOOTSTRAP_SERVERS,
        'security.protocol': SECURITY_PROTOCOL,
        'sasl.mechanisms': SASL_MECHANISM,
        'sasl.username': SASL_USERNAME,
        'sasl.password': SASL_PASSWORD,
    }
    producer = Producer(conf)
    try:
        while True:
            mock_data = generate_mock_data()
          
            producer.produce(TOPIC_NAME, mock_data.encode('utf-8'), callback=delivery_report)
            producer.flush()
            time.sleep(30)  # Send a new message every 30 second
    except KeyboardInterrupt:
        print("User interrupted, stopping data generation.")
    finally:
        producer.flush()
if __name__ == "__main__":
    main()
