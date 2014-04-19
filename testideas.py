from datetime import * 
ideas = []
while True:
	 recogedor = open('banco_ideas.txt','a+')
	 for item in recogedor:
	 	 ideas.append(item)	 
	 print "estas son las ideas que ha recogido hasta ahora."
	 print ideas
	 idea = raw_input("Que se le ha ocurrido?:  ")
	 ideas.append(idea)
	 ideas.append(date.today())
	 print ideas
	 d1 = raw_input("ajunto otra idea senor?: ") 
	 if d1 == "s":
	 	print idea
	 elif d1 == "n":
	 	 i = str(ideas)
	 	 banco_ideas = open('banco_ideas.txt','a+')
	 	 print ideas
		 banco_ideas.write(i)
		 banco_ideas.close()
		 print "ideas guardadas con exito"
		 raw_input("ENTER para salir: ")
	 	 break
	 else: 
	 	 print "seleciones una de las 2 senor"	