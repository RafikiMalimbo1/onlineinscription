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

    def validate_emailEtu(self, emailEtu):
        print('Nous sommes dans methode email')
        user = Etudiant.query.filter_by(emailEtu=emailEtu.data).first()
        if user:

            print('Nous sommes dans erreur email')
            raise ValidationError(
                'Ce email est deja pris. Pardon met un autre')

    def validate_telEtu(self, telEtu):
        user = Etudiant.query.filter_by(telEtu=telEtu.data).first()
        if user:
            raise ValidationError(
                'Ce numero est deja pris. Pardon choisi un autre')

    def validate_sexeEtu(self, sexeEtu):
        print('Nous sommes dans methode')
        sexeEtu = sexeEtu.data
        if sexeEtu != 'F' or sexeEtu != 'M':
            print('Nous sommes dans erreur')
            raise ValidationError(
                'Le sexe doit etre Masculin ou Feminin. Pardon choisi entre M et F')

    def __repr__(self):
        return f"Etudiant('{self.nomEtu} {self.postNomEtu} {self.prenomEtu}' '{self.emailEtu}' )"


class Formation(db.Model):
    idFormat = db.Column(db.Integer, primary_key=True)
    intituleFormat = db.Column(db.String(300), nullable=True)
    dateDebutFormat = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, unique=False)
    dateFinFormat = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, unique=False)
    inscri = db.relationship('Inscription', backref='authorForm', lazy=True)

    def __repr__(self):
        return f"Formation('{self.intitule_format}' '{self.dateDebut_format }' '{self.dateFin_format}' )"


class Annee(db.Model):
    idAnnee = db.Column(db.DateTime, primary_key=True,
                        autoincrement=False, unique=False)
    inscri = db.relationship('Inscription', backref='authorAnnee', lazy=True)

    def __repr__(self):
        return f"Annee('{self.id_annee}')"


class Inscription(db.Model):
    idInsc = db.Column(db.Integer, primary_key=True)
    montantInsc = db.Column(db.Integer, nullable=False, unique=False)
    EtuidFk = db.Column(db.Integer, db.ForeignKey(
        'etudiant.idEtu'), nullable=False, unique=False)
    formatIdFk = db.Column(db.Integer, db.ForeignKey(
        'formation.idFormat'), nullable=False, unique=False)
    anneeIdFk = db.Column(db.DateTime, db.ForeignKey(
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
