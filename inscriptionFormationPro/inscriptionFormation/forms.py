from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from inscriptionFormation.models import Etudiant, Annee, Formation, Inscription
from datetime import datetime


class EnregistrementEtudiantForm(FlaskForm):
    # table etudiant
    nomEtu = StringField('Nom', validators=[
                         DataRequired(), Length(min=2, max=20)])
    postNomEtu = StringField('Post Nom', validators=[
        DataRequired(), Length(min=2, max=20)])
    prenomEtu = StringField('Prenom', validators=[
        DataRequired(), Length(min=2, max=20)])
    sexeEtu = StringField('Sexe', validators=[
        DataRequired(), Length(min=1, max=1)])
    adressEtu = StringField('Adress', validators=[
        DataRequired(), Length(min=2, max=20)])
    telEtu = StringField('Telephone', validators=[
        DataRequired(), Length(min=2, max=12)])
    emailEtu = StringField('Email', validators=[DataRequired(), Email()])
    intituleFormat = StringField('Titre de la formation', validators=[
                                 DataRequired(), Length(min=2, max=500)])

    idAnnee = StringField('Annee', validators=[DataRequired()])
    # table inscription
    montantInsc = StringField('Montant inscription',
                              validators=[DataRequired()])
    submit = SubmitField("S'inscire")

    def validate_emailEtu(self, emailEtu):
        user = Etudiant.query.filter_by(emailEtu=emailEtu.data).first()
        if user:
            raise ValidationError(
                'Ce email est deja pris. Pardon met un autre')

    def validate_telEtu(self, telEtu):
        user = Etudiant.query.filter_by(telEtu=telEtu.data).first()
        if user:
            raise ValidationError(
                'Ce numero est deja pris. Pardon choisi un autre')

    def validate_sexeEtu(self, sexeEtu):
        sex = ['M', 'm', 'F', 'f']
        sexeEtu = sexeEtu.data
        if sexeEtu not in sex:
            print('Nous sommes dans erreur')
            raise ValidationError(
                'Le sexe doit etre Masculin ou Feminin. Pardon choisi entre M et F')


class AjoutFormationForm(FlaskForm):
    intituleFormat = StringField('Titre de la formation', validators=[
                                 DataRequired(), Length(min=2, max=500)])
    dateDebutFormat = DateField(
        'Date debut', format='%Y-%m-%d', validators=[DataRequired()])
    dateFinFormat = DateField(
        'Date fin', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField("Ajouter")

    def validate_intituleFormat(self, intituleFormat):
        forma = Formation.query.filter_by(
            intituleFormat=intituleFormat.data).first()
        if forma:
            raise ValidationError(
                'Ce titre est deja pris. Pardon met un autre')


class AjoutAnneeForm(FlaskForm):
    idAnnee = StringField('Annee',
                          validators=[DataRequired()])
    submit = SubmitField("Ajouter")

    def validate_idAnnee(self, idAnnee):
        annee = Annee.query.filter_by(
            idAnnee=idAnnee.data).first()
        if annee:
            print('Nous y sommes')
            raise ValidationError(
                'Ce Annee est dans la base ajoute une autre. Pardon met un autre')


class AfficherEnregistreForm():
    pass
# class LoginForm(FlaskForm):
#     emailForma = StringField('Email', validators=[DataRequired(), Email()])
#     passwordForma = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

class PaiementFromationForm(FlaskForm):
    montantPaie = IntegerField('Montant de paiement', [DataRequired()])
    typePaie = StringField('Motif',[DataRequired()])
    submit = SubmitField("Paie")