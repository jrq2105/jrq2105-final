##########################
# Name: Jerry Qu
# UNI: jrq2105
#
# File uses Flask to create a server that allows user to use a simple website.
# There are three routes to three different pages of the website.
##########################

# import statements
from flask import Flask, render_template;


# Flask app variable
app = Flask(__name__);


# route for homepage
@app.route("/")
def load_home_page():
    ''' This loads the home page (see home.html) '''
    
    return render_template("home.html");


# route for hobbies page
@app.route("/hobbies")
def load_hobbies_page():
    ''' This loads the hobbies page (see hobbies.html) '''
    
    return render_template("hobbies.html");
    

# route for 'two truths and a lie' game page
@app.route("/random_facts_game")
def load_puzzles_page():
    ''' This loads the 'two truths and a lie' game page
    (see random_facts_game.html) '''
    
    return render_template("random_facts_game.html");


# route for easter egg page
@app.route("/easter_egg")
def load_easter_egg_page():
    ''' This loads the easter egg page (see easter_egg.html) '''
    
    return render_template("easter_egg.html");


# start the server
if __name__ == "__main__":
    app.run();