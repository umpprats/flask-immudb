from datetime import datetime
from flask import jsonify, Blueprint
from app.models import Auditable
from app.repositories import AuditableRepository

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    auditable = Auditable(2,datetime.now().timestamp(),'pprats','test1.txt', '12345678901')

    rep = AuditableRepository()
    x=rep.create(auditable)
    print(x)
    resp = jsonify("OK")
    resp.status_code = 200
    return resp

@home.route('/update', methods=['GET'])
def update():
    auditable = Auditable(2,datetime.now().timestamp(),'pabloprats','test2.txt', '12345678901')

    rep = AuditableRepository()
    #x=rep.create(auditable)
    x=rep.upsert(auditable)
    resp = jsonify("OK")
    resp.status_code = 200
    return resp


