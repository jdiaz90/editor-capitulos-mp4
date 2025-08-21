# src/dialogos.py
import FreeSimpleGUI as sg
from .validacion import validar_capitulo

def tiempo_actual_segundos(player):
    return f"{player.get_time()/1000:.6f}"

def editar_capitulo(idx, capitulos, window, player):
    opciones = ['Inicio (s)', 'Fin (s)', 'Título']
    evp, valp = sg.Window(
        'Seleccionar campo',
        [[sg.Text('¿Qué quieres editar?')],
         [sg.Combo(opciones, default_value=opciones[0], key='-COLUMNA-', readonly=True)],
         [sg.Button('OK'), sg.Button('Cancelar')]],
        modal=True
    ).read(close=True)

    if evp != 'OK':
        return

    map_col = {'Inicio (s)':1, 'Fin (s)':2, 'Título':3}
    col_idx = map_col[valp['-COLUMNA-']]

    # Valores actuales para validación
    inicio_actual = capitulos[idx][1]
    fin_actual = capitulos[idx][2]
    titulo_actual = capitulos[idx][3]

    layout = [
        [sg.Input(default_text=str(capitulos[idx][col_idx]), key='-VAL-'),
         sg.Button('Usar tiempo actual')],
        [sg.Button('OK'), sg.Button('Cancelar')]
    ]
    win = sg.Window(f'Editar {valp["-COLUMNA-"]}', layout, modal=True)
    while True:
        e_ev, e_vals = win.read()
        if e_ev in (sg.WINDOW_CLOSED, 'Cancelar'):
            break
        if e_ev == 'Usar tiempo actual':
            win['-VAL-'].update(tiempo_actual_segundos(player))
        if e_ev == 'OK':
            nuevo_valor = e_vals['-VAL-']
            # Preparar datos para validar según columna
            if col_idx == 1:
                if not validar_capitulo(nuevo_valor, fin_actual, titulo_actual, player.get_length()/1000):
                    continue
            elif col_idx == 2:
                if not validar_capitulo(inicio_actual, nuevo_valor, titulo_actual, player.get_length()/1000):
                    continue
            elif col_idx == 3:
                if not validar_capitulo(inicio_actual, fin_actual, nuevo_valor, player.get_length()/1000):
                    continue
            capitulos[idx][col_idx] = nuevo_valor
            window['-TABLA-'].update(values=capitulos)
            break
    win.close()

def añadir_capitulo(capitulos, window, player):
    layout = [
        [sg.Text('Inicio (segundos)'), sg.Input(key='-INICIO-'),
         sg.Button('Usar tiempo actual', key='-TINI-')],
        [sg.Text('Fin (segundos)'), sg.Input(key='-FIN-'),
         sg.Button('Usar tiempo actual', key='-TFIN-')],
        [sg.Text('Título'), sg.Input(key='-TITULO-')],
        [sg.Button('OK'), sg.Button('Cancelar')]
    ]
    win = sg.Window('Añadir capítulo', layout, modal=True)
    while True:
        a_ev, a_vals = win.read()
        if a_ev in (sg.WINDOW_CLOSED, 'Cancelar'):
            break
        if a_ev == '-TINI-':
            win['-INICIO-'].update(tiempo_actual_segundos(player))
        if a_ev == '-TFIN-':
            win['-FIN-'].update(tiempo_actual_segundos(player))
        if a_ev == 'OK':
            if validar_capitulo(a_vals['-INICIO-'], a_vals['-FIN-'], a_vals['-TITULO-'], player.get_length()/1000):
                capitulos.append([len(capitulos), a_vals['-INICIO-'], a_vals['-FIN-'], a_vals['-TITULO-']])
                window['-TABLA-'].update(values=capitulos)
            # Si no es válido, no se cierra y se muestra error desde validar_capitulo
            else:
                continue
            break
    win.close()
