from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self): #defines a string to represent the init. obj.
        return '<User {}>'.format(self.name)

    def add_movie(self, name, genre): #my_user_object.add_movie(name, genre) <- this is how you call the method
        movie = Movie(name, genre, False) #False bc new movies haven't been watched yet
        self.movies.append(movie) #adds new movie to the self.movies list

    def delete_movie(self, name):
        self.movies = list(filter(lambda x: x.name != name, self.movies))

    def watched_movies(self): #\/ filter object below needs to be represented as a list
        return list(filter(lambda movie: movie.watched, self.movies)) #helpful function (requites a function & then a list to filter)
                                #lambda function is simply a way to define functions w/o "def"
                                #takes in 1 paramter 'x' just like how __init__ take in 'name' in this class

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    def json(self): #return a dictionary representation
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user

