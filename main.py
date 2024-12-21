from Zodiac_signs import get_day_number_by_date
from associate_sign_and_day import associates


if __name__ == '__main__':
    date = get_day_number_by_date(input())
    for animal, days in associates.items():
        if date in range(*days):
            if animal == 'Козерог 2':
                animal = 'Козерог'
            print(animal)