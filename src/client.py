import ctypes
import socket
import math
import time
from communications import Datagram, TypeOfDatagram, DatagramDeserialized


FRAGMENT_SIZE = 40000

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def upload(self, document_name):
        # Dirección y puerto del servidor
        server_address = ('localhost', 1234)

        with open(document_name, 'rb') as file:
            file_contents = file.read()

        # # Enviar mensaje de upload a Servidor y espera ACK
        # self.socket.send(Datagram.create_upload_header(document_name, len(file_contents)))
        # self.socket.recv(len(Datagram)) # ACK

        # Cantidad de fragmentos
        fragment_count = math.ceil(len(file_contents) / FRAGMENT_SIZE) 
        datagrams = []

        # Generamos los datagramas a enviar
        for i in range(fragment_count):
            start = i * FRAGMENT_SIZE
            end = min(start + FRAGMENT_SIZE, len(file_contents))
            fragment = file_contents[start:end]
            datagram = Datagram.create_content(packet_number=i, total_packet_count=fragment_count,
                                               packet_size=len(fragment), content=fragment)

            datagrams.append(datagram)
        
        # Timeout muy grande y tomamos medida de este ack 
        
        # enviar a server primera comunicacion de va archivo con x tamaño
        header = Datagram.create_upload_header(document_name, len(file_contents), fragment_count)
        sendTime = time.time()
        baids = header.get_datagram_bytes()
        self.socket.sendto(header.get_datagram_bytes(), server_address)  # Send the header to the server
        
        # esperar ack
        ack = self.socket.recv(40117)  # Wait to  an ACK from the server
        recvTime = time.time()
        ack_deserilized = DatagramDeserialized(ack)
        print(f"ACK recibido: {ack_deserilized.packet_number}")


        if ack_deserilized.total_packet_count != TypeOfDatagram.ACK.value:
            print("Error en la comunicacion")
            return
        
        firstTimeoutMeasure = recvTime - sendTime
        
        aproximateTimeout = firstTimeoutMeasure * 1.5
        # Timeout pasa a ser esta medida x 1,5 (flucutacion)
        
        # Stop and wait
        for i in datagrams:
            # enviar datagrama i
            self.socket.sendto(bytes(i), server_address)
            
            self.socket.settimeout(aproximateTimeout)
            try:
                ack = self.socket.recv(ctypes.sizeof(Datagram))
            except socket.timeout:
                print("Tiempo de espera excedido, no se recibió ACK.")

        
        # TODO: MANEJO DE ERRORES Y TIMEOUTS
        # TODO: Como definir el timeout? -> 1.5 * RTT (1.5 puede variar)         
        
#        
#    def download(self, document_name):
#        Enviar al servidor solicitud de descarga como un header
#            # TODO Implementar mensaje de solicitud de descarga
#        Esperar ACK del servidor
#            # TODO Implementar ACK del servidor por si o por no (que traiga -1 de numero?)
#        
#        
#        for i in cantidad:
#            esperar datagrama i
#            enviar ack
#               # ! Reeler enunciado si es stop-and-wait o todo de un saque con hilos
#        
#        llega todo reconstruir archivo
#        guardar archivo en disco (?)
    
   
    def send(self, message):
        self.socket.sendto(message.encode('utf-8'), (self.host, self.port))
        data, address = self.socket.recvfrom(1024)
        print(f"Received data from {address}: {data.decode()}")

    def close(self):
        self.socket.close()