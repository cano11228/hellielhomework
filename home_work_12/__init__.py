from data_film import films_data

from pprint import pprint
for film_data in films_data:
 for ssgalicia in film_data['gen']:
  pprint(ssgalicia.keys())

