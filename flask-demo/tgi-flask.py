from random import choice

from flask import Flask, render_template

app = Flask(__name__)

PIRATE_GREETINGS = ['Ahoy', 'Arr! Matey', 'Arrrrr!', '<parrot squeak>',
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
