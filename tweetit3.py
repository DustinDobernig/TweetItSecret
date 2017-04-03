from flask import Flask, render_template
from flask import request, redirect
from flask_limiter import Limiter
import time


from twitter import *

#Get API Tokens

access_token = "access_token"
access_token_secret = "access_token_secret"
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

app = Flask(__name__)
limiter = Limiter(app)


#Hello
@app.route('/')
def hello_world():
    author = "Me"
    name = "Dustin Dobernig"
    message = "Welcome to TweetItSecret. Want to confess something anonomously? Type it here and we'll tweet it for you."
    return render_template('index.html', author=author, name=name, message=message,)

#Get and post tweet
@app.route('/', methods = ['POST'])
def tweet_it():
    if request.method == 'POST':
        tweet = request.form['tweet']
        if tweet ==  "Welcome to TweetItSecret. Want to confess something anonomously? Type it here and we'll tweet it for you.":
            return redirect('/')
        elif tweet == "Tweet sent.":
            return redirect('/')
        elif tweet == "":
            return redirect('/')
        else:
            t.statuses.update(status = tweet + " #secret")
    return redirect('/success')

@app.route('/success')
def tweet_sent():
    author = "Me"
    name = "Dustin Dobernig"
    message = "Tweet sent."
    return render_template('index.html', author=author, name=name, message=message,)



def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string





if __name__ == "__main__":
    app.run()

