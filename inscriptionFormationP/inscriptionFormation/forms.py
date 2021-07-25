from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from inscriptionFormation.models import Etudiant
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
    # table formation
    intituleFormat = StringField('Titre de la formation', validators=[
                                 DataRequired(), Length(min=2, max=500)])
    dateDebutFormat = DateField(
        'Date debut', format='%Y-%m-%d', validators=[DataRequired()])
    dateFinFormat = DateField(
        'Date fin', format='%Y-%m-%d', validators=[DataRequired()])
    # table annee
    idAnnee = DateField('Annee', format='%Y', validators=[DataRequired()])

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


# class LoginForm(FlaskForm):
#     emailForma = StringField('Email', validators=[DataRequired(), Email()])
#     passwordForma = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')
