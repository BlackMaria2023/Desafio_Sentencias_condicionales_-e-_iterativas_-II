import sys
ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

40000
{'Mayo': 81000, 'Agosto': 41200, 'Noviembre': 91000}

mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "noviembre", "diciembre"]
ventas = [15000, 22000, 12000, 17000, 81000, 13000, 21000, 41200, 25000, 21500, 91000, 21000]
diccionario = {k:v for k,v in zip(mes, ventas)}
diccionario_filter = {k:v for k,v in diccionario.items() if v > 40000}
print(diccionario_filter)

