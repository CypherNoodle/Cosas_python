import json
import requests
from datetime import date, time, datetime, timedelta

#Un poco de decoracion para el titulo en la consola 
print(" *****************************************************")
print(" *Indicadores economicos extraido desde mindicador.cl*")
print(" *****************************************************\n")
 
class mindicador():
 
    def __init__(self, indicador, fecha):
        self.indicador = indicador
        self.fecha = fecha
 
    def InfoApi(self):
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en la fecha actual
        url = f"https://mindicador.cl/api/{self.indicador}/{self.fecha}"
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        dict = data
        d = data['serie']                                                               #debug: acceder a cadena "serie" de Json
        index = d[0]                                                                    #debug: accede al indice 0 
        valor = int(index['valor'])                                                     #debug: accede solo al valor del indicador y lo convierte a int
        print(f"    El valor de {self.indicador} a fecha de {hoy}, es de ${valor}")     #Imprime el indicador, fecha actual y su valor entero
    
    def InfoApiIpc(self):
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en la fecha actual
        url = f"https://mindicador.cl/api/{self.indicador}/{self.fecha}"
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        dict = data
        d = data['serie']                                                                       #debug: acceder a cadena "serie" de Json
        index = d[0]                                                                            #debug: accede al indice 0 
        valor = (index['valor'])                                                                #debug: accede solo al valor de ipc
        print(f"    El valor de {self.indicador} a fecha de {mes_anterior}, es de {valor}")     #Imprime el indicador, fecha actual y su valor entero                      

#Parametros de configuracion de formato de fecha       
fecha_actual = datetime.now()                                                           #Recoge la fecha actual de la ejecucion
hoy = str(fecha_actual.strftime('%d-%m-%Y'))                                            #Formato de fecha: Dia, Mes, Año actual

#Parametros para datos que son mensuales, ejemplo IPC
dia = datetime.today()                                                                  #Recoge la fecha actual
primer_dia = datetime(day = 1, month = dia.month - 2, year=dia.year)                    #Ajustamos para que muestre 2 meses antes
mes = primer_dia.replace(day = 1)                                                       #Reemplazamos el dia para que siempre sea el primer dia del mes
mes_anterior = str(mes.strftime('%d-%m-%Y'))                                            #Formato de fecha: Dia, Mes, Año actual
#(mes_anterior)                                                                         #Debug: Mostrar fecha de mes anterior para comprobar

#Indicador: UF
uf = mindicador("uf", hoy)                                                              #Llamamos a la clase
uf.InfoApi()                                                                            #Llamar a la API

#Indicador: UTM
utm = mindicador("utm", hoy)                                                            #Llamamos a la clase
utm.InfoApi()                                                                           #Llamar a la API

#Indicador: Dolar
dolar = mindicador("dolar", hoy)                                                        #Llamamos a la clase
dolar.InfoApi()                                                                         #Llamar a la API

#Indicador: Euro
euro = mindicador("euro", hoy)                                                          #Llamamos a la clase
euro.InfoApi()                                                                          #Llamar a la API

#Indicador: IPC (prueba)
euro = mindicador("ipc", mes_anterior)                                                  #Llamamos a la clase
euro.InfoApiIpc()                                                                       #Llamar a la API
print("  Presione enter para cerrar... \n")
input()                                                                                 #Espera input del usuario