from database import CursorFromConnectionPool
import oauth2
from twitter_utils import consumer
import json

class User:

    def __init__(self, screen_name, oauth_token, oauth_token_secret, id):
        self.screen_name = screen_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

    def __repr__(self):
        return "User {}".format(self.screen_name)

    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            cursor.execute("INSERT INTO users (screen_name, oauth_token, oauth_token_secret) VALUES (%s, %s, %s)",
                           (self.screen_name, self.oauth_token, self.oauth_token_secret))

    @classmethod
    def load_from_db_by_screen_name(cls, screen_name):
        with CursorFromConnectionPool() as cursor:
            cursor.execute("SELECT * FROM users WHERE screen_name = %s", (screen_name,))
            user_data = cursor.fetchone()
            if user_data:  # ('if user_data is not None' is the same as what we wrote. It means we found an account associated with our input email
                return cls(screen_name=user_data[1],
                           oauth_token=user_data[2],
                           oauth_token_secret=user_data[3],
                           id=user_data[0]
                           )

    def twitter_request(self, uri, verb='GET'):
        # everything below is used regardless of whether or not a user re-registers/gains access to app
        # create an 'authorized_token' Token object and use that to perform Twitter API calls on behalf of the user
        authorized_token = oauth2.Token(self.oauth_token, self.oauth_token_secret)  # uses the oauth_token/secret from the above defined user
        authorized_client = oauth2.Client(consumer, authorized_token)
        # When using the client and the authorized_token, we are using an access token(embedded in the authorized_token).. Twitter knows which user we are using
        # Make Twitter API calls
        response, content = authorized_client.request(uri, verb)
        # query string^ (enter search terms here)
        # uses the 'images' filter
        if response.status != 200:
            print('An error occurred when searching!')

        return json.loads(content.decode('utf-8')) #all Twitter requests return json files and then we encode it to utf-8 so we can read/use it

