# ClipboardSpy

ClipboardSpy es una aplicación de monitoreo del portapapeles utilizando GTK4. Esta aplicación permite rastrear el historial del portapapeles y proporciona una interfaz gráfica para ver y gestionar el contenido copiado.

## Características

- Monitoreo del portapapeles en tiempo real.
- Historial del portapapeles con vista previa.
- Interfaz gráfica intuitiva utilizando GTK4.

## Instalación

### Instalación Normal

#### Requisitos Previos

- Python 3.6 o superior.
- PyGObject.

#### Instrucciones de Instalación

1. Clona este repositorio:

    ```sh
    git clone https://github.com/tu_usuario/ClipboardSpy.git
    cd ClipboardSpy
    ```

2. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

3. Ejecuta la aplicación:

    ```sh
    python src/clipboardspy.py
    ```

### Instalación con Flatpak

#### Requisitos Previos

- Flatpak y Flatpak-builder instalados en tu sistema.

#### Instrucciones de Instalación

1. Construir el paquete Flatpak:

    ```sh
    flatpak-builder --force-clean build-dir com.example.ClipboardSpy.json
    ```

2. Instalar el paquete localmente:

    ```sh
    flatpak-builder --user --install build-dir com.example.ClipboardSpy.json
    ```

3. Ejecutar la aplicación:

    ```sh
    flatpak run com.example.ClipboardSpy
    ```

## Licencia

Este proyecto está licenciado bajo la Licencia Pública General de GNU v3.0. Para más detalles, consulta el archivo [LICENSE](LICENSE).

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas forkear el proyecto y modificar su desarrollo, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Empuja tus cambios a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre una Pull Request.

## Autor

Richardo G. Cibea - [richardo.gabriel.cibea@gmail.com](mailto:richardo.gabriel.cibea@gmail.com)
