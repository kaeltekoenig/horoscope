import converter

days = [
    (80, 110),
    (111, 140),
    (141, 172),
    (173, 203),
    (204, 235),
    (236, 266),
    (267, 296),
    (297, 326),
    (327, 355),
    (356, 365),  # 9
    (0, 20),      # 10
    (21, 49),
    (50, 79)
]

associates = dict(zip(converter.zodiac_signs, days))
