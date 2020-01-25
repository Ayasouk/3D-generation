import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Whatsup World")
		self.nb_tomato = 0
		self.nb_tuna = 0
		# Box
		self.box = Gtk.Box(spacing=10)
		self.add(self.box)

		# Tomato Button
		self.tomato_button = Gtk.Button(label="Add tomato")
		self.tomato_button.connect("clicked", self.tomato_clicked)
		self.box.pack_start(self.tomato_button, True, True, 0)

		# Tuna button
		self.tuna_button = Gtk.Button(label="Add Tuna")
		self.tuna_button.connect("clicked", self.tuna_clicked)
		self.box.pack_start(self.tuna_button,True, True, 0)

	def tomato_clicked(self, widget):
		self.nb_tomato+=1
		print("tomato added")
		print("there is ",self.nb_tomato, " added")

	def tuna_clicked(self, widget):
		self.nb_tuna+=1
		print("tuna added")
		print("there is ",self.nb_tuna, " added")

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
