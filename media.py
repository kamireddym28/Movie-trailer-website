#webbrowser, an essential module is imported to play videos

import webbrowser

class Movie(object):
    """
        A class to store movie related information.

        >>Passed in arguments of __init__() defines the following:
            title       :   Title of the movie
            duration    :   Total run time
            storyline   :   Brief description of the story
            poster_image:   An URL with respective movie poster
            trailer_url :   An URL of an official youtube trailer

        >>show_trailer() uses imported webbrowser module to play
            concerned trailer

    """
    def __init__(self, title, duration, storyline, poster_image, year_of_release, trailer_url):
                 self.title = title
                 self.duration = duration
                 self.storyline = storyline
                 self.poster_image_url = poster_image
                 self.year_of_release = year_of_release
                 self.trailer_youtube_url = trailer_url
                 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
