#!/bin/bash

set -e

# Eliminar los archivos instalados
sudo rm -rf /usr/local/lib/ClipboardSpy
sudo rm -f /usr/local/bin/clipboardspy
sudo rm -rf build
sudo rm -rf builddir
sudo rm -rf ClipboardSpy.egg-info
sudo rm -rf .flatpak-builder


# Eliminar el archivo .desktop del directorio de aplicaciones de usuario
rm -f ~/.local/share/applications/ClipboardSpy.desktop

echo "ClipboardSpy se ha desinstalado exitosamente."
