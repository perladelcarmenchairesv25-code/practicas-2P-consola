if __name__ == "__main__":
   from operacionesMatematicas import OperacionesMatematicas    
   from holaMundo import HolaMundo
   from persona import Persona
   from triangulo import triangulo  
   from rectangulo import rectangulo
   from cuadrado import cuadrado
   operaciones = OperacionesMatematicas()

   print("elige la opcion que deseas ejecutar")
   print("1. Hola Mundo") 
   print("2. Operaciones Matematicas")
   print("3. Calcular Edad")
   print("4. Calcular Area y Perimetro de Figuras Geometricas")

   opcion = int(input("ingresa el numero de la opcion ")) 
 
if opcion == 1:
      saludo = HolaMundo("Hola Mundo programación en clases")
      saludo.mostrar_mensaje()
 
elif opcion == 2:
      operaciones=OperacionesMatematicas()
      a=int(input("ingresa el primer numero "))
      b=int(input("ingresa el segundo numero "))
      print("la suma es ", operaciones.sumar(a,b))
      print("la resta es ", operaciones.restar(a,b))
      print("la multiplicacion es ", operaciones.multiplicar(a,b))
      print("la division es ", operaciones.dividir(a,b))

elif opcion == 3:
      print("ingresa tu nombre ")
      nombre = input()
      print("ingresa tu año de nacimiento ")
      anio_nacimiento = int(input())
      persona = Persona(nombre, anio_nacimiento, 0)
      print("tu edad es ", persona.calcular_edad(2026))

elif opcion == 4:
      print ("¿que figura geometrica deseas calcular?")
      print("1. Triangulo")
      print("2. Rectangulo")
      print("3. Cuadrado")
      figura = int(input("ingresa el numero de la figura "))
      if figura == 1:
         base = float(input("ingresa la base del triangulo "))
         altura = float(input("ingresa la altura del triangulo "))
         triangulo1 = triangulo(base, altura)
         print("el area del triangulo es ", triangulo1.calcular_area())
         print("el perimetro del triangulo es ", triangulo1.calcular_perimetro())
      
      elif figura == 2:
         base = float(input("ingresa la base del rectangulo "))
         altura = float(input("ingresa la altura del rectangulo "))
         rectangulo1 = rectangulo(base, altura)
         print("el area del rectangulo es ", rectangulo1.calcular_area())
         print("el perimetro del rectangulo es ", rectangulo1.calcular_perimetro())
      
      elif figura == 3:
         lado = float(input("ingresa el lado del cuadrado "))
         cuadrado1 = cuadrado(lado)
         print("el area del cuadrado es ", cuadrado1.calcular_area())
         print("el perimetro del cuadrado es ", cuadrado1.calcular_perimetro())


else:
      print("opcion no valida. por favor, elige 1 o 2 ")
      