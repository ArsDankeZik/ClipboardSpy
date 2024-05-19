#!/bin/bash

set -e

# Configurar y construir el proyecto usando Meson y Ninja
meson setup builddir || meson setup --reconfigure builddir
ninja -C builddir

# Ejecutar el script de instalación
sudo python3 install_script.py

# Crear el directorio de aplicaciones de usuario si no existe
mkdir -p ~/.local/share/applications/

# Copiar el archivo .desktop al directorio de aplicaciones de usuario
cp ClipboardSpy.desktop ~/.local/share/applications/

update-desktop-database ~/.local/share/applications/

echo "La instalación de ClipboardSpy se ha completado exitosamente."
echo "La aplicación debería aparecer en el menú del sistema."
