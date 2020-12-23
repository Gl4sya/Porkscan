import socket
import sys

#Cores
tPreto = "\033[1;30m"
fPreto = "\033[1;40m"

fVermelho = "\033[1;31m"
tVermelho = "\033[1;41m"

tVerde = "\033[1;32m"
fVerde = "\033[1;42m"

tAmarelo = "\033[1;33m"
fAmarelo = "\033[1;43m"

tAzul = "\033[1;34m"
fAzul = "\033[1;44m"

tMagenta = "\033[1;35m"
fMagenta = "\033[1;45m"

tCiano = "\033[1;36m"
fCiano = "\033[1;46m"

tCinzaClaro = "\033[1;37m"
fCinzaClaro = "\033[1;47m"

tCinzaEscuro = "\033[1;90m"
fCinzaEscuro = "\033[1;100m"

tVermelhoClaro = "\033[1;91m"
fVermelhoClaro = "\033[1;101m"

tVerdeClaro	= "\033[1;92m"
fVerdeClaro = "\033[1;102m"

tAmareloClaro = "\033[1;93m"
fAmareloClaro = "\033[1;103m"

tAzulClaro = "\033[1;94m"
tAzulClaro = "\033[1;104m"

tMagentaClaro = "\033[1;95m"
fMagentaClaro = "\033[1;105m"

tCianoClaro = "\033[1;96m"
fCianoClaro = "\033[1;106m"

tBranco = "\033[1;97m"
fBranco = "\033[1;107m"

tNegrito	= "\033[;1m"
tInverte	= "\033[;7m"

tReset = "\033[0;0m"


def linha(tam = 42):
    return tCinzaEscuro + f'-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
