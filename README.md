# Jogo-da-Forca
Este é um simples (extremamente simples) [jogo da forca](https://pt.wikipedia.org/wiki/Jogo_da_forca) feito em Python. 
O jogo consiste em advinhar uma palavra cuja as letras são desconhecidas. Pode-se chutar até 6 letras erradas, com o jogo acabando se:
1. O jogador zera seus chutes
2. O jogador acera a palavra
Se o chute estiver correto, a letra escolhida será substituída nos locais apropriados, não diminuindo as tentativas restante do jogador. Do contrário, o número de tentativa simplesmente diminui.

---

## Diretórios:
jogo-da-forca <br />
├── README.md <br />
├── LICENSE <br />
├── assets <br />
│   ├── jogo_ganho.png <br />
│   ├── jogo_perdido.png <br />
│   ├── tela_inicial <br />
│   ├── tentativa_certa.png <br />
│   └── tentativa_falha.png <br />
├── main.cpp <br />
└── words.txt <br />

- ```README.md```: arquivo readme.
- ```LICENSE```: MIT license.
- ```assets```: pasta onde arquivos PNGs estão armazenados.
- ```main.cpp```: jogo da forca programa.
- ```words.txt```: arquivo de texto que armazena as palavras do jogo.

---

## Jogando o Jogo da Forca

No começo, nós temos uma palavra escolhida aleatoriamente na lista em ```words.txt```, com todas as suas letras ocultas. Nos é pedido para digitarmos uma letra:

![inicial](assets/tela_inicial.png)

---

Após digitarmos a letra, o programa nos dirá se a letra está ou não está na palavra. Caso esteja, será mostrado:

![certo](assets/tentativa_certa.png)

Do contrário:

![falho](assets/tentativa_falha.png)

---

Continuando o jogo, o jogador poderá, de maneira vitoriosa, acertar a palavra:

![ganho](assets/jogo_ganho.png)

Ou, infelizmente, perder o jogo:

![perda](assets/jogo_perdido.png)


---

## O que é necessário para jogar
- Para jogar o jogo da forca, é necessário que você tenha alguma versão de Python instalada no seu computador (Python 3.9 ou superior). Instale Python por aqui: https://www.python.org/downloads/
- É extremamente necessário ter o arquivo ```words.txt``` no mesmo script que o ```main.py```.
---

## Licence
This project is licensed under the MIT license. For more information, see the [License](LICENSE) file.
