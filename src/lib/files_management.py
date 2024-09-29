import math
import os
from lib.communications import Datagram, FRAGMENT_SIZE

def get_count_of_datagrams(file_name):
    try:
        with open(file_name, "rb") as file:
            file_contents = file.read()
    except:
        raise "Archivo no encontrado"

    return math.ceil(len(file_contents) / FRAGMENT_SIZE)


def get_file_size(file_name):
    return os.path.getsize(file_name)

def get_file_content(file_name):
    try:
        with open(file_name, "rb") as file:
            file_contents = file.read()
        return file_contents
    except Exception as e:
        return e

def create_new_file(bytes_flow, file_name):
    file = b''.join(bytes_flow)

    os.makedirs(os.path.dirname('files/' + file_name), exist_ok=True)

    with open('files/' + file_name, 'wb') as f:
        f.write(file)

def get_datagramas(file_contents):
    # Cantidad de fragmentos
    total_datagrams = math.ceil(len(file_contents) / FRAGMENT_SIZE)
    datagrams = []

    # Generamos los datagramas a enviar
    for i in range(total_datagrams):
        start = i * FRAGMENT_SIZE
        end = min(start + FRAGMENT_SIZE, len(file_contents))
        fragment = file_contents[start:end]
        datagram = Datagram.create_content(
            datagram_number=i+1,
            total_datagrams=total_datagrams,
            file_name="",
            datagram_size=end - start,
            content=fragment,
        )

        datagrams.append(datagram)
    return datagrams