import socket
import requests
import colorama

def sub():

    colorama.init(autoreset=True)
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT +  f"                                            🌕                 FᴜZZɪɴɢ---➸    ʙʏ ᴍZɢ                🐀   " )
    print('                                                              »»————---　★　---————-««                   \n')

    with open('.venv/word.txt', 'a+') as arquivo:
        print(" Digite o dominio que voce deseja scanear ")
        print("< exemplo: (https/http)://(target).com >\n")
        alvo = (input("Target: "))
        arquivo.seek(0)
        palavras = arquivo.readlines()
        alvo = alvo.rstrip("/")
        ip = alvo
        ip = ip.replace('https://', '')
        ip = ip.replace('http://', '')

        try:
            print(f"Target: {alvo} - {socket.gethostbyname(ip)}\n")
            for words in palavras:
                words = words.replace('\n', '')
                final = alvo + "/" + words
                resposta = requests.get(final)

                if resposta.status_code >= 200 and resposta.status_code <= 299:
                    print(f"{final} - {resposta.status_code} ")
                elif resposta.status_code != 200:
                    print(f"{final} - {resposta.status_code} ")

        except:
            print(f" O dominio inserido é invalido ou não conseguimos estabelecer uma conexão!")
            exit()

if __name__ == "__main__":
    sub()
