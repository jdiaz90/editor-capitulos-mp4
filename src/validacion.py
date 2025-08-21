# src/validacion.py
import re
import FreeSimpleGUI as sg

def validar_capitulo(inicio_str, fin_str, titulo, duracion_seg):
    # 1. Inicio y Fin deben ser numéricos
    try:
        inicio = float(inicio_str)
        fin = float(fin_str)
    except ValueError:
        sg.popup_error("Inicio y Fin deben ser números válidos (usa punto como separador decimal).")
        return False

    # 2. No negativos
    if inicio < 0 or fin < 0:
        sg.popup_error("Inicio y Fin no pueden ser negativos.")
        return False

    # 3. Inicio < Fin
    if inicio >= fin:
        sg.popup_error("El inicio debe ser menor que el fin.")
        return False

    # 4. Dentro de la duración del vídeo
    if inicio > duracion_seg or fin > duracion_seg:
        sg.popup_error(f"Los tiempos deben estar dentro de la duración del vídeo ({duracion_seg:.3f} s).")
        return False

    # 5. Título no vacío
    if not titulo.strip():
        sg.popup_error("El título no puede estar vacío.")
        return False

    # 6. Título sin caracteres prohibidos para FFMETADATA
    #    - Sin saltos de línea
    #    - Sin caracteres de control
    #    - Evitar comillas dobles sin escapar (permitimos simples)
    if "\n" in titulo or "\r" in titulo:
        sg.popup_error("El título no puede contener saltos de línea.")
        return False
    if re.search(r'[\x00-\x1F\x7F]', titulo):
        sg.popup_error("El título contiene caracteres de control no permitidos.")
        return False
    if '"' in titulo:
        sg.popup_error('El título no debe contener comillas dobles (").')
        return False

    return True
