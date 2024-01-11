from queue import Queue
from time import sleep
import random
import uuid

queue = Queue()


def generate_request():
    if random.random() >= 0.5:
        queue.put(f"заявка {uuid.uuid4()}")


def process_request():
    if not queue.empty():
        print(f"Oпрацьована {queue.get()}")
    else:
        print("queue is empty")


if __name__ == "__main__":
    while True:
        try:
            generate_request()
            sleep(0.1)
            process_request()
            sleep(0.3)
        except KeyboardInterrupt:
            queue.empty()
            print("Завершую роботу")
            break
