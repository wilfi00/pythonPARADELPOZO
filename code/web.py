from bottle import route, run, template, error
from Recherche import *

@error(404)
def error404(error):
    return '<img style="position: absolute; left: 50%; top: 50%; margin-left: -285px; margin-top: -190px;" alt="Page Not Found (404)." src="https://css-tricks.com/images/404.jpg">'

@route('/equByDep/<dep>')
def index(dep):
    search = Recherche()
    result = search.sportEqResearchByDep(dep)
    str = '<body style="font-family:Arial">'
    for r in result :
        str += "<p>{}</p>".format(r.__str__())
    str += '</body>'
    return str

@route('/actByCom/<com>')
def index(com):
    search = Recherche()
    result = search.activiteRechercheByCom(com)
    str = '<body style="font-family:Arial">'
    for r in result :
        str += "<p>{}</p>".format(r.__str__())
    str += '</body>'
    return str

run(host='localhost', port=8080)
