import math

def cuadratica(a, b, c):
    #Resolver ecuaciones cuadráticas
    print("La ecuación que quieres resolver es", int(a), "X^2 +", int(b), "X +", int(c), " = 0")
    det = b ** 2 -4*a*c
    if det >= 0:
        x1= (math.sqrt(det) - b) / (2*a)
        x2= (math.sqrt(det) + b) / (2*a)
        print("Los resultados son: ", "\nx_1 = ", x1,"\nx_2 = ", x2) 
    else:
        print("La ecuación no tiene soluciones reales.")
        print("Las soluciones complejas son: ")
        print("x_1 = ", -1*b/(2*a),"+",(-det),"/",(2*a),"i\n","x_2 = ", -b/(2*a),"-",(-det),"/",(2*a),"i")

x = input("Ingrese los valores de los coeficientes de la ecuación:\n a = ")
y = input("b = ")
z = input("c = ")

cuadratica(float(x), float(y), float(z))
