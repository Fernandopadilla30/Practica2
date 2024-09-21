#En este ejercicio, tendrán total libertad para elegir la problemática y la mejor solución. 
# Cada grupo podrá decidir su propio enfoque y desarrollar el software según sus criterios. 
# El grupo que presente la mejor solución será el único en recibir los 60 puntos asignados a esta pregunta.


#Generadora de cotizaciones en Python

def ingresar_datos_cliente():
    cliente = {}
    
    cliente["nombre"] = input("Ingresa el nombre del cliente: ")
    cliente["direccion"] = input("Ingresa la direccion del cliente: ")
    cliente["telefono"] = input("Ingresar el telefono del cliente: ")
    cliente["email"]= input("Ingresar el correo electronico del cliente: ") 
    
    print ("\nDatos del cliente guardado: ")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Direccion: {cliente['direccion']}")
    print(f"Telefono: {cliente['telefono']}")
    print(f"Email: {cliente['email']}")
    
    return cliente

datos_clientes = ingresar_datos_cliente()



productos = []
def agregar_producto():
    
    producto = {}
    
    producto["nombre"] = input("Ingresa el nombre del producto o servicio: ")
    producto["precio"] = float(input("Ingrese el precio unitario: "))
    producto["cantidad"] = int(input("Ingrese la cantidad: "))
    
    productos.append(producto)
    print(f"Producto '{producto['nombre']})' agregado a la cotizacion.\n")
    
def agregar_productos_a_cotizacion():
    while True:
        agregar_producto()
        
        continuar= input("¿Quieres agregar otro Producto? (s/n): ").lower()
        if continuar != 's':
            break

def calcular_total():
    total = 0
    for producto in productos:
        costo_producto = producto["precio"] * producto["cantidad"]
        total += costo_producto
    return total

def mostral_total():
    total= calcular_total()
    print(f"\nEl total de la cotizacion es: ${total: .2f}")
    
agregar_productos_a_cotizacion()    
mostral_total()
