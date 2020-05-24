import diophantine as mdp
tuples = [
            (144, 89, 1),
            (1960, 103, 1),
            (170, 51, 12),
            (233, 144, 18),
            (3127, 901, 5723),
        ]

for tp in tuples:
    mdp.solve(*tp)
