import os
import FreeSimpleGUI as sg
from . import dialogos, tabla, capitulos

def manejar_evento(ev, vals, player, capitulos_list, window, video):
    """Gestiona eventos de la ventana principal."""

    # Controles básicos de reproducción
    if ev == '▶ Reproducir':
        player.play()
    elif ev == '⏸ Pausa':
        player.pause()

    # Edición de capítulos
    elif ev == 'Editar seleccionado':
        sel = vals['-TABLA-']
        if sel:
            dialogos.editar_capitulo(sel[0], capitulos_list, window, player)

    elif ev == 'Añadir':
        dialogos.añadir_capitulo(capitulos_list, window, player)

    elif ev == 'Eliminar':
        sel = vals['-TABLA-']
        if sel:
            tabla.eliminar_fila(capitulos_list, sel[0])
            window['-TABLA-'].update(values=capitulos_list)

    # Saltar al inicio del capítulo
    elif ev == 'Ir al inicio del capítulo':
        sel = vals['-TABLA-']
        if sel:
            try:
                start_sec = float(capitulos_list[sel[0]][1])
                player.set_time(int(start_sec * 1000))
            except Exception:
                pass

    # Guardar y aplicar cambios
    elif ev == 'Guardar y aplicar cambios':
        capitulos.guardar_txt(capitulos_list)
        base = os.path.splitext(os.path.basename(video))[0]
        sin_caps = os.path.join(capitulos.TEMP_DIR, f"{base}_sinchap.mp4")
        capitulos.crear_copia_sin(video, sin_caps)
        salida_final = os.path.join(capitulos.OUTPUT_DIR, f"{base}_editado.mp4")
        capitulos.aplicar(sin_caps, salida_final)
        sg.popup(f"Vídeo generado en:\n{salida_final}")
