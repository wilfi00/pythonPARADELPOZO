import sqlite3
import json
from unidecode import unidecode

conn = sqlite3.connect("data.db")
c = conn.cursor()



with open('installations.json') as jsonF :
    data = json.load(jsonF)

    for ind in range(len(data)):
        req = "insert into installation values("
        for i in range(1,30) :
            req += "'" + unidecode(data[ind]["FIELD"+str(i)]) + "',"
        req = req[:-1] + ");"
        print(req)
        c.execute(req)
