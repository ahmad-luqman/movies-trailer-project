import webbrowser


class Movie():
    """This class provides a way to store movie related
     information and show in webbrowser"""
    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube
    ):
        # Constructor
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Show the trailer in the webbrowser
        webbrowser.open(self.trailer_youtube_url)
