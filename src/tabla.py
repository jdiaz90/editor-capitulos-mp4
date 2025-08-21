# src/tabla.py
import FreeSimpleGUI as sg

def crear_tabla(col_names, capitulos):
    """Devuelve el elemento Table ya configurado (sin gestionar clics)."""
    return sg.Table(
        values=capitulos,
        headings=col_names,
        auto_size_columns=True,
        key='-TABLA-',
        justification='left',
        num_rows=20,
        enable_click_events=False,  # desactivamos eventos de clic
        select_mode=sg.TABLE_SELECT_MODE_BROWSE
    )

def eliminar_fila(capitulos, idx):
    """Elimina una fila y reenumera."""
    capitulos.pop(idx)
    for i, cap in enumerate(capitulos):
        cap[0] = i
