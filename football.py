import random

teams = ['arsenal', 'chelsea', 'manchester city', 'liverpool', 'everton', 'manchester united', 'tottenham']
pairs = []
for home in teams:
    for guest in teams:
        if home != guest:
            home_score = random.randint(0, 4)
            guest_score = random.randint(0, 4)
            pairs.append({home: home_score, guest: guest_score })



for index, pair in enumerate(pairs):
    print(index)
    print(pair.items())

