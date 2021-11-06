'''
Hoy simularemos un sistema financiero. 
Definiremos dos clases: Cliente y Banco
Cada Cliente tendrá asociado un nombre, un saldo y un identificador.

Los métodos de la clase Cliente consisten en: 
mostrar saldo del cliente, retirar dinero, abonar dinero y retornar el saldo.

Cada Banco debe tener un nombre, saldo_institucional y un identificador.
Para crear un banco, este debe contener al menos tres clientes.

Los Bancos deben tener un método para agregar o registrar nuevos clientes (por consola).
El saldo de cada cliente que se registra no puede exceder al 10% del saldo institucional.
Cada banco debe tener un método para mostrar la información de todos su clientes de forma ordenada y pausada.

'''
import uuid
from datetime import datetime
import time
class Cliente:
    def __init__(self, nombre, saldo=0):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.saldo = saldo
        self.historial_retiros = {}
        self.historial_abonos = {}

#mostrar saldo del cliente, retirar dinero, abonar dinero y retornar el saldo.
    def mostrar_saldo_cliente(self):
        print(f'El saldo de {self.nombre} es {self.saldo}')

    def retirar_dinero(self, monto_retiro):
        self.saldo = self.saldo - monto_retiro
        self.historial_retiros[datetime.today().strftime('%Y-%m-%d %H:%M:%S')] = (monto_retiro, self.saldo)
        #diccionario[nombre_clave] = valor
        
    def abonar_dinero(self, monto_abonado):
        self.saldo = self.saldo + monto_abonado
        self.historial_abonos[datetime.today().strftime('%Y-%m-%d %H:%M:%S')] = (monto_abonado, self.saldo)

    def retornar_saldo(self):
        return self.saldo
        
'''
Cada Banco debe tener un nombre, saldo_institucional y un identificador.
Para crear un banco, este debe contener al menos tres clientes.

Los Bancos deben tener un método para agregar o registrar nuevos clientes (por consola).
El saldo de cada cliente que se registra no puede exceder al 10% del saldo institucional.
Cada banco debe tener un método para mostrar la información de todos su clientes de forma ordenada y pausada.
'''
class Banco:
    def __init__(self, nombre, saldo_institucional, *clientes:Cliente):
        self.nombre = nombre
        self.saldo_institucional = saldo_institucional
        self.lista_clientes = list(clientes)
        if len(self.lista_clientes) < 3:
            print('El banco requiere tres o más clientes iniciales')
            raise ValueError
        self.id = uuid.uuid4()

    
    def mostrar_clientes(self):
        for cliente in self.lista_clientes:
            print(cliente.nombre)
#El saldo de cada nuevo cliente no puede exceder el 10% del saldo institucional
    def registrar_clientes(self):
        nombre = input('Ingrese el nombre del nuevo usuario: ')
        saldo = int(input('Ingrese el saldo del nuevo usuario: '))
        while saldo > 0.1 * self.saldo_institucional:
            print(f'El máximo saldo es de {0.1 * self.saldo_institucional}')
            saldo = int(input('Ingrese el saldo del nuevo usuario: '))
        nuevo_cliente = Cliente(nombre,saldo)
        self.lista_clientes.append(nuevo_cliente)
        self.saldo_institucional += saldo
                
    def mostar_toda_info_clientes(self):
        for cliente in self.lista_clientes:
            time.sleep(2)
            print(f'El nombre del cliente es {cliente.nombre}, su saldo es {cliente.saldo} y su identificador es {cliente.id}')
        
cliente1 = Cliente('Constanza Hurtado', 100000)
cliente2 = Cliente('Constanza Hurtado2', 100000)
cliente3 = Cliente('Constanza Hurtado3', 100000)
cliente4 = Cliente('Constanza Hurtado4', 100000)
'''
cliente1.mostrar_saldo_cliente()
print(cliente1.historial_retiros)
print('Se genera el retiro')
cliente1.retirar_dinero(49000)
print('Retiro exitoso')
cliente1.mostrar_saldo_cliente()
print(cliente1.historial_retiros)
'''

banco1 = Banco('Santander', 10000000, cliente1, cliente2, cliente3, cliente4)
#banco1.mostrar_clientes()

banco1.registrar_clientes()
banco1.mostar_toda_info_clientes()
