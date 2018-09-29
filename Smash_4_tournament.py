import time

character_values = {
                    'ba': 334.9, 'cd': 322.8, 'dd': 322.1, 'sh': 321.5, 'ra': 320.9, 'zs': 320.7, 'fx': 311.3,
                    'sc': 310.0, 'mo': 307.8, 'mw': 305.1, 'mt': 302.1, 'ru': 299.9, 'cr': 297.8, 'la': 297.0,
                    'pk': 296.1, 'mk': 286.0, 'lo': 285.6, 'lg': 283.1, 'cf': 282.6, 'pc': 282.0, 'ol': 281.1,
                    'dk': 278.9, 'tl': 278.4, 'bw': 275.0, 'vr': 274.5, 'gr': 274.0, 'mm': 273.3, 'ns': 271.6,
                    'ls': 270.7, 'dh': 269.3, 'ln': 265.6, 'pt': 263.1, 'dp': 258.9, 'yo': 258.3, 'sk': 257.9,
                    'rb': 254.8, 'rn': 252.5, 'ss': 249.4, 'gw': 248.5, 'ik': 247.2, 'wo': 246.1, 'ry': 245.8,
                    'cz': 242.7, 'lm': 241.9, 'pa': 240.7, 'pm': 240.4, 'fo': 237.8, 'bj': 235.4, 'dm': 231.9,
                    'kb': 227.4, 'wt': 226.0, 'kd': 217.1, 'gn': 215.8, 'za': 209.1, 'jp': 199.7, 'mi': 199.7
                    }
names = []
value_starter = []
amount_not_chosen = True
matches = 20


def is_number():
    global is_not_number
    is_not_number = True
    while is_not_number:
        var = input("How many players? (2 - 7)\n")
        if var.isdigit():
            is_not_number = False
            return var
        else:
            print("Numbers, not letters knuckle-head...")


while amount_not_chosen:
    player_number0 = is_number()
    player_number = int(player_number0)
    if 1 < int(player_number) < 8:
        amount_not_chosen = False
    else:
        print("Use a realistic player amount you wise-alec!")
count = 0

while count < player_number:
    answer = input("Who is player " + str(count+1) + "?")
    names.append(answer.title())
    value_starter.append(0)
    count += 1
player_scores = dict(zip(names, value_starter))


count = 0
print("\nPress enter if the player is not playing that round.")

while count < matches:     # which character is everyone using?
    character_match_storage = []
    for i in names:
        character_match_storage.append("")
    count2 = 0
    print("\nRound " + str(count + 1) + "\n")
    might_break = True
    while might_break:
        while count2 < len(names):
            answer = input("Which character is " + names[count2].title() + " using this round?")
            if answer.lower() not in character_values:
                while answer.lower() not in character_values:
                    if answer.lower() == "":
                        break
                    else:
                        print("That's not a character input. Try again!")
                        answer = input("Which character is " + names[count2].title() + " using this round?")
            character_match_storage[count2] = answer.lower()
            count2 += 1
        space_count = character_match_storage.count("")
        if space_count < (len(names) - 1):
            might_break = False
        else:
            print("\nToo many players 'not playing'. Try entering each player's character again.\n")
            count2 = 0
    time.sleep(2)
    answer = input("Who won?")
    winner = answer.title()
    count3 = 0
    match_storage_list_winner = names.index(winner)
    winner_character = character_match_storage[match_storage_list_winner]
    match_storage_list_losers = []
    while count3 < len(character_match_storage):
        if character_match_storage[count3] == "":
            count3 += 1
        elif count3 == names.index(winner):
            count3 += 1
        else:
            match_storage_list_losers.append(character_match_storage[count3])
            count3 += 1

    count4 = 0
    loser_ratings = 0.0
    winner_rating = character_values[winner_character]
    while count4 < len(match_storage_list_losers):
        loser_ratings += character_values[match_storage_list_losers[count4]]
        count4 += 1
    loser_ratings_average = loser_ratings / len(match_storage_list_losers)
    points_added = loser_ratings_average / winner_rating * 100
    player_scores[winner] += round(points_added, 1)
    print(player_scores)
    count += 1

maximum = max(player_scores, key=player_scores.get)
print("\n" + maximum + " wins with a score of " + str(player_scores[maximum]) + "!")







