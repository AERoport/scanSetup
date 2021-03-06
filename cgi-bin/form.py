#!/usr/bin/env python3
import cgi
import html


# Для корректной русской кодировки
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#

import scanMFP

form = cgi.FieldStorage()
host = html.escape(form.getfirst("host", "не задано"))
comp = html.escape(form.getfirst("comp", "не задано"))
folder = html.escape(form.getfirst("folder", "не задано"))
displayname = html.escape(form.getfirst("displayname", "не задано"))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Настройка сканирования</title>
        </head>
        <body>""")

print("<h1>Добавление сканера</h1>")
print("<p>Host: {}</p>".format(host))
print("<p>Компьютер: {}</p>".format(comp))
print("<p>Папка: {}</p>".format(folder))
print("<p>Отображаемое имя: {}</p>".format(displayname))

folderName = '\\\\' + comp + '\\' + folder
r = scanMFP.addScanToMFP(hostMFP = host, folderName = folderName, displayName = displayName)
print("<div> " + r + '</div>')

print("""</body>
        </html>""")
