from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Produs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume_produs = db.Column(db.String(250))
    cod_produs = db.Column(db.String(250)) 
    cantitate_produs = db.Column(db.Integer)
    pret_achizitie_produs = db.Column(db.Float)
    moneda_achizitie = db.Column(db.String(250))
    pret_vanzare_produs = db.Column(db.Float)
    moneda_vanzare = db.Column(db.String(250))
    nir_id= db.Column(db.Integer, db.ForeignKey('nir.id'))
    adaos_valoric_unitar = db.Column(db.Float,default=0)
    adaos_valoric_total = db.Column(db.Float,default=0)
    adaos_procentual = db.Column(db.Float, default = 0)
    pret_achizitie_produs_total = db.Column(db.Float, default = 0)
    pret_vanzare_produs_total = db.Column(db.Float, default = 0)

class Nir(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nume_firma = db.Column(db.String(250))
    nume_furnizor = db.Column(db.String(250))
    numar_factura = db.Column(db.String(250))
    nume_membri = db.Column(db.String(250))
    nume_gestionar = db.Column(db.String(250))
    cost_transport = db.Column(db.Float)
    moneda_transport = db.Column(db.String(250))
    taxe_tva = db.Column(db.Float)
    moneda_taxe_tva = db.Column(db.String(250))
    data_factura = db.Column(db.String(250))
    date = db.Column(db.DateTime(timezone= True), default=func.now())
    xlsx = db.Column(db.LargeBinary)
    produse = db.relationship('Produs')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    nirs = db.relationship('Nir')
    
