from socket import AF_INET, SOCK_DGRAM, socket

from chester.variables import SERVER, BUFFER_SIZE


def connect():
    client = socket(AF_INET, SOCK_DGRAM)
    client.connect(SERVER)
    return client


def interpret_data(d):
    pass


def main():
    client = connect()
    while True:
        data = client.recvfrom(BUFFER_SIZE)
        interpret_data(data)


if __name__ == '__main__':
    main()
