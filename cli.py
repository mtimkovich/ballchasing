#!/usr/bin/env python3
"""CLI entrypoint to the API code."""
import argparse
from datetime import date, timedelta

from ballchasing import Ballchasing
import config
import stats


def rfc3339(day):
    return day.isoformat() + 'T00:00:00+00:00'


SEASON2_START = date(2020, 12, 10)
today = date.today()
TIME_MAP = {
    'all': date(2015, 7, 7),
    'season': SEASON2_START,
    'month': today - timedelta(days=30),
    'week': today - timedelta(days=7),
    'yesterday': today - timedelta(days=1),
    'today': today,
}

TIME_MAP = {k: rfc3339(v) for k, v in TIME_MAP.items()}

PLAYLIST_OPTIONS = ['unranked-duels', 'unranked-doubles', 'unranked-standard',
                    'unranked-chaos', 'private', 'season', 'offline',
                    'ranked-duels', 'ranked-doubles', 'ranked-solo-standard',
                    'ranked-standard', 'snowday', 'rocketlabs', 'hoops',
                    'rumble', 'tournament', 'dropshot', 'ranked-hoops',
                    'ranked-rumble', 'ranked-dropshot', 'ranked-snowday',
                    'dropshot-rumble', 'heatseeker']

parser = argparse.ArgumentParser()
parser.add_argument('--since', choices=TIME_MAP.keys(), default='all',
                    help='how far back to gather replays')
parser.add_argument('--playlist', choices=PLAYLIST_OPTIONS,
                    default='ranked-standard',
                    help='which playlist to search through')
args = parser.parse_args()

ballchasing = Ballchasing(token=config.API_KEY)

replays = ballchasing.replays({
    'uploader': 'me',
    'playlist': args.playlist,
    'count': 200,
    'replay-date-after': TIME_MAP[args.since],
})

stats.win_percentage(replays)
