class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched #if true we assume the user has watched the movie

    def __repr__(self):
        return '<Movie: {} / Genre: {}>'.format(self.name, self.genre)

    def json(self): #json supports boolean values so 'watched' will return as a boolean
        return{
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, json_data): #{'name': '....', 'genre':'...', 'watched':True/False}
        return Movie(**json_data)  #name=json_data['genre'], name=json_data['name'], genre=json_data['watched']
        #this is argument unpacking: same thing as above