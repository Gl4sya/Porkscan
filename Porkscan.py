#Imports
import socket
import os
import sys
from time import sleep
from random import choice
from colorama import Fore, Style
from os import name, system

#cores
fVermelho = "\033[1;31m"
tVerde = "\033[1;32m"
tAzul = "\033[1;34m"
tMagenta = "\033[1;35m"
tCianoClaro = "\033[1;96m"
tAzulClaro = "\033[1;104m"
tVerdeClaro	= "\033[1;92m"
tBranco = "\033[1;97m"
fBranco = "\033[1;107m"

#Inicio
os.system(['clear', 'cls'][os.name == 'nt'])
sleep(1)
print(tCianoClaro + """
         _nnnn_      ...............,
        dGGGGMMb     | Portscan     |
       @p~qp~~qMb    |   by: Gl4sya |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL          
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' """)

#Ip
ip = input(tAzul + "Ip/Dominio do alvo:\n")
os.system(['clear', 'cls'][os.name == 'nt'])
sleep(2)
print(tVerdeClaro + """
   ._________________.
   |.---------------.|
   ||      ,_,      ||     
   ||     (o,o)     ||   
   ||     {`"'}     || 
   ||     -"-"-     ||
   ||_______________||
   /.-.-.-.-.-.-.-.-./
  /.-.-.-.-.-.-.-.-.-./
 /.-.-.-.-.-.-.-.-.-.-./
/______/__________\___o_/
\_______________________/

""")

#Portscan
for porta in range(1,65535):
    #Serviços
    http = 80 or 8081 or 8080 or 8082 or 8000
    ftp = 21 or 2121
    ssh = 22 or 2222
    
    #Ports
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        response = s.connect_ex((ip,porta))
        if response == 0:    
            print(tVerde + f"Porta {porta} Open!")
            if porta == http:
                print(tBranco + f"{porta}     HTTP")
            if porta == ssh:
                print(tBranco + f"{porta}     SSH")
    except:
        print("Não há portas abertas!")
        exit()

#Logo        
colors = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]

def logo_printer():
    logo = r""" 
 ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄      ▄▀▀▀▀▄    ▄▀▀▀▀▄   ▄▀▀█▄▄   ▄▀▀▀▀▄ 
█    █  ▐ █  █   ▄▀ ▐  ▄▀   ▐     █         █      █ █ ▄▀   █ █ █   ▐ 
▐   █     ▐  █▄▄▄█    █▄▄▄▄▄      █    ▀▄▄  █      █ ▐ █    █    ▀▄   
   █         █   █    █    ▌      █     █ █ ▀▄    ▄▀   █    █ ▀▄   █  
 ▄▀         ▄▀  ▄▀   ▄▀▄▄▄▄       ▐▀▄▄▄▄▀ ▐   ▀▀▀▀    ▄▀▄▄▄▄▀  █▀▀▀   
█          █   █     █    ▐       ▐                  █     ▐   ▐                    
							  ___             ,_,              ___
							 (o,o)           (o,o)         ,,,(o,o),,,
							 {`"'}           {`"'}          ';:`-':;'
							 -"-"-           -"-"-            -"-"-
    """
    _logo_enumer = 0
    for char in logo:
        sys.stdout.write(f"{choice(colors)}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        _logo_enumer +=1
        sleep(0.005)

logo_printer()

#Github
print(tAzul + "Gl4sya's Github: https://github.com/Gl4sya/")
print(tVerde + "March0s1a's Github: https://github.com/march0s1as/")
print(tMagenta + "Vapula's Github: https://github.com/Mussoxd")