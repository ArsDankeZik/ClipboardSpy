#!/bin/bash

# Variables
PROJECT_DIR="$(pwd)"
TAR_NAME="ClipboardSpy.tar.gz"
PARENT_DIR="$(dirname "$PROJECT_DIR")"
ARCHIVE_PATH="$PARENT_DIR/$TAR_NAME"
MANIFEST_NAME="com.example.ClipboardSpy.json"

# Comprimir el proyecto un nivel arriba del directorio del proyecto
echo "Compressing project directory into $TAR_NAME..."
tar -czf "$ARCHIVE_PATH" -C "$PROJECT_DIR" .

# Calcular el hash SHA256
echo "Calculating SHA256 hash..."
SHA256_HASH=$(sha256sum "$ARCHIVE_PATH" | awk '{print $1}')
echo "SHA256 hash: $SHA256_HASH"

# Actualizar el archivo de manifiesto
echo "Updating Flatpak manifest with new archive path and SHA256 hash..."
cat > "$PROJECT_DIR/$MANIFEST_NAME" <<EOF
{
  "app-id": "com.example.ClipboardSpy",
  "runtime": "org.gnome.Platform",
  "runtime-version": "45",
  "sdk": "org.gnome.Sdk",
  "command": "clipboardspy",
  "finish-args": [
    "--share=ipc",
    "--socket=fallback-x11",
    "--talk-name=org.freedesktop.DBus",
    "--socket=session-bus",
    "--socket=wayland",
    "--device=dri",
    "--share=network",
    "--filesystem=xdg-documents"
  ],
  "modules": [
    {
      "name": "clipboardspy",
      "buildsystem": "simple",
      "build-commands": [
        "pip3 install . --prefix=/app"
      ],
      "sources": [
        {
          "type": "archive",
          "url": "file://$ARCHIVE_PATH",
          "sha256": "$SHA256_HASH"
        }
      ]
    }
  ]
}
EOF

# Construir y empaquetar la aplicación con Flatpak
echo "Building Flatpak package..."
flatpak-builder --force-clean build-dir "$PROJECT_DIR/$MANIFEST_NAME"

# Instalar la aplicación localmente
echo "Installing Flatpak package locally..."
flatpak-builder --user --install build-dir "$PROJECT_DIR/$MANIFEST_NAME"

# Limpiar archivos temporales
echo "Cleaning up..."
rm -rf build-dir

echo "Done! You can now run your application with 'flatpak run com.example.ClipboardSpy'"
