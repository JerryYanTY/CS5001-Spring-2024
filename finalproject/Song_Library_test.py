from Song import Song
from Song_Library import Song_Library
import unittest

song_one = Song('MJ', 'Beat It', ['rock'])
other = Song('MJ', 'Beat It', ['rock'])
song_two = Song('MJ', 'Bad', ['pop', 'rock'])
song_three = Song('JB', 'Baby', ['pop', 'rap'])


class SongLibraryTest(unittest.TestCase):
    def test_add_dupes(self):
        songs = Song_Library()
        songs.add_song(song_one)
        self.assertEqual(songs.songs_by_tag, {'rock': [song_one]})
        songs.add_song(other)
        self.assertEqual(songs.songs_by_artist, {'MJ': [song_one]})
        self.assertEqual(songs.songs_by_tag, {'rock': [song_one]})

    def test_add_general(self):
        songs = Song_Library()
        songs.add_song(song_one)
        songs.add_song(song_two)
        songs.add_song(song_three)
        self.assertEqual(songs.songs_by_tag, {'rock': [song_one, song_two], 'pop': [song_two, song_three],
                                              'rap': [song_three]})
        self.assertEqual(songs.songs_by_artist, {'MJ': [song_one, song_two], 'JB': [song_three]})

    def test_search_name(self):
        songs = Song_Library()
        songs.add_song(song_one)
        songs.add_song(song_two)
        songs.add_song(song_three)
        self.assertEqual(songs.search_by_artist('MJ'), [song_one, song_two])

    def test_search_tag(self):
        songs = Song_Library()
        songs.add_song(song_one)
        songs.add_song(song_two)
        songs.add_song(song_three)
        self.assertEqual(songs.search_by_tag('rock'), [song_one, song_two])

    def test_hw_artist(self):
        songs = Song_Library()
        songs.add_song(song_one)
        songs.add_song(song_two)
        songs.add_song(song_three)
        self.assertEqual(songs.hard_working_artist(2), {'MJ': [song_one, song_two]})


if __name__ == '__main__':
    unittest.main()
