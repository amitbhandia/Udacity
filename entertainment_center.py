import media
import fresh_tomatoes

"""
Create new movie object to 3 variables is dunkirk_movie, the_ragnarok, wonder_woman
"""
dunkirk_movie = media.Movie('Dunkirk',
                            'Dunkirk is a 2017 war film written, directed, and produced by'
                            'Christopher Nolan that depicts the Dunkirk evacuation of World War II.',
                            'https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg',
                            'https://www.youtube.com/watch?v=F-eMt3SrfFU')

the_ragnarok = media.Movie('The Ragnarok',
                         'Thor: Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor',
                         'https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg',
                         'https://www.youtube.com/watch?v=ue80QwXMRHg')

wonder_woman = media.Movie('Wonder Woman',
                              'Wonder Woman is a 2017 American superhero film based on the DC Comics character',
                              'https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg',
                              'https://www.youtube.com/watch?v=VSB4wGIdDwo')

"""
Main subroutine for generate movie page
Add 3 variables to movies array for generate
"""
movies = [dunkirk_movie, the_ragnarok, wonder_woman]
fresh_tomatoes.open_movies_page(movies)
