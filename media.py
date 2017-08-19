import webbrowser

class Movie():
    """ Class for creating each movie instance or object that will then be passed from the
    entertainment.py file into the Fresh Tomatoes Website by way of fresh_tomatoes.py file """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Initilization of the Movie class in memory.  This method sets up the space for
        each piece of info that the instances of Movie will need for each movies information """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        """ This method is used for taking the youtube url it is passed and opening it inside of a browser """
        webbrowser.open(self.trailer_youtube_url)
