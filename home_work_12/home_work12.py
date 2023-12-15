import os
import string

from pprint import pprint
from data_film import films_titles
from data_film import films_awards

main_directory = "Harry Potter"
os.makedirs(main_directory, exist_ok=True)

for film in films_titles["results"]:
    film_title = film["title"]
    film_directory = os.path.join(main_directory, film_title.replace(':', '_'))
    os.makedirs(film_directory, exist_ok=True)
    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)
        os.makedirs(letter_directory, exist_ok=True)



def create_awards_structure(films_awards):
    result_list = []

    for film_awards in films_awards:
        for result in film_awards['results']:
            award_dict = {
                'type': result['type'],
                'award_name': result['award_name'],
                'award': result['award']
            }
            result_list.append(award_dict)

    return result_list

awards_list = create_awards_structure(films_awards)
sorted_awards_list = sorted(awards_list, key=lambda x: x['award_name'])

pprint(sorted_awards_list)
