import os
import art
os.system('clear')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar(direct, text_input, shift_number):
    cypher_text = ""
    if direct == "decode":
        shift_number *= -1
    for char in text_input:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            cypher_text += alphabet[new_position]
        else:
            cypher_text += char
    print(f"A mensagem {direct}d é: {cypher_text}")


restart = True
while restart:
    os.system('clear')
    print(art.logo)
    direction = input("Digite 'encode' para criptografar ou 'decode'\
 para descriptografar:\n")
    text = input("Escreva sua mensagem:\n").lower()
    shift = int(input("Quantas vezes deseja embaralhar:\n"))
    shift = shift % 26
    caesar(text_input=text, shift_number=shift, direct=direction)

    result = input("Deseja utlizar mais uma vez? 'y' ou 'n'.\n")
    if result == "n":
        restart = False
        os.system('clear')
        print("Até a próxima!")
