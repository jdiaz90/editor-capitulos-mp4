import os
import sys
import json
import platform
import FreeSimpleGUI as sg

CONFIG_FILE = 'config.json'

def cargar_config():
    if not os.path.exists(CONFIG_FILE):
        sg.popup_error("No se encontró config.json")
        raise SystemExit

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = json.load(f)

    vlc_path = config.get('vlc_path', '').strip()

    # Si no está configurado, intentar localizar VLC automáticamente en rutas típicas
    if not vlc_path:
        posibles = [
            r"C:\Program Files\VideoLAN\VLC",
            r"C:\Program Files (x86)\VideoLAN\VLC",
            "/usr/lib/vlc",
            "/usr/local/lib/vlc",
            "/Applications/VLC.app/Contents/MacOS/lib"
        ]
        for ruta in posibles:
            if os.path.exists(os.path.join(ruta, "libvlc.dll")) or \
               os.path.exists(os.path.join(ruta, "libvlc.dylib")) or \
               os.path.exists(os.path.join(ruta, "libvlc.so")):
                vlc_path = ruta
                break

    if not vlc_path or not os.path.exists(vlc_path):
        sg.popup_error(f"No se pudo encontrar VLC. Ajusta 'vlc_path' en {CONFIG_FILE}")
        raise SystemExit

    # Comprobar que contiene libvlc
    if not any(os.path.exists(os.path.join(vlc_path, lib))
               for lib in ("libvlc.dll", "libvlc.dylib", "libvlc.so")):
        sg.popup_error(f"La ruta '{vlc_path}' no contiene libvlc.")
        raise SystemExit

    # Añadir carpeta al PATH del proceso (Windows) o LD_LIBRARY_PATH/DYLD (Linux/Mac)
    if platform.system() == "Windows":
        os.environ["PATH"] = vlc_path + os.pathsep + os.environ.get("PATH", "")
        if hasattr(os, "add_dll_directory"):
            os.add_dll_directory(vlc_path)
    else:
        # En Unix/Mac, añadir a variables de librería
        lib_env = "LD_LIBRARY_PATH" if platform.system() == "Linux" else "DYLD_LIBRARY_PATH"
        os.environ[lib_env] = vlc_path + os.pathsep + os.environ.get(lib_env, "")

    return config, vlc_path
