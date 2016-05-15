import random

from django.template.defaultfilters import capfirst

ADJECTIVES = [
    'Appalachian',
    'Blue Ridge',
    'breezy',
    'cosmic',
    'country',
    'county',
    'dancin\'',
    'evergreen',
    'half mile',
    'hillside',
    'hilltop',
    'Floydian',
    'midnight',
    'moonlight',
    'moonlit',
    'mountain',
    'mountaintop',
    'pluckin\'',
    'rosy',
    'shady',
    'steppin\'',
    'sunlit',
    'sunny',
    'sunrise',
    'sunset',
    'sunshine',
    'truckin\'',
    'Virginia',
    'wild',
    'windy',
    'woodsy',
]

NOUNS = [
    'bald',
    'banjo',
    'blues',
    'bonfire',
    'bootlegger',
    'breeze',
    'camp-out',
    'campfire',
    'campsite',
    'celebration',
    'cove',
    'creek',
    'creekbed',
    'dance-off',
    'daydream',
    'feast',
    'forest',
    'grove',
    'hammock',
    'hike',
    'holler',
    'jam',
    'jamboree',
    'jaunt',
    'knob',
    'lightning',
    'log',
    'lovelight',
    'magnolia',
    'mandolin',
    'mountain',
    'oak',
    'picker',
    'pine',
    'ridge',
    'river',
    'rose',
    'step',
    'stream',
    'sunrise',
    'sunset',
    'tent',
    'trail',
    'train',
    'unicorn',
    'wildflower',
    'wind',
]


def generate_rsvp_code(num_nouns=1):
    words = [capfirst(random.choice(ADJECTIVES))]
    for _ in range(num_nouns):
        random_noun = random.choice(NOUNS)
        while random_noun in words:
            random_noun = random.choice(NOUNS)
        words.append(random_noun)
    if len(set(words)) != len(words):  # ensure there are not any repeated words
        return generate_rsvp_code(num_nouns)
    rsvp_code = ' '.join(words)
    return rsvp_code, slugify_rsvp_code(rsvp_code)


def slugify_rsvp_code(rsvp_code):
    return ''.join(filter(str.isalpha, str(rsvp_code.lower())))
