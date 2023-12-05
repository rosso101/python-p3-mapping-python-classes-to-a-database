#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
    
    Song = Song.create("Hello", "25")
    print("Song Name:", song.name)
    print("Song Album:", song.album)