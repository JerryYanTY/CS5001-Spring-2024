class Song:
    def __init__(self, artist, title, track_id ='', similar=None, tags=None):
        if similar is None:
            similar = []
        if tags is None:
            tags = []
        self.artist = artist
        self.title = title
        self.tags = tags
        self.similar_songs = similar
        self.track_id = track_id

    def __eq__(self, other):
        """
        This function is used to overload the == operator. Two song objects are only equal if they
        have the same title and the same artist.
        :param other: the other song object to be compared with
        :return: if both objects share the same title and artist
        """
        return self.title == other.title and self.artist == other.artist

    def debug(self):
        print(self.artist, self.title, self.tags)
