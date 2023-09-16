""" Modulo empleadosBD.py implementa una colección de empleados """
from empleado import *


#Constructoras ------------------------------------------------------------------------------------------------------------------------------

def crearBBDD():
    """ La función crearBBDD crea una BBDD vacía. 
    Devuelve una estructura diccionario. El diccionario vacío es así: {} ó dict(). Cualquiera de las dos formas es válida.
    Luego, sobre esta estructura agregaremos a los nuevos empleados. """

    return dict()



def agregarBBDD( BBDD, empleado ): 
    """La función agregarBBDD agrega un empleado inexistente a la BBDD. 
    La BBDD es un diccionario con clave #Legajo. 
    Por ejemplo, si el empleado={'#Legajo': 108, 'Nombre': 'Juan', ....} 
    entonces  BBDD={108: {'#Legajo': 108, 'Nombre': 'Juan', ....}} """

    #Obtener el legajo con la función que nos provee el módulo empleado
    clave = getLegajoEmpleado(empleado) 

    if clave in BBDD:
        #el empleado ya existe en la base de datos, no se agrega
        print('El empleado ya existe en la BBDD')
    else:
        #el empleado no existe en la BBDD, entonces lo agrego. 
        BBDD[clave] = empleado
        print('El empleado se agregó correctamente')
    return
     

 
def agregarBBDD_desdeArchivo(BBDD,archivo):
    """La función agregarBBDD_desdeArchivo agrega los empleados inexistentes a la BBDD. 
      Los datos que están almacenados en un archivo csv se ingresan a la BBDD. """
    
    # abro el archivo.cvs
    f = open(archivo, 'r')
    #leo el archivo
    lineas = f.readlines()
    #proceso 
    for i in lineas:     
        
        #crear el empleado
        e = crearEmpleado_desdeCadena(i[:-1])

        #añadir el empleado a la BBDD con clave LEGAJO  
        agregarBBDD(BBDD, e)
       
    f.close()


#Observadoras---------------------------------------------------------------------------------------------------------------------


def mostrarEmpleadoBBDD(BBDD, legajo_consulta):
    """La función mostrarEmpleadoBBDD muestra la información de un empleado 
    que ya existe dentro de la BBDD"""
    if ( legajo_consulta in BBDD):
        print(BBDD[legajo_consulta] )
    else:
        print('doy un aviso que no existe el legajo que busca')
    return  

def mostrarTodaBBDD(BBDD):
    for i in BBDD.values():
        print(i)
    return 

def listadoEmpleadosBBDD(BBDD):
    """La función devuelve una lista de lista de empleados. Listas anidadas"""
    return

def enLicenciaBBDD(BBDD):
    """Listar el personal que tomó licencia y la cantidad que lo hizo."""
    lista = []
    for i in BBDD.values():
        if (estaConLicenciaEmpleado(i)):
            lista.append(getNombreEmpleado(i))
    return lista

def mayorImporte_menosTrabaja(BBDD):
    """ la funcion mayorImporte_menosTrabaja retorna si o no"""
    mayorSueldo=0
    menosHrsTrabajadas = 0
    for i in BBDD:
        if getSueldo(i) > mayorSueldo:
            mayorSueldo = getSueldo(i)
            e_gana_mas = i
            
        elif getHorasTrabEmpleado(i) < menosHrsTrabajadas:
           menosHrsTrabajadas =  getHorasTrabEmpleado (i)
           e_menos_trabaja = i  
    return (e_gana_mas == e_menos_trabaja)
    

def sueldoBruto_decreciente(BBDD):
    lista = []
    #COMPLETAR
    return lista

def listarHaBrutoBBDD(BBDD):
    """ la función listarHaBrutoBBDD lista los haberes brutos (sueldos=horasTrab*pagoxhora)
     de todos los empleados de la BBDD """
    for i in BBDD.values():
        print(getNombreEmpleado(i), getSueldo(i))
    #imprimir el total (queda para deber)
    return 

#Modificadoras----------------------------------------------------------------------------------------------------------------------------
def borrarBBDD (BBDD, legajo_eliminar):
    """ La función borrarBBDD elimina un empleado existente de la BBBD.
      El legajo del empleado que se eliminará viene dado en el parámetro legajo_eliminar."""
    # en un diccionario borro con "del " . 
    # El diccionario es BBDD. 
    # Tengo que borrar legajo_eliminar
    if (legajo_eliminar in BBDD):
        del BBDD[legajo_eliminar]
        print('el empleado se ha borrado exitosamente')
    else:
        print ("no existe ese empleado")
    return


