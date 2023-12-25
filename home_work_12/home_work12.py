import os
import string
import csv

from pprint import pprint
from data_film import films_titles
from data_film import films_awards
from data_film import sorted_awards_list
from data_film import ganres
from data_film import films_data



main_directory = "Harry Potter"
os.makedirs(main_directory, exist_ok=True)

for film in films_titles["results"]:
    film_id = film["imdb_id"]
    film_title = film["title"]
    film_directory = os.path.join(main_directory, film_title.replace(':', ''))
    os.makedirs(film_directory, exist_ok=True)

    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)
        os.makedirs(letter_directory, exist_ok=True)

        for awards in films_awards:
            for award in awards['results']:
                award_name = award['award_name']
                title_id = award['movie']['imdb_id']
                if film_id == title_id:
                    first_letter_award = award_name[0]
                    if first_letter_award == letter:
                        award_file_path = os.path.join(letter_directory, f"{award_name}.txt")

                        with open(award_file_path, "a", encoding='utf-8') as award_file:
                            nomination = award['award']
                            award_file.write(f"{nomination}\n")

###Home work 13---------------------------------
ganres_dict = eval(ganres)

for genre in ganres_dict['results']:
    genre_name = genre['genre']
    os.makedirs(f'./genre_films/{genre_name}', exist_ok=True)

# В кожній папці з жанорм створіть CSV файл, з заголовками стобців
# Create genre folders if they don't exist
for genre in ganres_dict['results']:
    genre_name = genre['genre']
    os.makedirs(f'./genre_films/{genre_name}', exist_ok=True)

# Iterate through films and write data to relevant CSV files
for film in films_data:
    gen_list = [g['genre'] for g in film['gen']]  # Extract genre names
    for genre_name in gen_list:
        csv_file = open(f'./genre_films/{genre_name}/movies.csv', 'a', encoding='utf-8')  # Open in append mode
        csv_writer = csv.writer(csv_file)

        # Write only if the header hasn't been written yet
        if csv_file.tell() == 0:
            csv_writer.writerow(['title', 'year', 'rating', 'type', 'ganres',])

        csv_writer.writerow([
            film['title'],
            film['year'],
            film['rating'],
            film['type'],
            ','.join(gen_list),  # Include all genres in the 'ganres' column
        ])
        csv_file.close()