import pandas as pd

#creating a dictionary:
table = {
    'year': [2009, 2002, 2009, 2010, 2009],
    'title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
    'genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']
}

movies = pd.DataFrame(table)

print(movies)