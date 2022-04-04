from time import sleep
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
    sleep(0.5)

#expression_triste()








print.upper('              jaime manger le "carrée" de sable            ')