import diophantine as mdp
pairs = [
            (144, 89),
            (1960, 103),
            (170, 51),
            (233, 144),
            (3127, 901),
        ]

for pair in pairs:
    mdp.solve(*pair)
