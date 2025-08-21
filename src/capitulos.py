import os
import json
import subprocess

TEMP_DIR = 'temp'
OUTPUT_DIR = 'output'
TEMP_TXT = os.path.join(TEMP_DIR, 'chapters.txt')

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extraer(video):
    result = subprocess.run(
        ['ffprobe','-i',video,'-print_format','json','-show_chapters','-loglevel','error'],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout) if result.stdout else {"chapters":[]}
    return [
        [i, ch.get('start_time','0'), ch.get('end_time','0'),
         ch.get('tags',{}).get('title','')]
        for i, ch in enumerate(data.get('chapters',[]))
    ]

def guardar_txt(capitulos):
    with open(TEMP_TXT,'w',encoding='utf-8') as f:
        f.write(";FFMETADATA1\n")
        for i,start,end,title in capitulos:
            f.write("[CHAPTER]\nTIMEBASE=1/1000\n")
            f.write(f"START={int(float(start)*1000)}\n")
            f.write(f"END={int(float(end)*1000)}\n")
            f.write(f"title={title.strip()}\n")

def crear_copia_sin(video, salida):
    subprocess.call(['ffmpeg','-y','-i',video,
                     '-map_metadata','-1','-map_chapters','-1',
                     '-codec','copy',salida])

def aplicar(video_sin, salida_final):
    subprocess.call(['ffmpeg','-y','-i',video_sin,'-i',TEMP_TXT,
                     '-map_metadata','1','-map_chapters','1',
                     '-codec','copy',salida_final])
