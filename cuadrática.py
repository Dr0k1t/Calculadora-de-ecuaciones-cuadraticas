import math
#Simple implementación para resolver ecuaciones cuadráticas aún si sus resultados son complejos.
def cuadratica(a, b, c):
    print("La ecuación que quieres resolver es", a, "x^2 +", b, "x +", c, " = 0")
    det = b ** 2 -4*a*c #Calcula el determiante para simplificar escritura
    if det >= 0: #Si los resultados son positivos
        x1= (math.sqrt(det) - b) / (2*a)
        x2= (math.sqrt(det) + b) / (2*a)
        print("Los resultados son: ", "\nx_1 = ", x1,"\nx_2 = ", x2) 
    else: #Si los resultados son complejos
        print("La ecuación no tiene soluciones reales.")
        print("Las soluciones complejas son: ")
        print("\nx_1 = ", -b, "/",(2*a),"+",(-det),"i/",(2*a),"\nx_2 = ",-b,"/",(2*a),"-",(-det),"i/",(2*a))

x = input("Ingrese los valores de los coeficientes de la ecuación:\n a = ")
y = input("b = ")
z = input("c = ")

cuadratica(float(x), float(y), float(z))
