import sqlite3
import os
import sys

conn = sqlite3.connect('data.db')
c = conn.cursor()

def sportEqResearch(eq):
    req = "select * from equipement where EquNom = '" + eq + "';"
    c.execute(req)
    print (c.fetchone())

os.system('clear')
choice = ""
while choice != exit:
    eq = input("What's the name of the equipement sportif that you want to find ? \n")
    sportEqResearch(eq)
    if eq == "exit":
        os.system('clear')
        sys.exit(0)
