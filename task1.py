from queue import Queue
from time import sleep
import random

queue = Queue()


def generate_request():
    if random.random() >= 0.5:
        queue.put(f"заявка {random.randint(1,100000000)}")


def process_request():
    if not queue.empty():
        print(f"Oпрацьована {queue.get()}")
    else:
        print("queue is empty")


if __name__ == "__main__":
    while True:
        generate_request()
        sleep(0.1)
        process_request()
        sleep(0.3)
