
import time
import random

stock_zapatos = 120
stock_poleras = 150
zapatos_proveedor = 150
poleras_proveedor = 150

cantidad_compra = 0
while cantidad_compra <= 60:
    time.sleep(3)
    n1 = random.randrange(1,11)
    n2 = random.randrange(1,11)
    stock_zapatos -= n1 
    stock_poleras -= n2
    cantidad_compra += 1
    print('-----------------------------------')
    print(f'Operacion numero {cantidad_compra}')
    print('-----------------------------------')
    print(f'Del producto zapatos quedan: {stock_zapatos}')
    print(f'Del producto poleras quedan: {stock_poleras}')
    print('-----------------------------------')

    if cantidad_compra == 10:
        print('-----------------------------------')
        print(f'Del producto zapatos quedan: {stock_zapatos}')
        print('-----------------------------------')
    if cantidad_compra == 10:
        print('-----------------------------------')
        print(f'Del producto poleras quedan: {stock_poleras}')
        print('-----------------------------------')
    if stock_zapatos < 100 and zapatos_proveedor > 0:
        stock_zapatos += 50
        zapatos_proveedor -= 50
        print('-----------------------------------')
        print(f'Se han agregado 50 unidades a producto zapato {stock_zapatos}')
        print(f'Se han restado 50 unidades a proveedor de zapatos quedan {zapatos_proveedor}')
        print('-----------------------------------')
        if zapatos_proveedor == 0:
            print('-----------------------------------')
            print('Ya no quedan unidades de zapatos por parte del proveedor')
            print('-----------------------------------')
    if stock_poleras < 100 and poleras_proveedor > 0:
        stock_poleras += 50    
        poleras_proveedor -= 50
        print('-----------------------------------')
        print(f'Se han agregado 50 unidades a producto poleras {stock_poleras}')
        print(f'Se han restado 50 unidades a producto poleras quedan {poleras_proveedor}')
        print('-----------------------------------')
        if poleras_proveedor == 0:
            print('-----------------------------------')
            print('Ya no quedan unidades de poleras por parte del proveedor')
            print('-----------------------------------')
        


    

  




    







        
    
    