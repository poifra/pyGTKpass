#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject

class NewInfoWindow():
	def __init__(self,title='New password'):
		Gtk.window.__init__(self, title=title)
		self.set_size_request(200,100)

		vbox = Gtk.Box(orientation=Gtk.orientation.VERTICAL, spacing = 6)
		hbox = Gtk.Box(orientation=Gtk.orientation.HORIZONTAL, spacing = 8)
		self.usernameField = Gtk.Entry()
		self.passwordField = Gtk.Entry()

		vbox.pack_start(hbox, expand=True, fill=True, 0)
		hbox.pack_start(self.username, expand=True, fill=True, 0)

		self.check_visible = Gtk.CheckButton("Visible")
		self.check_visible.connect("toggled", self.on_visible_toggled)
		self.check_visible.set_active(True)
		hbox.pack_start(self.check_visible, True, True, 0)

	def on_visible_toggled(self, button):
		value = check_visible.get_active()
		self.passwordField.set_visibility(value)


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

		self.check_visible = Gtk.CheckButton("Visible")
		self.check_visible.connect("toggled", self.on_visible_toggled)
		self.check_visible.set_active(True)
		hbox.pack_start(self.check_visible, True, True, 0)

		self.pulse = Gtk.CheckButton("Pulse")
		self.pulse.connect("toggled", self.on_pulse_toggled)
		self.pulse.set_active(False)
		hbox.pack_start(self.pulse, True, True, 0)

		self.icon = Gtk.CheckButton("Icon")
		self.icon.connect("toggled", self.on_icon_toggled)
		self.icon.set_active(False)
		hbox.pack_start(self.icon, True, True, 0)

	def on_editable_toggled(self, button):
		value = button.get_active()
		self.entry.set_editable(value)

	def on_visible_toggled(self, button):
		value = button.get_active()
		self.entry.set_visibility(value)

	def on_pulse_toggled(self, button):
		if button.get_active():
			self.entry.set_progress_pulse_step(0.2)
			# Call self.do_pulse every 100 ms
			self.timeout_id = GObject.timeout_add(100, self.do_pulse, None)
		else:
			# Don't call self.do_pulse anymore
			GObject.source_remove(self.timeout_id)
			self.timeout_id = None
			self.entry.set_progress_pulse_step(0)

	def do_pulse(self, user_data):
		self.entry.progress_pulse()
		return True

	def on_icon_toggled(self, button):
		if button.get_active():
			icon_name = "system-search-symbolic"
		else:
			icon_name = None
		self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY,
			icon_name)

if __name__ == '__main__':
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()