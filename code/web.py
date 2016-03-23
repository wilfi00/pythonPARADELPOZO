from bottle import route, run, template, error, response
from Recherche import *
from json import dumps

@error(404)
def error404(error):
    return '<img style="position: absolute; left: 50%; top: 50%; margin-left: -285px; margin-top: -190px;" alt="Page Not Found (404)." src="https://css-tricks.com/images/404.jpg">'

@route('/equByDep/?<dep>')
def index(dep):
    search = Recherche()
    result = search.sportEqResearchByDep(dep)
    ret = []
    for r in result :
        ret.append(r.toJSON())
    response.content_type = 'application/json'
    return dumps(ret)



@route('/actByCom/<com>')
def index(com):
    search = Recherche()
    result = search.activiteRechercheByCom(com)
    ret = []
    for r in result :
        ret.append(r.toJSON())
    response.content_type = 'application/json'
    return dumps(ret)

run(host='localhost', port=8080)
