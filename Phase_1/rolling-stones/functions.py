import matplotlib.pyplot as plt
import math

def most_popular_artist(album_dict):
    counter_dict = {}
    for artist in all_album_artists(album_dict): #loops over list of the artists for all albums,
        # includes repeats
        if artist in counter_dict: #checking to see if artist alread in counter_dict
            counter_dict[artist] += 1 #if it is, increment by 1
        else: #if 
            counter_dict[artist] = 1 #add artist to the dictionary
    maximum_albums = max(counter_dict.values())
    artist_list = []
    for keys, values in counter_dict.items():
        if values == maximum_albums:
            artist_list.append(keys) 
    return artist_list

def most_popular_word(album_dict):
    counter_dict = {}
    for title in all_album_titles(album_dict): #loops over list of the titles for all albums,
        # includes repeats
        split_title = [word.lower() for word in title.split()]
        for word in split_title:
            if word in counter_dict: #checking to see if artist alread in counter_dict
                counter_dict[word] += 1 #if it is, increment by 1
            else: #if 
                counter_dict[word] = 1 #add artist to the dictionary
    maximum_occur = max(counter_dict.values())
    word_list = []
    for keys, values in counter_dict.items():
        if values == maximum_occur:
            word_list.append(keys) 
    return word_list

def find_album_by_name(album_name, album_dict):
    for album in album_dict:
        if album['album'] == album_name:
            return album
    return None

def find_album_by_rank(album_rank, album_dict):
    for album in album_dict:
        if int(album['number']) == album_rank:
            return album
    return None

def find_album_by_ranks(start_rank, end_rank, album_dict):
    albums_list = []
    for album in album_dict:
        if (int(album['number']) >= start_rank) and (int(album['number']) <= end_rank):
            albums_list.append(album)
    return albums_list

def find_album_by_year(album_year, album_dict):
    album_list = []
    for album in album_dict:
        if int(album['year']) == album_year:
            album_list.append(album['album'])
    return album_list

def find_album_by_years(start_year, end_year, album_dict):
    albums_list = []
    year_range = range(start_year, end_year + 1)
    for year in year_range:
        for album_name in find_album_by_year(year, album_dict):
            albums_list.append(album_name)
    return albums_list


def all_album_titles(album_dict):
    album_titles = [album['album'] for album in album_dict]
    return album_titles

def all_album_artists(album_dict):
    album_artists = [album['artist'] for album in album_dict]
    return album_artists

def albums_by_decade_hist(album_dict):
    album_years = [int(album['year']) for album in album_dict]
    min_year = min(album_years)
    max_year = max(album_years)
    min_year = int( 10 * math.floor(min_year/10) ) 
    max_year = int( 10 * math.ceil(max_year/10) )
    num_bins = int( (max_year - min_year) / 10 )
    fix, ax = plt.subplots()
    ax.hist(album_years, bins = num_bins, range = (min_year, max_year), color = 'b')
    ax.set_xlabel('Decade')
    ax.set_ylabel('Number of albums')
    return

def genre_hist(album_dict):
    album_genres = [album['genre'] for album in album_dict]
    fix, ax = plt.subplots()
    ax.hist(album_genres, bins = num_bins, range = (min_year, max_year), color = 'b')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Number of albums')
    return


def album_with_most_top_songs(album_dict, top_songs_list):
    artist_album_topsongs = []
    
    # build data structure of artist/album/count of top songs
    top_songs = [song['name'] for song in top_songs_list]
    max_count = 0
    for album in album_dict:
        count = 0
        for track in album['tracks']:
            if track in top_songs:
                count += 1
        if count > max_count:
            if max_count > 0:
                artist_album_topsongs.pop()
            artist_album_topsongs.append({'artist': album['artist'],
                                          'album': album['album'],
                                          'count': count})
            max_count = count
    
    return artist_album_topsongs

def albums_with_top_songs(top_songs_list, album_tracks_list):
    top_songs = [song['name'] for song in top_songs_list]
    top_albums = []
    for album in album_tracks_list:
        for track in album['tracks']:
            if track in top_songs: 
                top_albums.append(album['album'])
    return list(set(top_albums))

def songs_that_are_on_top_albums_old(album_tracks_list, top_songs_list):
    top_songs_top_albums = []
    # build data structure of artist/album/count of top songs
    top_songs = [song['name'] for song in top_songs_list]
    for album in album_tracks_list:
        for track in album['tracks']:
            if track in top_songs: 
                top_songs_top_albums.append(track)
    return list(set(top_songs_top_albums))

def top_10_albums_by_top_songs(album_tracks_list, top_songs_list):
    album_topsongs = {}
    top_songs = [song['name'] for song in top_songs_list]
    # build data structure of artist/album/count of top songs
    
    for album in album_tracks_list:
        count = 0
        for track in album['tracks']:
            if track in top_songs:
                    count += 1
        album_topsongs.update({album['album']:count})

    album_topsongs = sorted(album_topsongs.items(), key=lambda x: x[1], reverse = True)[:10]
    
    album_count_list = []
    for album in range(0,10):
        for count in range(album_topsongs[album][1]):
            album_count_list.append(album_topsongs[album][0])
    
    fig, ax = plt.subplots(figsize=(15,10));
    ax.hist(album_count_list)
        
#     ax.bar(top_10_albums, top_10_albums_songs, color= 'turquoise')
#     ax.set_xlabel('Album Name')
#     ax.set_ylabel('Songs on Top Songs List')
#     ax.set_title('Top 10 albums with chart-topping songs')
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    
#     return album_topsongs
#     return [top_10_albums, top_10_albums_songs]
    return
#     return hist_list

def top_overall_artist(album_tracks_list, top_songs_list):
    artist_scores = []
    
    # build data structure of artist: count for artists
    
    artists_list = []
    
    for song in top_songs_list:
        artists_list.append(song['artist'])
        
    for album in album_tracks_list:
        artists_list.append(album['artist'])

    unique_artists = list(set(artists_list))
    
    max_count = 0
    for unique_artist in unique_artists:
        count = 0
        for artist in artists_list:
            if unique_artist == artist:
                count += 1      
        if count > max_count:
            if max_count > 0:
                artist_scores.pop()
            artist_scores.append(unique_artist)
            max_count = count
        
    return artist_scores