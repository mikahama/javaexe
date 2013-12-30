#-*- coding: UTF-8 -*-
import webbrowser
import sys

def quit(obj):
	obj.kWindow.destroy()
	sys.exit(0)

def download(obj):
	webbrowser.open('http://java.com/getjava/')
	quit(obj)
