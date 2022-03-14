#Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), 
# son poids(en kg). Retournez ensuite la catégorie dans laquelle se trouve la personne.

from cgi import print_form


def imc_u():
    poids = int(input('entrez votre poids en kg :'))
    grandeur = int(input('entrez votre grandeur en metre:'))
    imc_personne = (poids / (grandeur)**2)

imc_u()
if (imc_personne < 18.5) :
    imc_personne = str("poids insuffisant")
if (imc_personne >= 18.5 or < 25) :
    imc_personne = str("poids normal")
if (imc_personne >= 25 or < 30):
    imc_personne = str("Excès de poids")
if (imc_personne >= 30 or < 35):
    imc_personne = str("Obeisté, classe I")
if (imc_personne >= 35 or < 40) :
    imc_personne = str("Obeisté, classe II")
if (imc_personne >= 40) :
    imc_personne = str("Obeisté, classe III")
print(f" votre IMC : {imc_personne} ")
