from inscriptionFormation import db
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import datetime
# from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(formaterIdFk):
#     return Etudiant.query.get(int(formaterIdFk))


class Etudiant(db.Model):
    idEtu = db.Column(db.Integer, primary_key=True)
    nomEtu = db.Column(db.String(25), nullable=False, unique=False)
    postNomEtu = db.Column(db.String(30), nullable=False, unique=False)
    prenomEtu = db.Column(db.String(30), nullable=False, unique=False)
    sexeEtu = db.Column(db.String(30), nullable=False, unique=False)
    adressEtu = db.Column(db.String(1), nullable=False, unique=False)
    telEtu = db.Column(db.String(15), unique=True, nullable=False)
    emailEtu = db.Column(db.String(120), unique=True, nullable=False)
    inscri = db.relationship('Inscription', backref='authorEtut', lazy=True)

    def __repr__(self):
        return f"Etudiant('{self.nomEtu} {self.postNomEtu} {self.prenomEtu}' '{self.emailEtu}' )"


class Formation(db.Model):
    idFormat = db.Column(db.Integer, primary_key=True)
    intituleFormat = db.Column(db.String(300), nullable=True)
    dateDebutFormat = db.Column(
        db.Date, nullable=False, default=datetime.utcnow(), unique=False)
    dateFinFormat = db.Column(
        db.Date, nullable=False, default=datetime.utcnow(), unique=False)
    inscri = db.relationship('Inscription', backref='authorForm', lazy=True)

    def __repr__(self):
        return f"Formation('{self.intituleFormat}' '{self.dateDebutFormat }' '{self.dateFinFormat}' )"


class Annee(db.Model):
    idAnnee = db.Column(db.String(4), primary_key=True,
                        autoincrement=False, unique=False)
    inscri = db.relationship('Inscription', backref='authorAnnee', lazy=True)

    def __repr__(self):
        return f"Annee('{self.idAnnee}')"


class Inscription(db.Model):
    idInsc = db.Column(db.Integer, primary_key=True)
    montantInsc = db.Column(db.Integer, nullable=False, unique=False)
    EtuidFk = db.Column(db.Integer, db.ForeignKey(
        'etudiant.idEtu'), nullable=False, unique=False)
    formatIdFk = db.Column(db.Integer, db.ForeignKey(
        'formation.idFormat'), nullable=False, unique=False)
    anneeIdFk = db.Column(db.String(4), db.ForeignKey(
        'annee.idAnnee'), nullable=False, unique=False)
    paie = db.relationship('Paiement', backref='authorPaiement', lazy=True)

    def __repr__(self):
        return f"Inscription('{self.montantInsc}')"


class Paiement(db.Model):
    idPaie = db.Column(db.Integer, primary_key=True)
    montantPaie = db.Column(db.Integer, unique=False)
    typePaie = db.Column(db.String(400), nullable=False, unique=False)
    inscriptionIdFk = db.Column(
        db.Integer, db.ForeignKey('inscription.idInsc'), nullable=False, unique=False)
