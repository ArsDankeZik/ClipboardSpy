project('ClipboardSpy',
  version: '0.1.0',
  default_options: ['warning_level=3'])

py3 = import('python').find_installation('python3')

project_root = meson.current_source_dir()
install_prefix = get_option('prefix')
build_root = meson.current_build_dir()

install_subdir('src', install_dir: install_prefix / 'lib' / 'ClipboardSpy')
install_data('assets/logo.ico', install_dir: install_prefix / 'share' / 'ClipboardSpy' / 'assets')

# Copiar el script de instalación al directorio de construcción
install_script = configure_file(
  input: 'install_script.py',
  output: 'install_script.py',
  copy: true
)

# Ejecutar el script de instalación desde el directorio de construcción
meson.add_install_script(py3, build_root / 'install_script.py', project_root, install_prefix)
