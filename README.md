# Editor de Capítulos MP4

Una herramienta de escritorio para extraer, editar y gestionar los capítulos de un archivo de vídeo MP4. Construida con FreeSimpleGUI, VLC y FFmpeg/FFprobe.

## Características

* **Extracción de Capítulos:** Lee automáticamente los metadatos de capítulos de un archivo MP4.

* **Reproductor de Vídeo:** Reproduce el vídeo directamente en la interfaz de la aplicación, mostrando el progreso y el tiempo actual.

* **Edición de Capítulos:**

  * Añade nuevos capítulos.

  * Edita el tiempo de inicio, el tiempo de fin y el título de los capítulos existentes.

  * Elimina capítulos de la lista.

* **Integración con Herramientas:** Utiliza FFprobe para la extracción y FFmpeg para la aplicación de los cambios a un nuevo archivo de vídeo.

* **Interfaz Sencilla:** Una GUI intuitiva que combina el reproductor de vídeo con la tabla de capítulos.

## Requisitos

* Python 3.x

* FreeSimpleGUI

* Python-VLC

* VLC Media Player

* FFmpeg y FFprobe (deben estar instalados y accesibles desde la línea de comandos)

## Estructura del Proyecto

* `app.py`: El punto de entrada principal de la aplicación.

* `src/`: Directorio que contiene los módulos de la aplicación.

  * `capitulos.py`: Funciones para extraer y guardar los datos de los capítulos.

  * `config_app.py`: Gestiona la configuración de la aplicación y la ruta de VLC.

  * `dialogos.py`: Contiene las ventanas de diálogo para la edición y adición de capítulos.

  * `eventos.py`: Manejador de eventos para la ventana principal.

  * `layouts.py`: Define el diseño de la interfaz de usuario.

  * `reproductor.py`: Funciones para incrustar y controlar el reproductor VLC.

  * `tabla.py`: Componente para la tabla de capítulos.

  * `utilidades.py`: Funciones de ayuda como la selección de archivos y la limpieza de directorios temporales.

  * `validacion.py`: Valida la entrada de datos en los formularios de edición.

## Uso

1. **Configuración:** Asegúrate de tener `config.json` en el mismo directorio que `app.py`. En este archivo, puedes especificar la ruta a tu instalación de VLC si la detección automática falla.

   ```
   {
     "vlc_path": ""
   }
   
   ```

2. **Ejecutar:**

   ```
   python app.py
   
   ```

3. **Seleccionar vídeo:** Al iniciar, se te pedirá que selecciones un archivo de vídeo MP4.

4. **Gestionar capítulos:** Utiliza los botones en el panel derecho para `Añadir`, `Editar` o `Eliminar` capítulos.

5. **Guardar:** Una vez que hayas terminado de editar, haz clic en `Guardar y aplicar cambios`. Esto creará una copia del vídeo original en el directorio `output/` con los nuevos capítulos aplicados.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](./LICENSE) en el repositorio.
