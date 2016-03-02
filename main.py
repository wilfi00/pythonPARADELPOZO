import sqlite3
import os
import sys

conn = sqlite3.connect('data.db')
c = conn.cursor()

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

def sqlRequest(req):
    c.execute(req)
    row = c.fetchone()
    while row is not None:
        print(row)
        row = c.fetchone()

os.system('clear')
choice = ""
while choice != exit:
    choice = input("What do you want to do ? \n - req to find an equipement sportif \n - devMode to dev mode \n\n")
    if choice == "req":
        eq = input("What's the name of the equipement sportif that you want to find ? \n")
        numLib = input("Departement : (0 : all departements)\n")
        sportEqResearch(eq, int(numLib))
    elif choice == "devMode":
        req = input("Type your SQL select request : \n")
        sqlRequest(req)
    if choice == "exit":
        os.system('clear')
        sys.exit(0)
