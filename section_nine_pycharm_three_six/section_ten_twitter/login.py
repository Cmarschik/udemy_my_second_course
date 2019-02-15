from user import User
from database import Database
from twitter_utils import get_request_token, get_oauth_verifier, get_access_token

#initializes our database in this login page
Database.initialize(user='postgres', password='CpSQLM', host='localhost', database='learning')

user_email = input("What is your email: ")

user = User.load_from_db(user_email)

if not user:
    #if the user we searched(by email) does not exist, you must re-authenticate(below)

    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    #creating a User below
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    #creating a User
    user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
                                            #^these are found once we know the access token above works(they are within the 'content' of the access token
    user.save_to_db()

tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers filter:images')
#           #loads means 'load string' bc it is loading from a string to we use it
#           ^allows us to load the content as a dictionary from a json file(dict is called 'tweets')
for tweet in tweets['statuses']:
    print(tweet['text'])


