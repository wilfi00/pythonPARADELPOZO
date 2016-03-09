import sqlite3
import json


conn = sqlite3.connect("data.db")
c = conn.cursor()



with open('json/installations.json') as jsonF :
    data = json.load(jsonF)

    for ind in range(len(data)):
        req = "insert into installation values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
        lst = []
        for i in range(1,30) :
            lst.append(data[ind]["FIELD"+str(i)])
        c.execute(req,lst)
    conn.commit()
c.close()
