def calcul_imc(): 
    grandeur_en_metre = float(input("Entrez votre grandeur en metre : "))
    poids_en_kg = float(input("Entrez votre poids en kilogramme : "))

    imc = poids_en_kg / (grandeur_en_metre)**2
    msg = ""
    if imc < 18.5:
        msg = "Poids insuffisant"
    elif 18.5 <= imc < 25 :
        msg = "Poids santé"
    elif 25 <=  imc < 30 :
        msg = "Excès de poids"
    elif 30 <= imc < 999  :
        msg = "Obèse"
    return msg

msg = calcul_imc()

print(f"Vous êtes dans la catégorie d'IMC suivante : {msg}. ")

