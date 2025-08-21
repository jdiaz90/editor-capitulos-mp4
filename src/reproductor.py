import time
import vlc
import FreeSimpleGUI as sg

def crear(player_config):
    """
    Inicializa el reproductor VLC incrustado en la GUI.

    player_config: dict con claves:
      - video_path: ruta al vídeo
      - canvas_elem: elemento sg.Canvas donde se incrusta el vídeo
      - slider_elem: elemento sg.Slider que hará de barra de progreso
      - osd_elem: elemento sg.Checkbox que activa/desactiva el OSD
      - tiempo_elem: elemento sg.Text donde mostrar el tiempo actual
    """
    video_path = player_config["video_path"]
    canvas_elem = player_config["canvas_elem"]
    slider_elem = player_config["slider_elem"]
    osd_elem = player_config["osd_elem"]
    tiempo_elem = player_config["tiempo_elem"]

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(video_path)
    player.set_media(media)

    # Incrustar en el canvas
    player.set_hwnd(canvas_elem.Widget.winfo_id())

    # Arrancar y pausar para inicializar
    player.play()
    time.sleep(0.6)
    player.pause()

    duracion_ms = player.get_length() or 1
    slider_elem.update(range=(0, duracion_ms/1000))

    return player, duracion_ms

def actualizar_tiempo(player, tiempo_elem, mostrar_osd):
    """
    Actualiza el texto con el tiempo actual y, si está activado, el OSD de VLC.
    Devuelve el tiempo actual en milisegundos.
    """
    ms = player.get_time()
    cur_str = format_six_decimals(ms)
    tiempo_elem.update(cur_str)
    if mostrar_osd:
        try:
            player.video_set_marquee_int(vlc.VideoMarqueeOption.Enable,1)
            player.video_set_marquee_string(vlc.VideoMarqueeOption.Text, cur_str)
        except:
            pass
    else:
        try:
            player.video_set_marquee_int(vlc.VideoMarqueeOption.Enable,0)
        except:
            pass
    return ms

def format_six_decimals(ms):
    """Convierte milisegundos a segundos con 6 decimales."""
    return "0.000000" if ms is None or ms < 0 else f"{ms/1000:.6f}"
