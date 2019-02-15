import oauth2
import constants
import urllib.parse as urlparse #imports this piece of the library represented as 'urlparse'

#consumer is basically our app
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET) #class in oauth2 library / Recieved from our App saved in 'constants'
    #^used to identify app uniquely

def get_request_token():
    client = oauth2.Client(consumer)
    # client using 'consumer' which represents our app
    # ^used to access API(clients are used to perform requests)

    response, content = client.request(constants.REQUEST_TOKEN_URL,'POST')  # requesting the request token / must add "'POST'" bc it is a POST URL (URL, verb)
    # ^this is what is returned so we want it to be defined as variables
    if response.status != 200:  # if the response did not work properly
        print('An error occurred getting the request token from Twitter!')

    return dict(urlparse.parse_qsl(content.decode('utf-8')))  # converts content quiery string into something else('dict' in this case)
    # ^converts content to strings rather than Bytes

def get_oauth_verifier(request_token):
    # ask the user to authorize our app and give us the PIN code
    print("Go to the following site in your browser:")
    print(get_oauth_verifier_url(request_token))
    #       ^query string: is in the format of name = some-value
    #       ^send Authorization URL to twitter w/the oauth_token query string
    return input('What is the PIN? ')
    #               ^user would input code they received at the website from code lines 19-20

def get_oauth_verifier_url(request_token):
    return "{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token'])


def get_access_token(request_token, oauth_verifier):
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    # ^binds the token and secret together into one object (using oauth2 library 'Token') and we named the product 'token'
    token.set_verifier(oauth_verifier)
    # ^sets the verifier to the oauth_verifier from line 24

    client = oauth2.Client(consumer, token)
    # ^creates a client with our consumer(app) and the newly created(and verified) token
    # ^can now use this client to get the access token

    # ask Twitter for an access token, and Twitter knows it should give it to use bc we verified the request token
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
    return dict(urlparse.parse_qsl(content.decode('utf-8')))



