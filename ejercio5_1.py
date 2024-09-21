print("______________________________________")

print("Ejercicios3: Puntaje Final")

print("______________________________________")


print("Ingrese numero de respuesta correctas:")
RC =int(input())
print("Ingrese numero de respuesta incorectas:")
RI =int(input())
print("Ingrese numero de respuesta en blanco:")
RB =int(input())

PCR =RC*3
PRI =RI*-1
PRB =RB*0

PF = PCR+PRI+PRB
print("El puntaje Total es:",PF)