import matplotlib.pyplot as plt
#%matplotlib inline

import math
    
def find_by_name(album_name, album_dict):
#str with name of album, return dict of album
    for album in album_dict: 
        if album['album'] == album_name:
            return album
    return None

def find_by_rank(album_number, album_dict):
#numb represents rank, return album with that rank
    for album in album_dict: 
        if int(album['number']) == album_number:
            return album['album']
    return None

def find_by_year(album_year, album_dict):
#take in yr album relseased, returns list returned that year
    album_list = []
    for album in album_dict: 
        if int(album['year']) == album_year:
            album_list.append(album['album'])
    return album_list

def find_by_years(start_year, end_year, album_dict):
#return list albums released on or between start an end year
    albums_list = []
    for album in album_dict:
        if int(album['year']) >= start_year and int(album['year']) <= end_year:
            albums_list.append(album['album'])
    return albums_list

def find_by_ranks(start_number, end_number, album_dict):
#return list of albums ranked between start and end number
    albums_list = []
    for album in album_dict:
        if int(album['number']) >= start_number and int(album['number']) <= end_number:
            albums_list.append(album['album'])
    return albums_list

def all_titles(album_dict):
#return list of titles for each albums
    titles = []
    for album in album_dict:
        titles.append(album['album'])
    return titles

def all_artists(album_dict):
#return list of artists for each album
    album_artist = [album['artist'] for album in album_dict]
    return album_artist

def most_popular_artist(album_dict):
#artist with highest amount of artist in top albums
    counter_dict = {}
    for artist in all_artists(album_dict): #loops over list of the artists for all albums includes repeats
        if artist in counter_dict: #checking to see if artist alread in counter_dict
            counter_dict[artist] += 1 #if it is, increment by 1
        else: #if 
            counter_dict[artist] = 1 #add artist to the dictionary
    maximum_albums = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_albums:
            artist_lists.append(keys) 
    return artist_lists

def most_popular_word(album_dict):
#returns words used most in album titles
    counter_dict = {}
    for title in all_titles(album_dict):
        split_title = [word.lower() for word in title.split()]
        for word in split_title:
            if word in counter_dict:
                counter_dict[word] += 1
            else: 
                counter_dict[word] = 1
    maximum_words = max(counter_dict.values())
    words_list = []
    for keys, values in counter_dict.items():
        if values == maximum_words:
            words_list.append(keys)
    return words_list

def album_by_decade_hist(album_dict):
#return hist of decade pointing to # albums released during decade
    fig,ax = plt.subplots()
    album_year_list = [int(album['year']) for album in album_dict]
    min_year = min(album_year_list)
    max_year = max(album_year_list)
    round_min_year = math.floor(min_year/10) * 10
    round_max_year = math.ceil(max_year/10) * 10
    bin_number = int((round_max_year - round_min_year)/10)
    ax.hist(album_year_list, bins = bin_number, range = (round_min_year, round_max_year))
    ax.set_title('Albums By Decade')
    ax.set_xlabel('Decades')
    ax.set_ylabel('Numbers of Albums');
    
def genre_hist(album_dict):
#hist of each genre pointing to number of albums in that genre
    fig,ax = plt.subplots()
    album_genre_list = [album['genre'] for album in album_dict]
    ax.hist(album_genre_list)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Numbers of Albums');
    ax.set_title('Genre of Albums')
    
def albumWithMostTopSongs(album_track_data, top_song_list):
#return name of artist and album with most songs on top 500
    artist_album_topsongs = []
    # build data structure of artist/album/count of top songs
    top_song = [song['name'] for song in top_song_list]
    max_count = 0
    for album in album_track_data:
        count = 0
        for track in album['tracks']:
            if track in top_song:
                count += 1
        if count > max_count:
            if max_count > 1:
                artist_album_topsongs.pop()
            artist_album_topsongs.append({'artist': album['artist'],
                                          'album': album['album'],
                                          'count': count})
            max_count = count
    return artist_album_topsongs

def album_with_top_songs(top_song_list, album_track_data):
#return list of albums with tracks on top 500 songs
    list_top_songs = [song['name'] for song in top_song_list]
    top_albums = []
    for album in album_track_data:
        for track in album['tracks']:
            if track in list_top_songs: 
                top_albums.append(album['album'])
    return list(set(top_albums))


#def songs_on_top_albums(album_dict, album_track_data):
#LONGreturn list with name of songs features on list of top albums
    #list_top_albums = [album['album'] for album in album_dict]
    #tracks = []
    #for album in album_track_data:
        #if album['album'] in list_top_albums: 
            #for track in album['tracks']:
                #tracks.append(track)
    #return tracks 

def songs_on_top_albums(album_dict, album_track_data):
#SHORTreturn list with name of songs features on list of top albums
    list_top_songs = [song['name'] for song in top_song_list]
    top_albums = []
    for album in album_track_data:
        for track in album['tracks']:
            if track in list_top_songs: 
                top_albums.append(track)
    return list(set(top_albums))
songs_on_top_albums(album_dict, album_track_data)


def top_10_albums_by_top_songs (top_song_list, album_track_data):
#return hist with top 10 albums with most songs on top song list
    list_top_songs = [song['name'] for song in top_song_list]
    top_albums = []
    for album in album_track_data:
        for track in album['tracks']:
            if track in list_top_songs: 
                top_albums.append(album['album'])
    counter_dict = {}
    for album in top_albums: 
        if album in counter_dict: 
            counter_dict[album] += 1 
        else:  
            counter_dict[album] = 1
    list_counter_dict = (counter_dict.items())
    sorted_dic = sorted(list_counter_dict, key = lambda x: x[1], reverse = True)
    top_10 = sorted_dic[0:10]

    album_count_list = []
    for album in range(len(top_10)):
        for count in range(top_10[album][1]):
            album_count_list.append(top_10[album][0])

    fig,ax = plt.subplots()
    ax.hist(album_count_list)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    ax.set_xlabel('Album')
    ax.set_ylabel('Number of Songs on Top 500 Songs List.');
    ax.set_title('Top 10 Albums By Top Songs')
    
def top_overall_artist (album_dict, top_song_list):
#artist with most songs and albums on two lists
    counter_dict = {}
    for artist in all_artists(album_dict): 
        if artist in counter_dict: 
            counter_dict[artist] += 1 
        else:  
            counter_dict[artist] = 1
    for artist in all_artists(top_song_list): 
        if artist in counter_dict: 
            counter_dict[artist] += 1 
        else: 
            counter_dict[artist] = 1
    max_artist = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == max_artist:
            artist_lists.append(keys) 
    return artist_lists