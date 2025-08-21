import os, shutil, FreeSimpleGUI as sg

def seleccionar_video():
    video = sg.popup_get_file('Selecciona un vídeo', file_types=(('MP4','*.mp4'),))
    if not video:
        raise SystemExit
    return video

def limpiar_temp(ruta_temp):
    for nombre in os.listdir(ruta_temp):
        ruta = os.path.join(ruta_temp, nombre)
        try:
            if os.path.isfile(ruta) or os.path.islink(ruta):
                os.remove(ruta)
            elif os.path.isdir(ruta):
                shutil.rmtree(ruta)
        except Exception as e:
            print(f"No se pudo eliminar {ruta}: {e}")
