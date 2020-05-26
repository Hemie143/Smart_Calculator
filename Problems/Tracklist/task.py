def tracklist(**tracks):
    for artist, data in tracks.items():
        print(artist)
        for album, track in data.items():
            print(f'ALBUM: {album} TRACK: {track}')
