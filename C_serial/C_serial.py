"""
Para correr el codigo el microcontrolador tiene que tener cargado el firmware de Firmata y 
debe estar conectado al puerto usb.
El código se utilizo en un Arduino UNO y se cargo el firmware  StandardFirmata de la libreria
de Arduino IDE. 
la linea "board = fi.Arduino(fi.Arduino.AUTODETECT)" se utiliza para establecer la conexion
serial con el Arduino UNO, para seleccionar un puerto espcifico se debe cambiar el argumento
"fi.Arduino.AUTODETECT" por '<Direccion del puerto serial>'.
Asi en windows quedaria como "board = fi.Arduino('COM3')"
"""
import time
import datetime
import pyfirmata2 as fi

def Sensor_1():
    board = fi.Arduino(fi.Arduino.AUTODETECT) #se establece la com. serial con arduino
    it = fi.util.Iterator(board) #se crea un hilo para leer el adc
    it.start() #se inicia el hilo
    pot1 = board.get_pin('a:0:i') #se configura el pin analogico a utilizar
    time.sleep(0.1)
    est = (pot1.read()*4.90+0.10) #se escala la lectura del adc a 0.1V x 1°C
    board.exit() #se cierra el puerto serial
    x = datetime.datetime.now() #se obtiene la fecha y hora del sistema
    f = x.strftime("%c") # se le da formato humano al la hora y fecha
    dic = {'Temperatura[°C]' : est, 'Fecha': f} #se almacenan los datos para su envio
    return(dic)

valor1 = Sensor_1()
print (valor1)

def Sensor_2():
    board = fi.Arduino(fi.Arduino.AUTODETECT)
    it = fi.util.Iterator(board)
    it.start()
    pot1 = board.get_pin('a:1:i')
    time.sleep(0.1)
    est = (pot1.read()*4.90+0.10)
    board.exit()
    x = datetime.datetime.now()
    f = x.strftime("%c")
    dic = {'Temperatura[°C]' : est, 'Fecha': f}
    return(dic)

valor2 = Sensor_2()
print (valor2)

def Sensor_entrada():
    board = fi.Arduino(fi.Arduino.AUTODETECT)
    pin = board.get_pin('d:4:i')
    pin.enable_reporting()
    time.sleep(0.1)
    est = ['visitante', 'sin visita']
    i = 0
    if str(pin.read()) =='False':
        i = 1
    elif str(pin.read())=='True':
        i = 0
    time.sleep(0.1)
    board.exit()
    x = datetime.datetime.now()
    f = x.strftime("%c")
    dic = {'En puerta' : est[i], 'Fecha': f}
    return(dic)

valor3 = Sensor_entrada()
print (valor3)

def Sensor_parqueo_1():
    board = fi.Arduino(fi.Arduino.AUTODETECT)
    pin = board.get_pin('d:5:i')
    pin.enable_reporting()
    time.sleep(0.1)
    est = ['ocupado', 'desocupado']
    i = 0
    if str(pin.read()) =='False':
        i = 1
    elif str(pin.read())=='True':
        i = 0
    time.sleep(0.1)
    board.exit()
    x = datetime.datetime.now()
    f = x.strftime("%c")
    dic = {'Estado' : est[i], 'Fecha': f}
    return(dic)

valor4 = Sensor_parqueo_1()
print (valor4)

def Sensor_parqueo_2():
    board = fi.Arduino(fi.Arduino.AUTODETECT)
    pin = board.get_pin('d:6:i')
    pin.enable_reporting()
    time.sleep(0.1)
    est = ['ocupado', 'desocupado']
    i = 0
    if str(pin.read()) =='False':
        i = 1
    elif str(pin.read())=='True':
        i = 0
    time.sleep(0.1)
    board.exit()
    x = datetime.datetime.now()
    f = x.strftime("%c")
    dic = {'Estado' : est[i], 'Fecha': f}
    return(dic)

valor5 = Sensor_parqueo_2()
print (valor5)

def Luz_parqueo_1():
    board = fi.Arduino(fi.Arduino.AUTODETECT)
    pin = board.get_pin('d:2:o')
    time.sleep(0.1)
    est = ['Luz apagada','Luz encendida']
    i = 0
    if str(pin.read()) == 'False':
        pin.write(1.0)
        i = 1
    else:
        pin.write(0.0)
        i = 0
    
    time.sleep(0.1)
    board.exit()
    x = datetime.datetime.now()
    f = x.strftime("%c")
    dic = {'Estado' : est[i], 'Fecha': f}
    return(dic)

valor6 = Luz_parqueo_1()
print (valor6)

def Luz_parqueo_2():
    board = fi.Arduino(fi.Arduino.AUTODETECT)
    pin = board.get_pin('d:3:o')
    time.sleep(0.1)
    est = ['Luz apagada','Luz encendida']
    i = 0
    if str(pin.read()) == 'False':
        pin.write(1.0)
        i = 1
    else:
        pin.write(0.0)
        i = 0
    
    time.sleep(0.1)
    board.exit()
    x = datetime.datetime.now()
    f = x.strftime("%c")
    dic = {'Estado' : est[i], 'Fecha': f}
    return(dic)

valor7 = Luz_parqueo_1()
print (valor7)