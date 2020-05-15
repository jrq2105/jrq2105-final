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
    

# route for puzzles page
@app.route("/puzzles")
def load_puzzles_page():
    ''' This loads the puzzles page (see puzzles.html) '''
    
    return render_template("puzzles.html");


# route for easter egg page
@app.route("/easter_egg")
def load_easter_egg_page():
    ''' This loads the easter egg page (see easter_egg.html) '''
    
    return render_template("easter_egg.html");


# start the server
if __name__ == "__main__":
    app.run();