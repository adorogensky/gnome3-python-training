#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window()
window.set_title("Hello World")
window.connect("destroy", Gtk.main_quit)
window.show()
Gtk.main()
