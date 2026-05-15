# Enunciado --> Criação de programas que simulem situações reais (exemplo: 
#               sistema de semáforo, controle de estoque, sorteios).

import time
from colorama import Fore, Style, init
init()

print(Fore.BLUE + "\n-- SISTEMA DE SEMÁFORO (CRUZAMENTO) --\n" + Style.RESET_ALL)

while True:
    # Def serve apenas para organizar a váriavel
    def contagem(segundos, msg_a, msg_b):
        for i in range(segundos, -1, -1):
            print(f"\r{msg_a} | {msg_b} | [{i}s]", end=" ") 
            # Ao colocar para exibir a mensagem A e B, ao lado do i, basicamente faz exibir 
            #    as cores do semáforo uma ao lado da outra, já o i é para mostrar a contagem 
            #    regressiva no terminal, também ao lado das cores. O end é para garantir que 
            #    nessa linha só será exibida a mensagem que eu quero
            
            time.sleep(1) # O comando time.sleep serve para criar um delay de 1 segundo na contagem 

    # Farol A - verde / Farol B - vermelho
    contagem(8, Fore.GREEN + "Farol A: 🟢" + Style.RESET_ALL, Fore.RED + "Farol B: 🔴" + Style.RESET_ALL)
    print()

    # Farol A - amarelo / Farol B - vermelho
    contagem(6, Fore.YELLOW + "Farol A: 🟡" + Style.RESET_ALL, Fore.RED + "Farol B: 🔴" + Style.RESET_ALL)
    print()

    # Farol A - vermelho / Farol B - verde
    contagem(8,Fore.RED + "Farol A: 🔴" + Style.RESET_ALL, Fore.GREEN + "Farol B: 🟢" + Style.RESET_ALL)
    print()

    # Farol A - vermelho / Farol B - amarelo
    contagem(6,Fore.RED + "Farol A: 🔴" + Style.RESET_ALL, Fore.YELLOW + "Farol B: 🟡" + Style.RESET_ALL)
    print()
    print("\n")
    