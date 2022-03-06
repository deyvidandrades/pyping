import argparse

from src.objetos.cliente import Cliente
from src.objetos.servidor import Servidor


def main(args):
    if args.server:
        Servidor(25050).iniciar()
    else:
        Cliente(args.endereco, args.c, 25050).ping()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Implementação do comando PING")

    parser.add_argument('endereco', nargs='?', action='store', type=str, help='DNS ou endereço de IP')
    parser.add_argument('-c', action='store', type=int, default=20, help='para depois de <contador> respostas.')
    parser.add_argument('-s', '--server', action='store_true', help='inicia em modo servidor.')
    parser.add_argument("-v", "--versao", help="Versao", action="version", version='%(prog)s 1.0')

    main(parser.parse_args())
