import random


ADJECTIVES = ('Adamant', 'Adroit', 'Amatory', 'Animistic', 'Antic', 'Arcadian', 'Baleful', 'Bellicose', 'Bilious', 'Boorish', 'Calamitous', 'Caustic', 'Cerulean', 'Comely', 'Concomitant', 'Contumacious', 'Corpulent', 'Crapulous', 'Defamatory', 'Didactic', 'Dilatory', 'Dowdy', 'Efficacious', 'Effulgent', 'Egregious', 'Endemic', 'Equanimous', 'Execrable', 'Fastidious', 'Feckless', 'Fecund', 'Friable', 'Fulsome', 'Garrulous', 'Guileless', 'Gustatory', 'Heuristic', 'Histrionic', 'Hubristic', 'Incendiary', 'Insidious', 'Insolent', 'Intransigent', 'Inveterate', 'Invidious', 'Irksome', 'Jejune', 'Jocular', 'Judicious', 'Lachrymose', 'Limpid', 'Loquacious', 'Luminous', 'Mannered', 'Mendacious', 'Meretricious', 'Minatory', 'Mordant', 'Munificent', 'Nefarious', 'Noxious', 'Obtuse', 'Parsimonious', 'Pendulous', 'Pernicious', 'Pervasive', 'Petulant', 'Platitudinous', 'Precipitate', 'Propitious', 'Puckish', 'Querulous', 'Quiescent', 'Rebarbative', 'Recalcitrant', 'Redolent', 'Rhadamanthine', 'Risible', 'Ruminative', 'Sagacious', 'Salubrious', 'Sartorial', 'Sclerotic', 'Serpentine', 'Spasmodic', 'Strident', 'Taciturn', 'Tenacious', 'Tremulous', 'Trenchant', 'Turbulent', 'Turgid', 'Ubiquitous', 'Uxorious', 'Verdant', 'Voluble', 'Voracious', 'Wheedling', 'Withering', 'Zealous',)
NOUNS = ('turkey', 'squirrel', 'toothpaste', 'distribution', 'friction', 'silk', 'birth', 'peace', 'zoo', 'cough', 'pancake', 'afternoon',)


def generate_rsvp_code():
    return "%s-%s" % (random.choice(ADJECTIVES).lower(), random.choice(NOUNS).lower())
