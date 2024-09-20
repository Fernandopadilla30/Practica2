#edwin manuel
#Para tributar un determinado impuesto se debe ser mayor 
# de 16 años y tener unos ingresos iguales o superiores 
# a 1000 € mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre 
# por pantalla si el usuario tiene que tributar o no. 

edad= int(input("ingresar tu edad: "))
ingreso_mes= float(input("Ingresar tus ingresos mensuales: "))
if edad >16 and ingreso_mes >=1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")