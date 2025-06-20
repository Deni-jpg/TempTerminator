import tempfile
import shutil
import os
import textwrap
import time
from colorama import init, Fore, Style
from pathlib import Path

deletado = 0
n_deletado = 0

# Pega a pasta temp do sistema
temp_dir = Path(tempfile.gettempdir())

#Excluir arquivos de %TEMP%
def ex_temp():
    global deletado
    global n_deletado

    # 1) Apaga TUDO dentro de temp_dir
    for item in temp_dir.iterdir():
        try:
            if item.is_dir():
                shutil.rmtree(item)   # remove diretório e subtudo
            else:
                item.unlink()         # remove arquivo
            print(f"🗑️  Deletado: {item}")
            deletado += 1

        except Exception as e:
            print(f"⚠️  Erro ao deletar {item}: {e}")
            n_deletado += 1
    
    print(Fore.GREEN + f"\n{deletado} Arquivos deletados com sucesso, "+ Fore.RED + f"{n_deletado} falharam ao ser excluídos.\n")
    deletado = 0
    n_deletado = 0
    continuar()

def continuar():

    print(Fore.CYAN + "1) Voltar ao menu")
    print(Fore.CYAN + "2) Sair\n")

    continua = int(input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL))

    if continua == 1: 
        menu() 
    else:
        for i in range(3):
            s = Fore.RED + "Saindo" + "." * (i + 1)
            time.sleep(1)
            print(s.ljust(10), end="\r", flush=True)
        time.sleep(1)  
        exit()


# Menu
def menu():
    os.system("cls" if os.name == "nt" else "clear")
    init(autoreset=True)

    ascii_art = r"""
      _______                _______                  _             _             
     |__   __|              |__   __|                (_)           | |            
        | | ___ _ __ ___   _ __| | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
        | |/ _ \ '_ ` _ \| '_ \| |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
        | |  __/ | | | | | |_) | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
        |_|\___|_| |_| |_| .__/|_|\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_|   
                         | |                                                      
                         |_|                                                      
    """
    # Remove indentação do bloco
    art = textwrap.dedent(ascii_art).strip("\n")

    # Cores em loop (gradient simples)
    colors = [Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.GREEN]
    for idx, line in enumerate(art.splitlines()):
        color = colors[idx % len(colors)]
        print(color + line)

    # Menu
    print(Style.RESET_ALL)  # só pra garantir
        # só printa as opções
    print(Fore.CYAN + "1) Limpar arquivos temporários")
    print(Fore.CYAN + "2) Sair\n")

    # agora pede a escolha, passando UMA string como prompt
    pergunta = int(input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL))
    
    if pergunta == 1: 
        ex_temp()

menu()