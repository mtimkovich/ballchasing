"""Do math with the replays."""


def winning_team(replay):
    """Returns which team won."""
    orange = replay['orange'].get('goals', 0)
    blue = replay['blue'].get('goals', 0)

    return 'orange' if orange > blue else 'blue'


def which_team(replay, name):
    """Return which team `name` is on."""
    for team in ['orange', 'blue']:
        players = replay[team]['players']
        for p in players:
            if p['name'] == name:
                return team


def win_percentage(replays, name):
    wins = 0
    total = 0
    for replay in replays['list']:
        winner = winning_team(replay)
        color = which_team(replay, name)
        total += 1

        if winner == color:
            wins += 1
    if total == 0:
        return 0

    print(f'{wins} wins, {total} played')
    print(f'Win %: {wins / total * 100:.2f}%')
