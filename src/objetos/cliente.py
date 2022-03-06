from socket import socket, AF_INET, SOCK_DGRAM, timeout
import ipaddress
import time


class Cliente:
    """
    Implementação do cliente
    """
    __timeout = .25
    __intervalo = 1
    __tempo_inicio = 0

    __pings_enviados = 0
    __pings_recebidos = 0
    __pings_media = 0

    __min_ping = 999999
    __max_ping = 0

    def __init__(self, host: ipaddress, contador: int, porta: int = 5002) -> None:
        """
        :param host: endereço realizar o ping
        :param porta: porta de conexão do socket

        Vinculamos o socket no endereço local na porta. Definimos o timeout.
        """
        super().__init__()

        self.__host = host
        self.__porta = porta
        self.__num_pings = contador
        self.__mensagem = bytearray('PING-GCC125'.encode())

        self.__socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket.settimeout(self.__timeout)

    def ping(self):
        """

        :return: None
        """

        self.__tempo_inicio = time.time()

        for sequencia_udp in range(self.__num_pings):
            try:
                self.__socket.sendto(self.__mensagem, (self.__host, self.__porta))

                tempo_inicio = time.time()
                dados, servidor = self.__socket.recvfrom(2048)
                tempo_final = time.time()

                tempo_delta = (tempo_final - tempo_inicio) * 1000

                if tempo_delta < self.__min_ping:
                    self.__min_ping = tempo_delta

                if tempo_delta > self.__max_ping:
                    self.__max_ping = tempo_delta

                self.__pings_recebidos += 1

                self.__pings_media += tempo_delta

                jitter = tempo_delta - self.__min_ping

                print(
                    f'{len(dados)} bytes recebidos de {self.__host} udp_seq={sequencia_udp} tempo_resposta={round(tempo_delta, 1)} ms jitter={round(jitter, 2)} ms'
                )

                time.sleep(self.__intervalo)
            except timeout:
                print(f'udp_seq={sequencia_udp} timeout')
            except KeyboardInterrupt:
                self.__exibir_detalhes()

            self.__pings_enviados += 1

        self.__exibir_detalhes()

    def __exibir_detalhes(self):
        tempo_gasto = (time.time() - self.__tempo_inicio) * 1000

        print(f'--- estatisticas de ping udp para {self.__host} ---')
        print(
            f'{self.__pings_enviados} pacotes transmitidos, {self.__pings_recebidos} recebidos, {round((self.__pings_enviados - self.__pings_recebidos) / self.__pings_enviados * 100, 1)}% de pacotes perdidos, tempo {round(tempo_gasto, 1)} ms')

        print(
            f'rtt min/avg/max/mdev = {round(self.__min_ping, 3)}/{round(self.__pings_media / self.__pings_enviados, 3)}/{round(self.__max_ping, 3)}/{round(self.__max_ping - self.__min_ping, 3)}'
        )
