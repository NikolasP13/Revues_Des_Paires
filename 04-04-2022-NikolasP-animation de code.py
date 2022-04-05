from time import sleep
import sys
import os

#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke (ou exemple donner par toi)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def expression_triste():
    
    for frame in range(4):
        cls()
        bouche = 'O'
        yeux = '^'
        if frame == 1 :
            bouche = '-'
            yeux = '-'
        elif frame == 2 :
            bouche = '--'
            yeux = 'v'
        elif frame == 3 :
            bouche = '⁀'
            yeux = 'V'
        print("""    
          ___________       
          |  ^   ^  |      
          |    u    |      
          |         |      
          |    O    |      
          TTTTTTTTTTT      """ )
        
        print(f"""    
          ___________       
          |  {yeux}   {yeux}  |      
          |    u    |      
          |         |      
          |    {bouche}    |      
          TTTTTTTTTTT      """ )
        sleep(1)

#expression_triste()


#typewriter style animated text (tutoriel) url : https://www.youtube.com/watch?v=2h8e0tXHfk0
# user : learn learn scratch tutorial

def imprimer_braille():
    message = """           
          ____  
        o8%8888,    
      o88%8888888.  
     8'-    -:8888b   
    8'         8888  
   d8.-=. ,==-.:888b  
   >8 `~` :`~' d8888   
   88         ,88888   
   88b. `-~  ':88888  
   888b ~==~ .:88888 
   88888o--:':::8888      
   `88888| :::' 8888b  
   8888^^'       8888b  
  d888           ,%888b.   
 d88%            %%%8--'-.  
/88:.__ ,       _%-' ---  -  
    '''::===..-'   =  --.
    LA MONA LISA !!!!!!!! """ 
    for charactere in message:
        sys.stdout.write(charactere)
        sys.stdout.flush()
        sleep(0.01)

#imprimer_braille()

#terminal loading bar in python (url):https://www.youtube.com/watch?v=MtYOrIwW1FQ
#user : tyler Luedtke

def bar_chargement(iteration, total, prefix='', suffix='', decimals=1, lenght = 100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLenght = int(lenght * iteration // total)
    bar = fill * filledLenght + '-' * (lenght - filledLenght)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total :
        print()

items = list(range(0,50))
l = len(items)

bar_chargement(0, l, prefix='Progress', suffix='Complete', lenght=l)
for i, items in enumerate(items):
    sleep(0.1)
    bar_chargement(i + 1, l, prefix='Progress', suffix='Complete', lenght=l)




