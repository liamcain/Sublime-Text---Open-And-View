Simply add something like this to the top of each of your files.

//LOCATION: /controllerName/

When you hit Shift+Command+m this plugin will check the top 10 lines of the current file and look for the location tag and append it to the URL defined below
So in this example it will open http://localhost:8888/controllerName/ in your default browser.

So when your editing a view, controller or model you can define the actual URL and popup your changes right away.

If your programming language uses a different identifier for comments, simply change // to whatever. I have it setup for PHP.

Key Binding
[
	{ "keys": ["super+shift+m"], "command": "open_and_view" }
]	

I use this code together with Code Igniter framework

Emjoy,

Derek