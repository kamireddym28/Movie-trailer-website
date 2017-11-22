#Movie class is defined in media.py
#fresh_tomatoes.py generates a HTML and opens listed movies in a webpage

import fresh_tomatoes
import media

#list of instances called on Movie class

Titanic = media.Movie("Titanic",
                      "Duration:195min", 
                      "An epic, action-packed romance set against the ill " \
                      "fated maiden voyage of R.M.S Titanic",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg", #noqa
                      "Year:1997",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
Avatar = media.Movie("Avatar",
                     "Duration:162min", 
                     "A story depicting the interaction of genetically " \
                     "engineered Na'vi body with the mind of a remotely " \
                     "located human inorder to with the natives of Pandora",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "Year:2009",
                     "https://www.youtube.com/watch?v=wsnMbDdhCe8")

War_apes = media.Movie("War for the planet of the Apes",
                       "Duration:142min", 
                       "A confrontation between the apes and the humans for " \
                       "control of Earth",
                       "http://bigfanboy.com/wp/wp-content/uploads/2016/12/warplanetoftheapes-poster1.jpg", #noqa
                       "Year:2017",
                       "https://www.youtube.com/watch?v=JDcAlo8i2y8")


HPotter_P1= media.Movie("Harry Potter and the Deathly Hallows: Part1",
                        "Duration:146min",
                        "Harry Potter and his friends has been tasked by" \
                        "Dumbledore with finding and destroying Lord "\
                        "Voldemort's secret to immortality -- the Horcruxes",
                        "https://vignette.wikia.nocookie.net/harrypotter/images/6/65/Harry-Potter-and-the-Deathly-Hallows-Part-1-poster.jpg/revision/latest?cb=20101001182826", #noqa
                        "Year:2010",
                        "https://www.youtube.com/watch?v=MxqsmsA8y5k")

LRings_P1 = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                        "Duration:228min", 
                        "The future of civilization rests in the fate of the " \
                        "One Ring, which has been lost for centuries",
                        "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg", 
                        "Year:2001",
                        "https://www.youtube.com/watch?v=Pki6jbSbXIY")

Twilight = media.Movie("Twilight",
                       "Duration:122min", 
                       "A story of a girl and her romantic relationship with " \
                       "an immortal soulmate",
                       "https://upload.wikimedia.org/wikipedia/en/b/b6/Twilight_%282008_film%29_poster.jpg", #noqa
                       "Year:2008",
                       "https://www.youtube.com/watch?v=E1z1zseX5C8")

#Array of the movies to be displayed on the webpage
movies = [Titanic, Avatar, War_apes, HPotter_P1, LRings_P1, Twilight]

#Triggers open_movies_page() in fresh_tomatoes.py and generates HTML
fresh_tomatoes.open_movies_page(movies)
