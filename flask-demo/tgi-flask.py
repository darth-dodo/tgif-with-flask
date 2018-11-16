from random import choice

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'bottle-o-rummmmmm'


PIRATE_GREETINGS = ['Ahoy', 'Arr! Matey', 'Arrrrr!', "SQWAK! 'ello",
"Shiver me timbers! It's", "On to the deck"]

PIRATE_INSULTS = ["yellow bellied, lily-livered landlubber!",
"rotten sack of fermented potatoes",
"rapscallion",
"scallywag"
]

PIRATE_BOOTY = {
"chops": ['No compromise attitude', 'Start magic', 'FR'],
"growth": ['Funnel metrics', 'Social Media', 'Blogs, blogs and more blogs'],
"communiteam": ['Influencers', 'Data', 'Sutta', 'Love']
}

INVALID_DECK = "Gimme a valid deck"
INVALID_NAME = "Gimme a name"


# forms
class ReusableForm(Form):
    name = TextField('Department Name:', validators=[validators.required()])


# helpers
def get_department_booty(department_name):

    lowercase_department_name = department_name.lower()

    booty = PIRATE_BOOTY.get(lowercase_department_name, None)

    # if booty:
    #     booty = '\n'.join(booty)

    return booty


def get_all_departments():
    return ' '.join(PIRATE_BOOTY.keys())

def booty_error_handler():
    all_departments = get_all_departments()
    random_insult = choice(PIRATE_INSULTS)
    error_message = '{0}, ye {1} {2}'.format(INVALID_DECK, random_insult,
    all_departments)
    return error_message

# controllers
@app.route("/")
def hello():
    return "Ahoy, Pirates!"


@app.route("/pirate/")
@app.route("/pirate/<pirate_name>")
def pirate_greet(pirate_name=None):

    if not pirate_name:

        random_insult = choice(PIRATE_INSULTS).lower()
        return "{0}, ye {1}".format(INVALID_NAME, random_insult)

    random_greeting = choice(PIRATE_GREETINGS)

    return "{0} {1}!".format(random_greeting, pirate_name.title())


# form for getting name and corresponding pirate booty
@app.route("/booty", methods=['GET', 'POST'])
def department_booty():
    form = ReusableForm(request.form)
    print(form.errors)

    if request.method == 'POST':
        name = request.form.get('name', None)

        error_message = booty_error_handler()

        if form.validate():

            department_booty = get_department_booty(name)

            if department_booty is None:
                flash(error_message)
            else:
                flash(department_booty)
        else:
            flash(error_message)

    return render_template('get_booty.html', form=form)
