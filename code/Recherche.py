class Recherche :
""" Classe qui effectue des recherches en utilisant les objets Activités et Equipements """

    def activiteRecherche():

    def sportEqResearch(eq, numLib):
        if numLib == 0:
            req = "select ComLib, EquNom from equipement where EquNom like '%" + eq + "%';"
        else:
            req = "select ComLib, EquNom from equipement where EquNom like '%" + eq + "%' and ComInsee like '" + str(numLib) + "%';"
        c.execute(req)
        row = c.fetchone()
        while row is not None:
            print(row)
            row = c.fetchone()
