import random

teams = ['arsenal', 'chelsea', 'manchester city', 'liverpool', 'everton', 'manchester united', 'tottenham']


pairs = []
for home_name in teams:
    for guest_name in teams:
        winner = None
        if home_name != guest_name:
            home_score = random.randint(0, 4)
            guest_score = random.randint(0, 4)
            if home_score > guest_score:
                winner = home_name
            elif home_score < guest_score:
                winner = guest_name
            else:
                pass
            new_pair = {'home_name': home_name,
                          'home_score': home_score,
                          'guest_name': guest_name,
                          'guest_score': guest_score,
                           'winner': winner}
            pairs.append(new_pair)
            print(*new_pair.values(), sep=" - ")


teams_res = {}
for i in teams:
    teams_res[i] = 0
    for pair in pairs:
        if pair['winner'] == i:
            teams_res[i]+=3
        elif pair['winner'] == None and (pair['home_name'] == i or pair['guest_name'] == i):
            teams_res[i]+=1
print("=================================================")
print(*sorted(teams_res.items(), key = lambda x: x[1], reverse=True))
