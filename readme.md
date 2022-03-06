# PYPING - Implementação do comando ping com sockets em python

#### [Projeto prático](https://github.com/deyvidandrades/pyping) desenvoldido na disciplina de Redes de computadores.

A proposta inicial é compreender como o ping funciona e como as estatísticas são calculadas e o que elas significam.

# Primeiros passos

Essas instruções farão com que você tenha uma cópia do projeto em execução na sua máquina local para fins de  
desenvolvimento e teste. Veja a implantação de notas sobre como implantar o projeto em um sistema ativo.

## Pré-requisitos

O que você precisa instalar para desenvolver e rodar o projeto:

* [Python3.x](https://www.python.org/downloads/) - Ambiente de desenvolvimento Python

## Baixe ou clone o repositório

```  
$ git clone https://github.com/deyvidandrades/pyping.git  
```  

## Rodando o PYPING:

```  
$ python __main__.py <endereco> [opcoes]  
```  

## Como usar o PYPING

### Executando o PYPING

Você pode simplesmente rodar o executável java localizado no diretório raiz do projeto.

```
$ python __main__.py [opcoes] <endereco> 
```

### Opções de linha de comando

```  
uso: __main__.py [-h] [-c C] [-s] [-v] [endereco]

Argumentos posicionais:
  endereco      DNS ou endereço de IP

opções:
  -h, --help    mostra a mensagem de ajuda.
  -c C          para depois de <contador> respostas.
  -s, --server  inicia em modo servidor.
```  

### Exemplos de uso
```
__main__.py 127.0.0.1
__main__.py 127.0.0.1 -c 10
__main__.py -s
```

Simule o atendimento numa fila de um 0800.

## Ferramentas e Bibliotecas

* [Socket (Python builtIn)](https://docs.python.org/3/library/socket.html) - A biblioteca da acesso ao usu de sockets em Python.

## Changelog
-

## Autores

* **Deyvid Andrade** - [github](https://github.com/deyvidandrades/)

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para obter detalhes.