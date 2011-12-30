#	Key Binding
#	[
#		{ "keys": ["super+shift+m"], "command": "open_and_view" }
#	]

import sublime, sublime_plugin
import webbrowser

LocationCode = "//LOCATION:"
LocationURL = "http://localhost:8888"

class OpenAndViewCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for i in range(1, 10):
			LocationLine = self.view.substr(self.view.word(self.view.line(i)))
			if LocationLine.find(LocationCode) == -1:
				sublime.status_message("Location not set")
			else:
				url = LocationLine.replace(LocationCode,'').strip()
				webbrowser.open_new(LocationURL + url)
				sublime.status_message(LocationURL + url)
				break