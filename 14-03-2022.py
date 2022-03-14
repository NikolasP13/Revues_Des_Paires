#Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), 
# son poids(en kg). Retournez ensuite la catégorie dans laquelle se trouve la personne.

from cgi import print_form

#defintiion de fonction pour imc
def imc_u():
    poids = float(input('entrez votre poids en kg :'))
    grandeur = float(input('entrez votre grandeur en metre:'))
    imc_personne = (poids / (grandeur)**2)
    if (imc_personne < 18.5) :
        imc_categorie = "poids insuffisant"

    elif 18.5 <= imc_personne  < 25:
        imc_categorie = "poids normal"

    elif 25 <= imc_personne < 30 :
        imc_categorie = "Excès de poids"

    elif 30 <= imc_personne < 35 :
        imc_categorie = "Obeisté, classe I"

    elif 35 <= imc_personne < 40 :
        imc_categorie = "Obeisté, classe II"

    elif imc_personne >= 40 :
        imc_categorie = "Obeisté, classe III"
    return imc_categorie

imc_categorie = imc_u()

print(f" votre catégorie d'IMC : {imc_categorie} ")