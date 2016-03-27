import random

from django.template.defaultfilters import capfirst

ADJECTIVES = [
    'Appalachian',
    'Blue Ridge',
    'breezy',
    'cosmic',
    'county',
    'dancin\'',
    'half mile',
    'hillside',
    'hilltop',
    'Floydian',
    'moonlight',
    'moonlit',
    'mountain',
    'mountaintop',
    'pluckin\'',
    'steppin\'',
    'sunshine',
    'truckin\'',
    'Virginia',
    'wild',
    'woodsy',
]
NOUNS = [
    'banjo',
    'blues',
    'bonfire',
    'bootlegger',
    'campfire',
    'celebration',
    'dance-off',
    'feast',
    'forest',
    'jam',
    'jamboree',
    'jaunt',
    'lightning',
    'lovelight',
    'magnolia',
    'mandolin',
    'mountain',
    'picker',
    'rose',
    'step',
    'trail',
    'train',
    'unicorn',
]


def generate_rsvp_code(num_nouns=1):
    nouns = list(NOUNS)
    words = [capfirst(random.choice(ADJECTIVES))]
    for i in range(num_nouns):
        random_noun = random.choice(NOUNS)
        while random_noun in words:
            random_noun = random.choice(NOUNS)
        words.append(random_noun)
    return ' '.join(words)
