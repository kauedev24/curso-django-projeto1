"""From inspect import signature."""
from random import randint
from faker import Faker


def rand_ratio():
    """."""
    return randint(840, 900), randint(473, 573)


fake = Faker('pt-BR')
# print(signature(fake.random_number))


def make_recipe():
    """."""
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%sfood,cook' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
