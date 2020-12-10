from ballchasing import Ballchasing
import config

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

ballchasing = Ballchasing(token=config.API_KEY)
SEASON2_START = '2020-12-10T00:00:00+00:00'

replays = ballchasing.replays({
    'uploader': 'me',
    'playlist': 'ranked-standard',
    'count': 200,
    'replay-date-after': SEASON2_START,
})

win_percentage(replays, 'DJSwerve')
