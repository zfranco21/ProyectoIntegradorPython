
""" Módulo empleado.py ofrece toda la funcionalidad para crear un empleado, 
consultar los datos del empleado o modificar los datos que hayan sido ingresados anteriormente"""

#Constructoras -----------------------------------------------------------------------------------------------------------------

def crearEmpleado():
    """La funciòn crearEmpleado crea un empleado.
    Primero pide que ingresemos los datos por consola.
    Luego, crea un diccionario empleado con los datos que le brindó el usuario.
    Finalmente, devuelve el empleado. """
    
    #ingreso los datos por consola 
    datos0 = str(input('¿Legajo Nro.?: '))
    datos1 = str(input('¿Nombre?: '))
    datos2 = input('¿ profesión?: ')
    datos3 = int(input('¿ Horas trabajadas?: '))
    datos4 = float(input('¿pago por hora?: '))
    datos5 = input('¿licencia?: ')

    #crear el diccionario empleado (crear objeto empleado)
    empleado = {'#Legajo': datos0, 'Nombre': datos1, 'Profesión': datos2, 'HorasTrab': datos3, 'PagoxHs': datos4, 'TipoLic': datos5}

    return empleado

def crearEmpleado_desdeCadena(cadenaSC):
    """La funciòn crearEmpleado(cadenaSC) crea un empleado desde una cadena separada por comas.
       Finalmente, devuelve el empleado. """
    
    #la función split me devuelve una lista
    cadenaSC = (cadenaSC.split(','))

    #crear el diccionario empleado (crear objeto empleado)
    empleado = {'#Legajo': cadenaSC[0], 'Nombre': cadenaSC[1], 'Profesión': cadenaSC[2], 'HorasTrab': int(cadenaSC[3]), 'PagoxHs': float(cadenaSC[4]), 'TipoLic': cadenaSC[5]}

    return empleado



#Observadoras -----------------------------------------------------------------------------------------------------------------------
def getLegajoEmpleado(empleado):
    """función que permite observar el número de legajo de empleado"""
    return empleado['#Legajo']


def getNombreEmpleado(empleado):
    """Función que permite observar el nombre del empleado"""
    return empleado['Nombre']


def getProfesionEmpleado(empleado):
    """Función que permite observar  la profesión del empleado"""
    return empleado['Profesion']


def getHorasTrabEmpleado(empleado):
    """Función que permite observar  las horas que trabajó el empleado"""
    return empleado['HorasTrab']


def getPagoxHsEmpleado(empleado):
    """Función que permite observar  el pago por hora del empleado"""
    return empleado['PagoxHs']

def getSueldo(empleado):
    """Función que permite observar  el sueldo del empleado"""
    return empleado['HorasTrab']*empleado['PagoxHs']

def estaConLicenciaEmpleado(empleado):
    """Función que permite observar  si el empleado está de licencia (SI,NO)"""
    #solucion 1
    #Licencia = empleado['TipoLic'].find('lic')
    #return  Licencia

    #solucion de araceli. Andando!!!
    if ('lic' in empleado['TipoLic']):
        return True
    else:
        return False
    

#Modificadoras ------------------------------------------------------------------------------------------------------------------

def setNombreEmpleado(empleado):
    """Función que permite modificar el nombre del empleado"""
    empleado['Nombre'] = str(input('¿Nombre?: '))
    return empleado

def setPagoxHs(empleado):
    """Función que permite actualizar el importe del monto por hora del empleado"""
    empleado['Nombre'] = float(input('¿pago por hora?: '))
    return empleado

#CONTINUAR COMPLETANDO 