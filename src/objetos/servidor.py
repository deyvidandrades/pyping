from socket import socket, AF_INET, SOCK_DGRAM


class Servidor:
    def __init__(self, porta: int) -> None:
        """ Inicializando o Servidor
        :param porta: A porta na qual o servidor vai se comunicar com o cliente
        """
        super().__init__()

        self.__porta = porta
        self.__socket = socket(AF_INET, SOCK_DGRAM)

    def iniciar(self):
        """
        Vinculamos o socket no endereço local na porta recebida. O servidor aguarda conexões até o usuário
        interromper o programa. Quando a conexão é realizada, o endereço é impresso, em seguida
        a mensagem é enviada de volta ao cliente (o PING).

        :return: None
        :except KeyboardInterrupt: Caso o servidor seja interrompido pelo usuario uma mensagem é apresentada e o
        socket é fechado.
        """

        self.__socket.bind(('', self.__porta))
        print('[i] Servidor iniciado. Aguardando conexões.')

        try:
            while True:
                mensagem, endereco = self.__socket.recvfrom(2048)

                print(f"[+] data=[endereco:{endereco[0]}]")

                self.__socket.sendto(mensagem, endereco)

        except KeyboardInterrupt:
            self.__socket.close()
            print('[i] Servidor desativado.')
