from random import choice
from sys import exit

tentativas: int = 6
palavra_original: str

try:
    with open("words.txt", "r") as palavras:
        lista_palavras: list[str] = []
        for letra in palavras:
            lista_palavras.append(letra.strip().upper())
        
        if len(lista_palavras) == 0:
            print("Nenhuma palavra encontrada! Jogo finalizado.")
            exit()
        
        palavra_original = choice(lista_palavras)
except FileNotFoundError:
    print("Arquivo de palavras não encontrado!")
    exit()
    
def palavra(lista: set[str]):
    lista_final: list[str] = []
    for letter in palavra_original:
        if letter in lista:
            lista_final.append(letter)
        else:
            lista_final.append("_")
    final_word: str = " ".join(lista_final)
    return final_word

if __name__ == "__main__":
    lista_letras: set[str] = set()

    print("Bem-vindo ao Jogo da Forca!\n")
    # print("")
    print(f"Palavra: {palavra(lista_letras)}\n")
    # print("")
    print(f"Tentativas restantes: {tentativas}")
    print("Letras tentadas: Nenhuma\n")
    # print("")
    
    while tentativas:
        letra = input("Digite uma letra: ").strip().upper()
        if not letra.isalpha() or len(letra) > 1:
            print("Letra inválida! Tente outra vez.")
            continue
        lista_letras.add(letra)

        if letra not in palavra_original:
            tentativas -= 1

        if letra in palavra_original:
            print(f"Boa! A letra '{letra}' está na palavra.\n")
        else:
            print(f"A letra '{letra.upper()}' não está na palavra.\n")
        
        print(f"Palavra: {palavra(lista_letras)}\n")
        
        letras_usadas: str = ", ".join(lista_letras)
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras tentadas: {letras_usadas}\n")

        if "_" not in palavra(lista_letras):
            print(f"Parabéns! Você acertou a palavra: {palavra_original}")
            break
        elif tentativas == 0:
            print(f"Fim de jogo! A palavra era: {palavra_original}")
            break
