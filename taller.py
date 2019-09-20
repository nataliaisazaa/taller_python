import requests
import lxml.html as lh
import bs4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pymysql.cursors

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

url2 = "https://www.foxsports.com.co"
url = "https://pokemondb.net/pokedex/all"

def Menu():
    print("\n")
    print("1. Mostrar Etiquetas")
    print("2. Ver Codigo Fuente")
    print("3. Graficar Tabla de Posiciones")
    print("4. Mostrar Base de Datos")
    print("0. Salir")
    opcion = input("\nSeleccione una opcion ")
    MenuOpciones(opcion)

def MenuOpciones(opcion):
    if(opcion == "1"):
        MenuEtiquetas()
    elif(opcion == "2"):
        CodigoFuente()
    elif(opcion == "3"):
        Graficar()
    elif (opcion == "4"):
        BaseDatos()
    else:
        print("1")

def MenuEtiquetas():
    etiqueta = input("Que etiqueta desea mostrar? ")
    Etiquetas(etiqueta)

def Etiquetas(etiqueta):
    print("\n")
    html = urlopen(url2)
    soup = BeautifulSoup(html, 'html5lib')
    type(soup)
    print('\n'.join(strong.text for strong in soup.select(etiqueta)))

def CodigoFuente():
    print("\n")
    html = urlopen(url2)
    soup = BeautifulSoup(html, 'html5lib')
    type(soup)
    print(soup.get_text())

def Graficar():
    print("\n")
    pagina = requests.get(url)
    documento = lh.fromstring(pagina.content)
    tr = documento.xpath('//tr')

    columnas = []
    i = 0
    for t in tr[0]:
        i += 1
        nombre = t.text_content()
        columnas.append((nombre, []))

    for j in range(1, len(tr)):
        T = tr[j]
        if len(T) != 10:
            break

        i = 0
        for t in T.iterchildren():
            informacion = t.text_content()
            if i > 0:
                try:
                    informacion = int(informacion)
                except:
                    pass
            columnas[i][1].append(informacion)
            i += 1

    Tabla = {title: column for (title, column) in columnas}
    df = pd.DataFrame(Tabla)
    nuevo_df = df.iloc[0:10]
    nombres = nuevo_df['Name']
    ataques = nuevo_df['Attack']
    plt.pie(ataques, labels=nombres, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()

def BaseDatos():
    nombres = []
    ataques = []

    conexion = pymysql.connect(host='localhost',user='root',password='123456',db='nada',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT `nombre`, `ataque` FROM `informacion`"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            for row in resultado:
                nombres.append(row["nombre"])
                ataques.append(row["ataque"])
    finally:
        conexion.close()

    plt.pie(ataques, labels=nombres, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    Menu()