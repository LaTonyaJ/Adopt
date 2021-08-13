from forms import AddPet, EditPet
from flask.templating import render_template
from flask import render_template, redirect
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

app.config['SECRET_KEY'] = 'RescueAnimalAdoptMe54321'
debug = DebugToolbarExtension(app)


@app.route('/')
def show_pets():
    """Show All pets"""

    pets = Pet.query.all()

    return render_template('pets.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Add a pet"""

    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, age=age,
                      photo_url=photo_url, notes=notes)

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_info(pet_id):
    """Show pet info page and edit form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('pet_info.html', pet=pet, form=form)
