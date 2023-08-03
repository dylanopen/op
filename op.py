import os, sys
import requests

args = sys.argv

if args[1] == "i":
	app = requests.get("https://github.com/dylanopen/op/raw/main/core/" + args[2]).content.decode("utf-8")
	with open("/usr/bin/" + args[2], "w") as f:
		f.write(app)
