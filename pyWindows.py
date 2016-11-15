#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject

class NewInfoWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title='title')
		self.set_size_request(200,100)

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)

		urlHBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 8)
		usernameHBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 8)
		passwordHBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 8)
		noteHBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 8)
		
		self.urlLabel = Gtk.Label("URL : ")
		self.urlLabel.set_justify(Gtk.Justification.LEFT)
		self.usernameLabel = Gtk.Label("Username : ")
		self.passwordLabel = Gtk.Label("Password : ")
		self.noteLabel = Gtk.Label("Additional Notes : ")

		self.urlField = Gtk.Entry()
		self.usernameField = Gtk.Entry()
		self.passwordField = Gtk.Entry()
		self.noteField = Gtk.TextView()
		self.noteField.set_wrap_mode(Gtk.WrapMode.WORD)
		self.noteField.set_size_request(-1, 150)

		urlHBox.pack_start(self.urlLabel, expand=True, fill=False, padding=5)
		urlHBox.pack_start(self.urlField, expand=True, fill=False, padding=5)

		usernameHBox.pack_start(self.usernameLabel, expand=True, fill=False,padding=5)
		usernameHBox.pack_start(self.usernameField, expand=True, fill=False,padding=5)

		self.toggleVisiblePassword = Gtk.CheckButton("Visible")
		self.toggleVisiblePassword.connect("toggled", self.on_visible_toggled)
		self.toggleVisiblePassword.set_active(True)

		passwordHBox.pack_start(self.passwordLabel, True, False, 0)
		passwordHBox.pack_start(self.passwordField, True, False, 0)
		passwordHBox.pack_start(self.toggleVisiblePassword, True, False, 0)

		noteHBox.pack_start(self.noteLabel, expand=True, fill=True, padding=0)
		noteHBox.pack_start(self.noteField, expand=True, fill=True, padding=0)

		vbox.pack_start(urlHBox, expand=True, fill=True, padding=0)
		vbox.pack_start(usernameHBox, expand=True, fill=True, padding=0)
		vbox.pack_start(passwordHBox, expand=True, fill=True, padding=0)
		vbox.pack_start(noteHBox, expand=True, fill=True, padding=0)

		buttonHBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		self.buttonCancel = Gtk.Button(label='Cancel')
		self.buttonCancel.connect("clicked", self.on_button_cancel_clicked)
		buttonHBox.pack_end(self.buttonCancel, True, True, 0)

		self.buttonSave = Gtk.Button(label='Save')
		self.buttonSave.connect("clicked", self.on_button_save_clicked)
		buttonHBox.pack_start(self.buttonSave, True, True, 0)

		vbox.pack_start(buttonHBox, True, True, 0)
		self.add(vbox)

	def on_visible_toggled(self, button):
		value = self.toggleVisiblePassword.get_active()
		self.passwordField.set_visibility(value)

	def on_button_cancel_clicked(self,widget):
		self.destroy()

	def on_button_save_clicked(self,widget):
		return True

class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Entry Demo")
		self.set_size_request(200, 100)

		self.timeout_id = None

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)

		self.entry = Gtk.Entry()
		self.entry.set_text("Hello World")
		vbox.pack_start(self.entry, True, True, 0)

		hbox = Gtk.Box(spacing=6)
		vbox.pack_start(hbox, True, True, 0)

		self.toggleVisiblePassword = Gtk.CheckButton("Visible")
		self.toggleVisiblePassword.connect("toggled", self.on_visible_toggled)
		self.toggleVisiblePassword.set_active(True)
		hbox.pack_start(self.toggleVisiblePassword, True, True, 0)


	def on_editable_toggled(self, button):
		value = button.get_active()
		self.entry.set_editable(value)

	def on_visible_toggled(self, button):
		value = button.get_active()
		self.entry.set_visibility(value)


if __name__ == '__main__':
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()

	win2 = NewInfoWindow()
	win2.connect("delete-event", Gtk.main_quit)
	win2.show_all()
	Gtk.main()