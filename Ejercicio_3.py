#Los tramos impositivos para la declaración de la renta en un 
# determinado país son los siguientes:

# ------ Renta------------   ----Tipo impositivo
#   menos de 10000 $                  5 %
#   entre 10000 $ y 20000 $           15 %
#   entre 20000 $ y 35000 $           20 %
#   entre 35000 $ y 60000 $           30 %
#   mas de 60000 $                    45 %

#Escribir un programa que pregunte al usuario su renta anual y muestre
# por pantalla el tipo impositivo que le corresponde. 

renta=int(input("¿Cual es renta anual?")) #pregunta al usuario su renta
if renta<10000:
    tipo_impo=5
elif renta<20000:
    tipo_impo=15
elif renta<35000:
    tipo_impo=20
elif renta<60000:
    tipo_impo=30
else:
    tipo_impo=45
print("tienes que pagar" , renta*tipo_impo/100, "$") #mostrando la renta y el tipo_impo







                                                                    #resuelto roy and manuel