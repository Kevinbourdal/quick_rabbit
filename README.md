# Quick RabbitMQ Python Library

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This is a Python library designed to simplify communication with RabbitMQ, offering an easier and more secure way to consume and produce messages without the need to deeply study the official RabbitMQ documentation.

## Features

- Simple sending and receiving of messages with RabbitMQ.
- Queue and connection management.
- Support for multiple message types and serialization.
- High flexibility to define custom consumers and producers.
- Scalable for large volumes of messages.
- Easy integration with existing applications.

## Installation

- First, make sure you have Python 3.8 or higher installed. Then, you can install the library using pip:
```bash
pip install quick_rabbit
```


## Contributions

Contributions are welcome. If you have an idea, suggestion, or found a bug, please open an issue or a pull request.

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## A Simple Example Consumer

```py
import quick_rabbit as qr
import json


class your_objt(qr.RabbitMqClient):
    # It's important redefinne this method
    def callback(self, ch, method, properties, body):
        super().callback(ch, method, properties, body)
        if self.queue == "your_queue":
            self.your_func()
    
    def recive(self, q, list_queue):
        self._recive(q, list_queue)
        
    def your_func(self):
        ## logic here
        pass


def main():
    qr.consumer("RABBITMQ_HOSTNAME",
                int("RABBITMQ_PORT"),
                "RABBITMQ_USER",
                "RABBITMQ_PASS",
                int("RABBIT_TIMER"),
                "your queue",
                your_objt)

```

## A Simple Example Producer

```py
from quick_rabbit import get_data


def main(cmd, queue, data=None):
    return get_data("RABBITMQ_HOSTNAME",
                    int("RABBITMQ_PORT"),
                    "RABBITMQ_USER",
                    "RABBITMQ_PASS",
                    int("RABBIT_TIMER"),
                    cmd, queue, data)


res = main("get-cmd", "queue", {"key": "value"})



```