from flask import Flask, redirect, url_for, render_template, request, flash, redirect, request, abort
from inscriptionFormation import app, db, bcrypt
from inscriptionFormation.models import Etudiant, Formation, Inscription, Paiement, Annee
# from flask_login import login_etudiant, current_etudiant, logout_etudiant, login_required
from inscriptionFormation.forms import EnregistrementEtudiantForm, AjoutFormationForm, AjoutAnneeForm,PaiementFromationForm
from datetime import datetime

@app.route("/")
def home():
    # forma = Formation().paginate()
    return render_template('/pages/home.html')


@ app.route('/inscriptionEtudiant', methods=['GET', 'POST'])
def inscriptionEtudiant():
    formEtu = EnregistrementEtudiantForm()
    bdformation = Formation.query.all()
    bdannee = Annee.query.all()
    if formEtu.validate_on_submit():
        etudiant = Etudiant(nomEtu=formEtu.nomEtu.data, postNomEtu=formEtu.postNomEtu.data, prenomEtu=formEtu.prenomEtu.data, sexeEtu=formEtu.sexeEtu.data,
                            adressEtu=formEtu.adressEtu.data,   telEtu=formEtu.telEtu.data,  emailEtu=formEtu.emailEtu.data)
        inscription = Inscription(
            montantInsc=formEtu.montantInsc.data, authorEtut=etudiant, authorForm=Formation.query.filter_by(intituleFormat=formEtu.intituleFormat.data).first(), authorAnnee=Annee.query.filter_by(idAnnee=formEtu.idAnnee.data).first())
        db.session.add(etudiant)
        db.session.add(inscription)
        db.session.commit()
        flash(f'Ton compte a ete bien cree', 'success')
        return redirect(url_for('home'))
    return render_template('/pages/inscriptionEtudiant.html', title='EnregistrementEtudiant', formEtu=formEtu, sexechoi=['M', 'F'], bdannee=bdannee, bdformation=bdformation)


@ app.route('/ajoutFormation', methods=['GET', 'POST'])
def ajoutFormation():
    formForm = AjoutFormationForm()
    if formForm.validate_on_submit():
        formation = Formation(intituleFormat=formForm.intituleFormat.data,
                              dateDebutFormat=formForm.dateDebutFormat.data, dateFinFormat=formForm.dateFinFormat.data)
        db.session.add(formation)
        db.session.commit()
        flash(f'La formation a ete bien ajoute', 'success')
        return redirect(url_for('home'))
    return render_template('/pages/ajoutFormation.html', title='Ajout Formation', formForm=formForm)


@ app.route('/ajoutAnnee', methods=['GET', 'POST'])
def ajoutAnnee():
    formAnnee = AjoutAnneeForm()
    if formAnnee.validate_on_submit():
        annee = Annee(idAnnee=formAnnee.idAnnee.data)
        db.session.add(annee)
        db.session.commit()
        flash(f'L annee a ete bien creee', 'success')
        return redirect(url_for('home'))
    return render_template('/pages/ajoutAnnee.html', title='Ajout Annee', formAnnee=formAnnee)


@app.route("/listeInscrit")
def afficheListe():
    page = request.args.get('page', 1, type=int)
    inscris = Inscription.query.order_by(
        Inscription.anneeIdFk.desc()).paginate(page=page, per_page=20)
    # inscris = Inscription.query.all()
    return render_template('/pages/afficheListe.html', inscris=inscris)

@ app.route('/inscription/<int:idInsc>')
def ownerinscri(idInsc):
    insc = Inscription.query.get_or_404(idInsc)
    paiement = Paiement.query.filter_by(inscriptionIdFk =idInsc)
    return render_template('/pages/ownerInsc.html', title=insc.authorForm.intituleFormat, insc=insc,paiement = paiement, datePaiement=datetime.utcnow())

@ app.route('/inscription/<int:idInsc>/supprimer', methods=['POST'])
def inscriptionSupprimee(idInsc):
    insc = Inscription.query.get_or_404(idInsc)
    print(insc)
    db.session.delete(insc)
    db.session.commit()
    flash('Ton inscription a ete bien supprimee', 'success')
    return redirect(url_for('home'))

@ app.route('/paiement/<int:idInsc>', methods=['GET', 'POST'])
def paiementFormation(idInsc):
    insc = Inscription.query.get_or_404(idInsc)
    paiementForm = PaiementFromationForm()
    print(insc.idInsc)
    if paiementForm.validate_on_submit():
        paiement = Paiement(montantPaie = paiementForm.montantPaie.data, typePaie = paiementForm.typePaie.data, authorPaiement = insc)
        db.session.add(paiement)
        db.session.commit()
        flash(f'Ton paiement a ete bien fait', 'success')
        return redirect(url_for('ownerinscri',idInsc = insc.idInsc))
    return render_template('/pages/paiement.html', paiementForm = paiementForm)

# @app.route("/listeInscrit/<string:intituleFormat>")
# def afficheListeParFormation(intituleFormat):
#     page = request.args.get('page', 1, type=int)
#     inscrisParForm = Inscription.query.filter_by(intituleFormat = authorForm.intituleFormat).paginate(page=page, per_page=20)
#     # inscris = Inscription.query.all()
#     return render_template('/pages/afficheListeParFormation.html', inscrisParForm =inscrisParForm )

# @app.route("/listeformation/")
# def afficheListedeFormation():
#     page = request.args.get('page', 1, type=int)
#     bdformation = Formation.query.filter_by(intituleFormat=Formation.intituleFormat).paginate(page=page, per_page=20)
#     # inscris = Inscription.query.all()
#     return render_template('/pages/afficheListedeFormation.html',  bdformation = bdformation )