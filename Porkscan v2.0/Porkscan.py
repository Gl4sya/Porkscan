from Lib.Interface import *


cabeçalho(tBranco + """
  _ _ _ ____ _    ____ ____ _  _ ____ 
  | | | |___ |    |    |  | |\/| |___ 
  |_|_| |___ |___ |___ |__| |  | |___ 
        
                ➥ Portscan by Gl4sya                                            
     """)
print(tBranco + "Enter the IP / Domain below")
print(linha())

ip = input("► ")
    
for porta in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        response = s.connect_ex((ip,porta))
        if response == 0: 
            print(linha())   
            print(tBranco+ f"➥  Port {porta} Open!")
    except:
        print(fVermelho + "Host not found")
        exit(1)