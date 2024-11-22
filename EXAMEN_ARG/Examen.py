#Examen argumentativo, proyecto de creación de videojuego usando conceptos de física
#Dante Hernández Ramírez
#21 de Noviembre de 2024

#......................................................................
#Se importan las librerías...

#Librería que permite visualizar una imagen
import streamlit as st
from PIL import Image
import os

#Inicio de funciones...
def resumen_intro():
    st.write("Objetivo:")
    st.write("Eres un piloto atravezando el último tramo de una pista, el tramo "
             "en cuestión consiste de una curva y una recta, seguido de esto se"
             "encuentra la meta, debes calcular la velocidad y aceleración de tu"
             "auto para asegurar que cruces la meta en primer lugar"
             "\n SUERTEEEE!!!")
    
def obtener_valores():
    coef_derrape = 0.7 #Valor encontrado en https://intblog.onspot.com
    radio_curva = 100 #Valor en metros
    rango_vel = (30,60) #Rango de velocidad ideal para la curva
    st.write(f"---Valores constantes y parámetros---")
    st.write(f"Coeficiente de derrape: {coef_derrape}")
    st.write(f"Radio de la curva: {radio_curva} m")
    st.write(f"Rango de velocidad ideal para la curva: {rango_vel[0]} a {rango_vel[1]}")
    return coef_derrape, radio_curva, rango_vel

def fuerza_maxima(coef_derrape,radio_curva):
    gravedad = 9.8 #Constante gravitacional estándar

    '''Se inician los calculos para delimitar la velocidad máxima a la que debe ir 
    el auto en la curva'''
    fuerza_max = coef_derrape * gravedad
    vel_max = (fuerza_max * radio_curva)**0.5 
    return vel_max * 3.6 #Se pasa todo a kilometro * hora

#Se evalua si la velocidad proporcionada  esta entre el rango
def eval_vel(vel_jugador, vel_max, rango_vel):
    #En caso de que la velocidad sea excesiva
    if vel_jugador > vel_max:
        st.write("El exceso de velocidad a hecho que el coche salga de la pista en"
              "plena curva...")
        #En caso de que la velocidad sea muy baja
    elif vel_jugador < rango_vel[0]:
        st.write("La velocidad es muy baja, debido a esto, un auto te ha impactado"
              "en la parte trasera de tu auto...")
        #En caso de que esté dentro del margen ideal
    elif rango_vel[0] < vel_jugador < rango_vel[1]:
        st.write("El auto ha atravezado la curva de manera exitosa")

#Se pregunta por la aceleración pasada la curva
def preguntar_acel():
    st.write("\n En la última recta, ¿cuánto deseas acelerar?")
    st.write("1. Baja")
    st.write("2. Ideal")
    st.write("3. Alta")
    op = st.radio("Selecciona una:", ('1', '2', '3'))
    return op

def evalua_op(op):
    op = int(op) #se convierte a numero entero
    if op == 1:
        st.write("El auto rival te ha adelantado por ir muy lento...")
    elif op == 2:
        st.write("FELICIDADES! ganaste la carreraaaa!!")
    elif op == 3:
        st.write("Ibas muy rápido, ganaste la carrera, peeero tuviste un acidente al"
              "momento de querer frenar...")
    else:
        st.write("Opción inválida")

#Se crea un main en donde se registrarán todas las respuestas del usuario
def main():
    st.title("--SIMULADOR DE SEGMENTO FINAL DE UNA CARRERA--")

    #Se va a cargar la imagen que verá el usuario en todo momento
    if os.path.exist("Image.png"):
        image = Image.open("Image.png") #Directorio personal
        st.image(image, caption="Auto", use_column_width= True)

    resumen_intro()
    coef_derrape, radio_curva, rango_vel = obtener_valores()
    vel_max = fuerza_maxima(coef_derrape,radio_curva)
    st.write(f"La velocidad máxima segura para la curva es: {vel_max:.2f} km/h")

    #Se piden los datos al usuario
    vel_jugador = st.number_input("¿Cuál es tu velocidad actual?", min_value=0.0)
    eval_vel(vel_jugador, vel_max, rango_vel)

    if rango_vel[0] <= vel_jugador <= rango_vel[1]:
        op  = preguntar_acel()
        evalua_op(op)

    st.write("FIN DEL JUEGO...")