#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import html
# Для корректной русской кодировки
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#
#from urlparse import urlparse

#import scanMFP

form = cgi.FieldStorage()

host = html.escape(form.getfirst("host", "не задано"))
comp = html.escape(form.getfirst("comp", "не задано"))
folder = html.escape(form.getfirst("folder", "не задано"))
displayName = html.escape(form.getfirst("displayname", "не задано"))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Настройка сканирования</title>
        </head>
        <body>""")

print("<h1>Добавление сканера</h1>")
print("<form action='/cgi-bin/form.py'>")

print(f"<div>МФУ: <input type='text'value = '{host}'></div>")
print(f"<div>Компьютер:<input type='text' value='{comp}'></div>")
print(f"<div>Папка: <input type='text' value='scan'></div>")
print(f"<div>Имя сотрдуника: <input type = 'text' value='{displayName}'></div>")
print('<input type="submit" value="Добавить">')

print("</form>")
print("""</body>
        </html>""")
