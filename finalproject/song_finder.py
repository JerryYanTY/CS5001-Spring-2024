import os
import sys
import json
from Song import Song
from Song_Library import Song_Library
from flask import Flask, render_template, request

app = Flask(__name__)

CHOICE = ['a', 'b', 'c', 'd', 'e']


def read_file(dirty):
    """
    Read all .json files within one directory and return a Song_Library object
    :param dirty (the directory string)
    :return: a Song_Library object
    """
    #     # resources used to learn input files within one directory:
    #     # https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
    all_songs = Song_Library()
    os.chdir(dirty)
    for root, subdir, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.json'):
                json_path = os.path.join(root, filename)
                with open(json_path) as song_data:
                    file = json.load(song_data)
                    tags = file['tags']
                    refined_tag = []
                    for item in tags:
                        refined_tag.append(str(item[0]))
                    similars = file['similars']
                    refined_similars = []
                    for item in similars:
                        refined_similars.append(str(item[0]))
                    song = Song(file['artist'], file['title'], file['track_id'], refined_similars, refined_tag)
                    all_songs.add_song(song)
    return all_songs


songs_library = read_file('lastfm_subset')


@app.route('/')
def home_page():
    result = songs_library.popular_tags(10)  # show top 10 tags
    return render_template('home_page.html', items=result)


@app.route('/search')
def search_songs():
    criterion = request.args.get('search_criterion')
    term = request.args.get('search_term')  # get the needed info/keys
    search_result = []
    if criterion == 'tag':
        if term in songs_library.songs_by_tag:
            search_result = songs_library.songs_by_tag[term]
            # songs_library.update_similar('tag',term)
    else:
        if term in songs_library.songs_by_artist:
            search_result = songs_library.songs_by_artist[term]
            # songs_library.update_similar('artist',term)

    return render_template('search_result.html', items=search_result, term=term, crit=criterion)


@app.route('/new_song')
def new_song():
    title = request.args.get('new_song_title')
    artist = request.args.get('new_song_artist')
    tag = [request.args.get('new_song_tag')]
    new_song_obj = Song(artist, title, tags=tag)
    added = songs_library.add_song(new_song_obj)
    return_message = ''
    if added:
        return_message = 'Successfully added.'

    else:
        return_message = 'Failed to add.'
    return render_template('add_result.html', result=return_message)


@app.route('/database/<song>')
def get_info(song: str):
    this_song = songs_library.songs_by_id[song]  # find song obj by id
    title = this_song.title
    artist = this_song.artist
    track_id = this_song.track_id
    tag = this_song.tags  # self-explanatory
    similar_song = []
    for similar in this_song.similar_songs:
        if similar in songs_library.songs_by_id:
            similar_song.append(songs_library.songs_by_id[similar])
    return render_template('song_info.html', id=track_id, title=title, artist=artist, tags=tag,
                           similar_song=similar_song)


@app.route('/add_tag/<song>')
def add_tag(song: str):   # very similar to new_song()
    new_tag = request.args.get('new_tag')
    this_song = songs_library.songs_by_id[song]
    return_message = ''
    if new_tag not in this_song.tags:
        this_song.tags.append(new_tag)
        if new_tag in songs_library.songs_by_tag:
            songs_library.songs_by_tag[new_tag].append(this_song)
        else:
            songs_library.songs_by_tag[new_tag] = [this_song]
        for song in songs_library.songs_by_artist[this_song.artist]:
            if song.title == this_song.title:
                song = this_song   # updating the other two data structure
        return_message = 'Successfully added.'
    else:
        return_message = 'Failed to add.'
    return render_template('add_result.html', result=return_message)
