from flask import Flask, redirect, url_for, render_template, request, flash, redirect, request, abort
from inscriptionFormation import app, db, bcrypt
from inscriptionFormation.models import Etudiant, Formation, Inscription, Paiement, Annee
# from flask_login import login_user, current_user, logout_user, login_required
from inscriptionFormation.forms import EnregistrementEtudiantForm


@app.route("/")
def home():
    # forma = Formation().paginate()
    return render_template('/pages/home.html')


# @ app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     formLog = LoginForm()
#     if formLog.validate_on_submit():
#         etudiant = Etudiant.query.filter_by(
#             emailEtu=formLog.emailEtu.data).first()
#         if etudiant and bcrypt.check_password_hash(etudiant.passwordEtu, formLog.passwordEtu.data):
#             login_user(etudiant, remember=formLog.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('home'))

#         else:
#             flash('Login Unsuccessful. Please check email  and password', 'danger')
#     return render_template('/pages/login.html', title='Register', formLog=formLog)


@ app.route('/inscriptionEtudiant', methods=['GET', 'POST'])
def inscriptionEtudiant():
    formEtu = EnregistrementEtudiantForm()
    if formEtu.validate_on_submit():
        etudiant = Etudiant(nomEtu=formEtu.nomEtu.data, postNomEtu=formEtu.postNomEtu.data, prenomEtu=formEtu.prenomEtu.data, sexeEtu=formEtu.sexeEtu.data,
                            adressEtu=formEtu.adressEtu.data,   telEtu=formEtu.telEtu.data,  emailEtu=formEtu.emailEtu.data)
        annee = Annee(idAnnee=formEtu.idAnnee.data)
        formation = Formation(intituleFormat=formEtu.intituleFormat.data,
                              dateDebutFormat=formEtu.dateDebutFormat.data, dateFinFormat=formEtu.dateFinFormat.data)
        inscription = Inscription(
            montantInsc=formEtu.montantInsc.data, authorEtut=etudiant, authorForm=formation, authorAnnee=annee)
        #inscription = Inscriptio
        db.session.add(etudiant)
        db.session.add(formation)
        db.session.add(annee)
        db.session.add(inscription)
        db.session.commit()
        flash(f'Ton compte a ete bien cree', 'success')
        return redirect(url_for('home'))
    return render_template('/pages/inscriptionEtudiant.html', title='EnregistrementEtudiant', formEtu=formEtu, sexechoi=['M', 'F'])


# @ app.route('/post/nouvelFormation', methods=['GET', 'POST'])
# def nouveauFormation():
#     formFormat = NouvelleFormation()
#     if formFormat.validate_on_submit():
#         nouvelFormation = Formation(intituleFormat=formFormat.intituleFormat.data, contentFormat=formFormat.contentFormat.data,
#                                     dateDebutFormat=formFormat.dateDebutFormat.data,   dateFinFormat=formFormat.dateFinFormat.data, authorFormat=current_user)
#         db.session.add(nouvelFormation)
#         db.session.commit()
#         flash('Your formation been created', 'success')
#         return redirect(url_for('home'))
#     return render_template('/pages/nouvelformation.html', title='Nouvel Formation', formFormat=formFormat, legend='Nouvel formation')
