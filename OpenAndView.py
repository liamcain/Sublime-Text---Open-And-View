#	Simply add something like this to the top of each of your files.
#	//LOCATION: /controllerName/
#	When you hit Shift+Command+m this plugin will check the top 10 lines of the current file
#	look for the location tag and append it to the URL defined below
#	So in this example it will open http://localhost:8888/controllerName/
#	If the programming location used needs a different identifier for comments, simply change // to whatever.

#	Key Binding
#	[
#		{ "keys": ["super+shift+m"], "command": "open_and_view" }
#	]	

#	I use this code together with Code Igniter framework

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