import random 


d= {"poleras":[8000, 200], "calzas": [10000,200],"buzos":[20000,200], "calcetines":[2000,200], "zapatillas":[50000, 200],
              "botines":[45000, 200], "gorro":[15000, 200],"sudaderas":[15000, 200],"polerones":[25000, 200],
              "chaquetas":[30000, 200],"short":[20000, 200],"calzas cortas":[20000, 200],"peto deportivo":[18000, 200],
                  "camiseta de futbol":[45000, 200],"parkas":[80000, 200]}

lista_precio=[]
prod = []
precio = []
stock = []
for producto, lista in d.items():
    #print(prod)
    prod.append(producto)
    precio.append(lista[0])
    stock.append(lista[1])

print('--------------------------------------------')
print('Bienvenido estos son los primeros 5 productos')
print('--------------------------------------------')


ran_prod = random.sample(prod,5)
condicion = input('Desea ver 5 productos:(S/N)')
while condicion == 'S':
    for producto_seleccionado in ran_prod:
        prod.remove(producto_seleccionado)
        print(producto_seleccionado)
        print(prod)
    condicion = input('Desea ver 5 productos:(S/N)')
    






