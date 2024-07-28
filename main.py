# import required modules
from flask import Flask, render_template, request, redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# create the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        # request the word
        word = request.form.get("word")
        # endpoint for Dictionary API
        end = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(end)
        data = response.json()
        # get the phonetic, meaning, part of speech
        phonetic = data[0]["phonetic"]
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        part_of_speech = data[0]["meanings"][0]["partOfSpeech"]
        # return a new page to show results
        return render_template("dictionary.html", word=word,  phonetic=phonetic, meaning=meaning, part_of_speech=part_of_speech)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
