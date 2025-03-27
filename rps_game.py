import json

def who_wins(player1, item1, player2, item2): # Checks which player won the round
    if item1 == item2: # For the same move
        return None
    if (item1 == "rock" and item2 == "scissors") or \
       (item1 == "scissors" and item2 == "paper") or \
       (item1 == "paper" and item2 == "rock"):
        return player1
    else:
        return player2

def find_best_player(stats): # Takes the stats and find which player has the best stats
    best_ratio = -1
    winners = [] # List of the winners if there are more than one

    for player in stats:
        wins, games = stats[player]
        ratio = wins / games

        if ratio > best_ratio:
            best_ratio = ratio
            winners = [player]
        elif ratio == best_ratio:
            winners.append(player)

    if len(winners) == 1: # Checks how many players have the best stats
        return winners[0]
    else:
        return "tie"

def game(results_filename):
    try:
        with open(results_filename, 'r', encoding='utf8') as f:
            lines = f.readlines() # A line is one game each
    except FileNotFoundError:
        print("Error.")
        exit(1)
    stats = dict()

    for line in lines[1:]:
        player1, item1, player2, item2 = line.strip().split() # Takes all the data from the line

        for player in [player1, player2]:
            if player not in stats:
                stats[player] = [0, 0]
            stats[player][1] += 1 # Add one game each either way

        p_winner = who_wins(player1, item1, player2, item2)
        if p_winner is not None:
            stats[p_winner][0] += 1
    return find_best_player(stats)

students = {'id1': '207106238', 'id2': '322630716'}

if __name__ == '__main__':
    with open('config-rps.json', 'r') as json_file:
        config = json.load(json_file)

    winner = game(config['results_filename'])
    print(f'the winner is: {winner}')
