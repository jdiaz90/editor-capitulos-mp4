import FreeSimpleGUI as sg
from src import config_app, reproductor, capitulos, utilidades, layouts, eventos

# --- Inicialización ---
config, vlc_path = config_app.cargar_config()
import vlc

sg.theme('SystemDefault')
video = utilidades.seleccionar_video()

capitulos_list = capitulos.extraer(video)
col_names = ['#', 'Inicio (s)', 'Fin (s)', 'Título']

layout = [
    [layouts.crear_col_video(),
     layouts.crear_col_tabla(col_names, capitulos_list)],
    [sg.Button('Salir')]
]

window = sg.Window('Editor MP4', layout, finalize=True,
                   resizable=True, size=(1400, 800))

# --- Reproductor VLC ---
player, duracion_ms = reproductor.crear({
    "video_path": video,
    "canvas_elem": window['-CANVAS-'],
    "slider_elem": window['-SLIDER-'],
    "osd_elem": window['-OSD-'],
    "tiempo_elem": window['-TIME-']
})
window['-SLIDER-'].update(range=(0, duracion_ms / 1000))
slider_dragging = False

# --- Bucle principal ---
while True:
    ev, vals = window.read(timeout=100)
    if ev in (sg.WINDOW_CLOSED, 'Salir'):
        break

    # Actualizar tiempo y slider
    ms = reproductor.actualizar_tiempo(player, window['-TIME-'], vals['-OSD-'])
    if not slider_dragging:
        window['-SLIDER-'].update(value=ms / 1000)

    if ev == '-SLIDER-':
        slider_dragging = True
        player.set_time(int(float(vals['-SLIDER-']) * 1000))
        slider_dragging = False

    # Enviar el resto de eventos al gestor
    eventos.manejar_evento(ev, vals, player, capitulos_list, window, video)

# --- Limpieza carpeta temp ---
utilidades.limpiar_temp(capitulos.TEMP_DIR)
window.close()
