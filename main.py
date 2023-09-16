"""----------------------------------------------------
 Trabajo integrador de Python  
 Resolver los siguientes servicios sobre el archivo.cvs:
   1) Calcular cuánto es el sueldo bruto de c/u 
   2) Calcular el total de sueldos (sobre el bruto)
   3) Listar el personal que tomó licencia y la cantidad que lo hizo.
   4) La persona que cobra el mayor importe por hora es la que menos horas trabaja?
       Responder sí o no
   5) Listar Persona - Sueldo ordenado por sueldo de mayor a menor
----------------------------------------------------
"""

from empleadosBD import *
from empleado import *
import time

#------------------------------------------------------------------------------------
# Main  
#------------------------------------------------------------------------------------
def main():

    # creación de la colección de empleados o BBDD
    empleadosBD = crearBBDD()

    # cargar la BBDD con los empleados desde el archivo.cvs
    agregarBBDD_desdeArchivo( empleadosBD, 'arch.csv' )
 
    # mostrar todo
    mostrarTodaBBDD(empleadosBD)

    # menu de opciones para ejecutar cada servicio
    opcion = 1

    while ((opcion !=9) & (opcion >= 1) & (opcion <=8)):
        print('----------------------------------------------------------------------------------------')
        print('-------  Servicios p/ Empleados --------------------------------------------------------')
        print('1. agregar un empleado inexistente') 
        print('2. dar de baja un empleado existente')
        print('3. listar la información de un empleado')
        print('4. listado de haberes brutos ')
        print('5. listado del personal en licencia ')
        print('6. La persona que cobra el mayor importe por hora es la que menos horas trabaja? (S/N)')
        print('7. Listar Persona - Sueldo ordenado por sueldo bruto decreciente')
        print('8. Listar todos los empleados')
        print('9. Salir')
        print('----------------------------------------------------------------------------------------')

        opcion=int(input('elija una opcion:  '))
        
        #---------------------------------------------
        #  ingresar un empleado nuevo a la BBDD
        #---------------------------------------------
        if (opcion == 1):
            empleado=crearEmpleado()
            agregarBBDD(empleadosBD, empleado)
           
        #---------------------------------------------
        #2. dar de baja un empleado existente'
        #--------------------------------------------
        elif (opcion==2):
            legajo = str(input('¿Legajo Nro.?: '))
            borrarBBDD(empleadosBD, legajo)

        #---------------------------------------------
        #  listar la información de un empleado que existe en la BBDD
        #---------------------------------------------
        elif (opcion == 3):
            legajo = str(input('¿Legajo Nro.?: '))
            mostrarEmpleadoBBDD(empleadosBD,legajo)
        

        #---------------------------------------------
        # 4. listado de haberes brutos
        #---------------------------------------------
        elif (opcion == 4):
            listarHaBrutoBBDD(empleadosBD)

        #---------------------------------------------
        # 5. listado de personal en licencia
        #---------------------------------------------
        elif (opcion == 5):
            lista2 = enLicenciaBBDD(empleadosBD)
            print(lista2)
            
        #---------------------------------------------
        # 6. la persona que cobra el mayor importe es la que menos trabaja?
        #---------------------------------------------
            


        #---------------------------------------------
        #8.  Listar todos los empleados'
        #--------------------------------------------
        elif (opcion == 8):
             mostrarTodaBBDD(empleadosBD)
              
        time.sleep(2)

main() 