# ufu-atividade-1-modulo3

1ª atividade avaliativa do Módulo 3 (Segurança Web) — Cibersegurança UFU.

Aplicações cliente-servidor em Python usando sockets, uma com **TCP** e outra com **UDP**.

## O que cada aplicação faz

**TCP** — o cliente envia um texto e o servidor devolve o texto invertido, informando se ele é um palíndromo.

```
coloque qualquer coisa: arara
do servidor:
------------------------------
Invertido: arara
É palíndromo!
------------------------------
```

**UDP** — o cliente envia uma frase e o servidor devolve a contagem de cada vogal (considerando acentos e letras maiúsculas) e o total.

```
digite qualquer sentença: carro
a: 1
e: 0
i: 0
o: 1
u: 0
Total de vogais: 2
```

## Estrutura

```
.
├── TCP/
│   ├── TCPServer.py
│   ├── TCPClient.py
│   └── inverter_texto.py
├── UDP/
│   ├── UDPServer.py
│   ├── UDPClient.py
│   └── contagem_vogais.py
└── README.md
```

## Requisitos

- Python 3

Os dois servidores usam a porta **1219** (uma em TCP e outra em UDP, por isso não há conflito).

## Configurando o endereço do servidor

Nos clientes, ajuste a variável `serverName` com o IP da máquina onde o servidor está rodando:

```python
serverName = ""   # IP do servidor
serverPort = 1219
```

Para testar tudo na mesma máquina, use `"localhost"`.

## Executando

Em um terminal, inicie o servidor:

```bash
cd TCP
python3 TCPServer.py
```

Em outro terminal, rode o cliente:

```bash
cd TCP
python3 TCPClient.py
```

Para a aplicação UDP, o processo é o mesmo, dentro da pasta `UDP/` com `UDPServer.py` e `UDPClient.py`.

## Autor

Arthur Rodrigues Carvalho — [ArthurRod-Ciber](https://github.com/ArthurRod-Ciber)
