import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
from gi.repository import Gtk, Gdk, GLib, Gio # type: ignore

class ClipboardApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.GtkClipboardSpy")
        self.clipboard_history = []

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("Clipboard Spy")
        window.set_default_size(500, 400)
        
        self.clipboard = Gdk.Display.get_default().get_clipboard()

        # Crear un ListStore para mantener los elementos del portapapeles
        self.liststore = Gtk.ListStore(str, str)  # Almacenar tanto la vista previa como el contenido completo

        # Crear un TreeView para mostrar los elementos del portapapeles
        self.treeview = Gtk.TreeView(model=self.liststore)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(title="History", cell_renderer=renderer, text=0)
        self.treeview.append_column(column)

        # Configurar el tooltip para mostrar el contenido completo al pasar el mouse
        self.treeview.set_tooltip_column(1)

        # Conectar la señal de clic en la fila
        self.treeview.connect("row-activated", self.on_row_activated)

        # Crear un contenedor y añadir el TreeView
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_child(self.treeview)
        window.set_child(scrolled_window)

        # Configurar un temporizador para verificar el contenido del portapapeles
        GLib.timeout_add(1000, self.check_clipboard)

        window.present()

    def check_clipboard(self):
        """Verificar el contenido del portapapeles y actualizar la lista si es nuevo."""
        self.clipboard.read_text_async(None, self.on_text_received)
        return True  # Continuar ejecutando el temporizador

    def on_text_received(self, clipboard, result):
        """Callback para manejar el texto recibido del portapapeles."""
        content = clipboard.read_text_finish(result)
        if content and (not self.clipboard_history or content != self.clipboard_history[-1]):
            self.clipboard_history.append(content)
            preview = content.splitlines()[0]  # Obtener la primera línea del texto como vista previa
            self.liststore.append([preview, content])

    def on_row_activated(self, treeview, path, column):
        """Copiar el contenido completo seleccionado al portapapeles."""
        model = treeview.get_model()
        treeiter = model.get_iter(path)
        full_content = model[path][1]  # Obtener el contenido completo
        #self.clipboard.set_text(full_content)
        # Crear un Gdk.ContentProvider para el texto
        content_provider = Gdk.ContentProvider.new_for_value(full_content)
        self.clipboard.set_content(content_provider)

def main():
    app = ClipboardApp()
    app.run(None)

if __name__ == "__main__":
    main()
