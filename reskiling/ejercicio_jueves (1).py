#Proveedor, Cliente, Producto, Vendedor.

#Proveedor: RUT, Nombre Legal, Razón Social, País, Una distinción entre persona jurídica o persona natural

# Cliente, Producto y Vendedor: agregar un atributo.

# Al momento de instanciar un objeto de la clase Producto, 
# deberá existir una Composición con la clase Proveedor

class Cliente:
    def __init__(self, nombre, apellido, id_cliente, correo, fecha_registro, saldo, direccion=None):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.saldo = saldo
        self.direccion = direccion
    
    def mostrar_saldo(self):
        print(self.saldo)
    
    def agregar_saldo(self, ingreso):
        self.saldo = self.saldo + ingreso
        return 'Ingresado con exito'


#Proveedor: RUT, Nombre Legal, Razón Social, País, Una distinción entre persona jurídica o persona natural

class Proveedor:
    def __init__(self, rut_proveedor, nombre_legal, razon_social, pais, tipo_sociedad):
        self.rut_proveedor = rut_proveedor
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_sociedad = tipo_sociedad

class Producto:
    def __init__(self, sku, nombre_producto, categoria, valor_neto, proveedor=None, stock=0):
        self.sku = sku
        self.nombre_producto = nombre_producto
        self.categoria = categoria
        self.valor_neto = valor_neto
        self.proveedor = proveedor
        self.stock = stock
        self.__impuesto = 1.19

    def asignar_proveedor(self, proveedor_nuevo:Proveedor):
        self.proveedor = proveedor_nuevo
        return 'Proveedor asignado'
    def desencapsular_impuesto(self):
        impuesto = self.__impuesto
        return impuesto

#Se deberá crear un método vender de la clase Vendedor y esta deberá descontar el valor del atributo
#stock de la clase Producto y calcular un 0.5% de comisión referente al valor_neto del producto y 
# luego
#sumarlo al atributo comisión de la clase Vendedor. 
# Luego el método deberá calcular el valor final del
#producto y descontarlo del atributo saldo de la clase Cliente.

class Vendedor:
    def __init__(self, rut_vendedor, nombre_vendedor, apellido_vendedor, seccion, telefono_vendedor=None):
        self.rut_vendedor = rut_vendedor
        self.nombre_vendedor = nombre_vendedor
        self.apellido_vendedor = apellido_vendedor
        self.seccion = seccion
        self.telefono_vendedor = telefono_vendedor
        self.seguro_social = True
        self.comisiones = 0
    
    def vender(self, producto:Producto, cliente:Cliente, unidades_venta):
        if producto.stock >= unidades_venta and cliente.saldo >= producto.valor_neto*unidades_venta*producto.desencapsular_impuesto():
            producto.stock = producto.stock - unidades_venta
            self.comisiones = self.comisiones + (unidades_venta * producto.valor_neto * 0.005)
            cliente.saldo = cliente.saldo - (producto.valor_neto*unidades_venta*producto.desencapsular_impuesto())
            
        elif producto.stock < unidades_venta:
            print('No hay stock suficiente')
        else:
            print('El cliente no tiene saldo suficiente')



cliente1 = Cliente('Ronald', 'Madariaga', 1, 'ronald@gmail.com', '1/1/2021', 100000)

cliente1.mostrar_saldo()
print(cliente1.agregar_saldo(1000))
cliente1.mostrar_saldo()

vendedor1 = Vendedor('123', 'Joao', 'Guzman', 'b')
vendedor1.seguro_social

proveedor1 = Proveedor('123', 'Sony', 'Comercializadora LTDA', 'Chile', 'Juridica')
proveedor2 = Proveedor('122', 'Juanita PYME', 'Juanita S.A.', 'Chile', 'Persona Natural')
print(proveedor1.nombre_legal)

producto1 = Producto(123, 'Audifonos', 'Electronica', 10000, None, 5)
producto1.asignar_proveedor(proveedor1)
print(producto1.proveedor.nombre_legal)
#producto1.asignar_proveedor(proveedor2)
print(producto1.proveedor.nombre_legal)
print('-------------------')
print(producto1.stock)
print(f'La comision es de {vendedor1.comisiones}')
#vendedor1.vender(producto1, 2)
print(producto1.stock)
print(f'La comision es de {vendedor1.comisiones}')
print('-------------------')
cliente1.mostrar_saldo()
vendedor1.vender(producto1, cliente1, 2)
cliente1.mostrar_saldo()