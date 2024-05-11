from Song import Song
import unittest


class SongTest(unittest.TestCase):
    def test_init(self):
        song = Song('MJ', 'Beat It', ['rock'])
        self.assertEqual(song.artist, 'MJ')
        self.assertEqual(song.title, 'Beat It')
        self.assertEqual(song.tags, ['rock'])

    def test_no_tag(self):
        song = Song('MJ', 'Beat It')
        self.assertEqual(song.artist, 'MJ')
        self.assertEqual(song.title, 'Beat It')
        self.assertEqual(song.tags, [])

    def test_eq_overload(self):
        song = Song('MJ', 'Beat', ['rock'])
        other = Song('MJ', 'Beat', ['rock'])
        self.assertTrue(song == other)


if __name__ == '__main__':
    unittest.main()
