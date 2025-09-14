def titulo():
    print('-'*30)

lar=float(input('digite a largura do terreno:'))
com=float(input('digite a comprimento do terreno:'))

def area():
    a= lar*com

titulo()
print(f'o valor do comprimento é {com}, o valor da largura é {lar}, a área total do terreno é ', area())