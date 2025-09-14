cont=0

while cont <= 8:
    print(f"o contandor está na posição {cont}ª")
    cont+=1


while True:
    dig=int(input("digite um num par: "))
    if dig%2 == 0:
        print("vc digitou um num par, thx")
    else:
        print("você digitou um num impar, seu burro")