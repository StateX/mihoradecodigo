import re
import urllib

web =  raw_input("pega aqui la Url: ")
url = []
patron= re.compile('''href=["'](.[^"']+)["']''')
busqueda = re.findall(patron, urllib.urlopen(web).read())
for i in busqueda:
	 url.append(i)
	 d1 =  str(i)
	 ListaUrl = open('url.txt','a+')
	 ListaUrl.write("--> "+ d1 +" <--")
	 ListaUrl.close()
	 busqueda2 = re.findall(patron, urllib.urlopen(i).read())
	 for e in busqueda2:
	 	 url.append(e)
	 	 d2 =  str(e)
	 	 ListaUrl = open('url.txt','a+')
	 	 ListaUrl.write("--> "+ d2 +" <--")
	 	 ListaUrl.close()
print "URls Guardadas con Exito."