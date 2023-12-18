import os
import string
from pprint import pprint
from data_film import films_titles
from data_film import films_awards


os.mkdir("Harry Potter")

# Отримайте список назв фільмів
films_titles = films_titles["results"]
films_titles = [films_titles[i]["title"] for i in range(len(films_titles))]
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

# Для кожного фільму створіть новий список нагород
award_lists = []
for film_title in films_titles:
    award_lists.append([])
    for award in sorted_awards_list:
        if award["type"].startswith(film_title):
            award_lists[-1].append(award)

# Для кожного фільму та кожної нагороди створіть текстовий файл
for film_title, award_list in zip(films_titles, award_lists):
    for award in award_list:
        award_name = award["award_name"]
        award_type = award["type"]
        for letter in string.ascii_uppercase:
            directory_name = f"{film_title}_{letter}"
            if not os.path.exists(os.path.join("Harry Potter", directory_name)):
                os.mkdir(os.path.join("Harry Potter", directory_name))
            filename = f"{award_name}_{award_type}.txt"
            with open(os.path.join("Harry Potter", directory_name, filename), "w") as f:
                for nomination in award["nominations"]:
                    f.write(nomination + "\n")

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


def write_awards_to_files(awards_lists):
    # Для кожного фільму і для кожної нагороди створіть файл
    for awards_list in awards_lists:
        for award in awards_list:
            award_name = award["award_name"]
            award_text = award["award"]

            # Створіть файл
            file_path = os.path.join("Harry Potter", award_name, award_name + ".txt")
            with open(file_path, "w") as file:
                file.write(award_text)


