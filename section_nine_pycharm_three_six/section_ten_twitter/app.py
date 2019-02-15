import requests
from flask import Flask, render_template, session, redirect, request, url_for, g
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token
from user import User
from database import Database

app = Flask(__name__) #created an app
app.secret_key = '1234' #required bc cookies are encrypted and you don't want someone else gaining access

Database.initialize(user='postgres', password='CpSQLM', host='localhost', database='learning')


@app.before_request #happens before an requests
def load_user():
    if 'screen_name' in session: #if session has a paramater 'screen_name'
        g.user = User.load_from_db_by_screen_name(session['screen_name'])
        #g variables do not disappear once we exit a method


@app.route('/') #decorator / when we access forward slash endpoint, return the method below(http://127.0.0.1:4995/
def homepage(): #called it homepage bc it is simply after "/" rather than somthing like "/users/list/etc"
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    if 'screen_name' in session:
        return redirect(url_for('profile')) #if you are already loggined in this session, you will be redirected instantly to the profile page
    request_token = get_request_token()
    session['request_token'] = request_token #session gets saved through cookies to keep user data active(so it doesn't dissapear)

    return redirect(get_oauth_verifier_url(request_token))

@app.route('/logout')
def logout():
    session.clear() #empties out the session for the user
    return redirect(url_for('homepage'))

@app.route('/auth/twitter') #http://127.0.0.1:5000/auth/twitter?oauth_verifiter=*rest_of_query_string*
def twitter_auth():             #args are the query string parameters
    oauth_verifier = request.args.get('oauth_verifier') #extracts the value of the above oauth verifier and puts it in this veriable 'oauth_verifier'
    access_token = get_access_token(session['request_token'], oauth_verifier)

    user = User.load_from_db_by_screen_name(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], None)
        user.save_to_db()

    session['screen_name'] = user.screen_name

    return redirect(url_for('profile')) #'url_for' is used to redirect to the endpoint associated with the method

@app.route('/profile')
def profile():
    return render_template('profile.html', user=g.user) #can pass in variables after the template name is defined(and create)

@app.route('/search')
def search():
    query = request.args.get('q')

    tweets = g.user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query))

    tweet_texts = [{'tweet':tweet['text'], 'label':'neutral'} for tweet in tweets['statuses']] #get each of the tweet's texts for each of the tweets in 'tweets['statuses]'
                                                                #puts it all into a new list
    for tweet in tweet_texts:
        #using the 'requests' library (for API usage not using oauth)
        r = requests.post('http://text-processing.com/api/sentiment/', data={'text':tweet['tweet']})
        json_response = r.json() #retreives the json contents of the request 'r'
        label = json_response['label']
        tweet['label'] = label

    return render_template('search.html', content=tweet_texts)
app.run(port=5000, debug=True) #told the app to run
