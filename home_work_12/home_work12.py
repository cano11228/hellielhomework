import os
import string

from pprint import pprint
from data_film import films_titles
from data_film import films_awards
from data_film import sorted_awards_list



main_directory = "Harry Potter"
os.makedirs(main_directory, exist_ok=True)

for film in films_titles["results"]:
    film_title = film["title"]
    film_directory = os.path.join(main_directory, film_title.replace(':', ''))
    os.makedirs(film_directory, exist_ok=True)

    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)
        os.makedirs(letter_directory, exist_ok=True)

        # Цикл для кожної нагороди фільму
        for award in sorted_awards_list:
            award_name = award["award_name"]
            first_letter_award = award_name[0]
            if first_letter_award == letter:
                # Create the award file path within the loop
                award_file_path = os.path.join(letter_directory, f"{award_name}.txt")

                # Створення або дописання інформації в файл
                with open(award_file_path, "a", encoding='utf-8') as award_file:
                    # Цикл для кожної номінації нагороди
                     nomination = award['award']
                     award_file.write(f"{nomination}\n")