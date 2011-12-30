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
		
		url_region = self.view.find('(?<=' + LocationCode + ').*$', 0)
		
		if url_region:
			url = self.view.substr(url_region).strip()
			sublime.status_message(LocationURL + '/' + url)
			webbrowser.open_new(LocationURL + '/' + url)
		else:
			sublime.status_message("Location not set")