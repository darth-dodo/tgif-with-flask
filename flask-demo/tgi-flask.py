from random import choice

from flask import Flask, render_template, flash, request, jsonify
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

DEPARTMENT_DATA = [
{"name": "Engineering", "bio": "Bad at copywriting."},
{"name": "Product", "bio": "Require more sleep."},
{"name": "Growth", "bio": "Discuss about funnel conversions and throughputs."},
{"name": "ChOps", "bio": "The secret sauce <3"},
{"name": "Business", "bio": "Onboarding vendors like a boss"},
{"name": "Communiteam", "bio": "Data and Sutta and Chai and Love"}
]

PIRATE_BOOTY = {
"chops": ['No compromise attitude', 'FR', 'Sales smarts'],
"growth": ['Funnel metrics', 'Social Media', 'Blogs, blogs and more blogs'],
"communiteam": ['Influencers','CLCC', 'Rolling paper']
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

    return booty


def get_all_departments():
    return list(PIRATE_BOOTY.keys())

def booty_error_message_generator():
    random_insult = choice(PIRATE_INSULTS)
    error_message = '{0}, ye {1}'.format(INVALID_DECK, random_insult)
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
    error_message = None
    all_departments = get_all_departments()

    if request.method == 'POST':

        name = request.form.get('name', None)

        if form.validate():

            department_booty = get_department_booty(name)

            if department_booty is None:
                error_message = booty_error_message_generator()

        else:
            error_message = booty_error_message_generator()

    return render_template('get_booty.html', form=form,
    error_message=error_message,
    department_booty=department_booty,
    all_departments=all_departments)


@app.route("/decks")
def ithaka_decks():
    return jsonify(DEPARTMENT_DATA)
