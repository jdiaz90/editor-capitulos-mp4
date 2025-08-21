import FreeSimpleGUI as sg
from . import tabla

def crear_col_video():
    return sg.Column([
        [sg.Canvas(key='-CANVAS-', size=(960,540))],
        [sg.Slider(range=(0,1), default_value=0, resolution=0.001,
                   orientation='h', size=(80,20), key='-SLIDER-', enable_events=True)],
        [sg.Button('▶ Reproducir'), sg.Button('⏸ Pausa'),
         sg.Checkbox('OSD', default=True, key='-OSD-'),
         sg.Text('Tiempo:'), sg.Text('0.000000', key='-TIME-', size=(12,1))]
    ], element_justification='center')

def crear_col_tabla(col_names, capitulos_list):
    return sg.Column([
        [tabla.crear_tabla(col_names, capitulos_list)],
        [sg.Button('Editar seleccionado'), sg.Button('Añadir'),
         sg.Button('Eliminar'), sg.Button('Ir al inicio del capítulo')],
        [sg.Button('Guardar y aplicar cambios')]
    ])
