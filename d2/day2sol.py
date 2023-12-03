# Part 1:

fp = open('input.txt')
lines = fp.readlines()
possible_game_ids = []
for line in lines:
    line = line.strip()
    info, games = line.split(": ")
    game_id = int(info.split()[1])

    games = games.split('; ')
    working = True
    for game in games:
        game = game.split(', ')
        for blocks in game:
            amount, color = blocks.split()
            amount = int(amount)
            if color == 'red' and amount > 12:
                working = False
            elif color == 'green' and amount > 13:
                working = False
            elif color == 'blue' and amount > 14:
                working = False
    if working:
        possible_game_ids.append(game_id)
fp.close()

print(sum(possible_game_ids))


# Part 2

fp = open('input.txt')
lines = fp.readlines()
lowest_possible_cubes = []
for line in lines:
    line = line.strip()
    info, games = line.split(": ")

    games = games.split('; ')
    red_max = 0
    blue_max = 0
    green_max = 0
    for game in games:
        game = game.split(', ')
        for blocks in game:
            amount, color = blocks.split()
            amount = int(amount)
            if color == 'red' and amount > red_max:
                red_max = amount
            elif color == 'green' and amount > green_max:
                green_max = amount
            elif color == 'blue' and amount > blue_max:
                blue_max = amount
    lowest_possible_cubes.append(red_max * blue_max * green_max)
fp.close()

print(sum(lowest_possible_cubes))