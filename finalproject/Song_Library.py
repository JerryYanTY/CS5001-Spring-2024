from Song import Song


class Song_Library:
    def __init__(self):
        self.songs_by_artist = {}
        self.songs_by_tag = {}
        self.songs_by_id = {}

    def __contains__(self, song: Song):  # improved overloading thanks to Sami's clarification
        if song.artist in self.songs_by_artist:
            return song in self.songs_by_artist[song.artist]
        return False

    def add_song(self, new_song: Song):
        """
        Add a new Song object to the Song_Library data structure
        :param new_song: a Song object
        :return: nothing
        """
        if new_song not in self:
            if new_song.artist in self.songs_by_artist:
                self.songs_by_artist[new_song.artist].append(new_song)
            else:
                self.songs_by_artist[new_song.artist] = [new_song]
            if new_song.tags:
                for tag in new_song.tags:
                    if tag in self.songs_by_tag:
                        self.songs_by_tag[tag].append(new_song)
                    else:
                        self.songs_by_tag[tag] = [new_song]
            self.songs_by_id[new_song.track_id] = new_song
            return True
        return False

    def by_artist(self):
        """
        :return: The dictionary that maps artists to a set of all their Song objects
        """
        return self.songs_by_artist

    def by_tag(self):
        """
        :return: The dictionary that maps tags to a set of all their Song objects
        """
        return self.songs_by_tag

    def by_id(self):
        """
        :return: The dictionary that maps each id to corresponding Song
        :return:
        """
        return self.songs_by_id

    def artist_song_num(self):
        """
        :return: A dictionary that maps artists to their number of songs
        """
        artist_num = {}
        for artist in self.songs_by_artist:
            artist_num[artist] = len(self.songs_by_artist[artist])
        return artist_num

    def tag_song_num(self):
        """
        :return: A dictionary that maps tags to their number of songs
        """
        tag_num = {}
        for tag in self.songs_by_tag:
            tag_num[tag] = len(self.songs_by_tag[tag])
        return tag_num

    def search_by_artist(self, name: str):
        """
        :param name: The desired name of the artist
        :return: A list of all Song object that matches the artist's name
        """
        if name in self.songs_by_artist:
            return self.songs_by_artist[name]
        else:
            return None

    def search_by_tag(self, tag: str):
        """
        :param tag: The desired tag
        :return: A list of all Song object that matches the tag
        """
        if tag in self.songs_by_tag:
            return self.songs_by_tag[tag]
        else:
            return None

    def search_by_id(self, id: str):
        """
        :param id: string of the id of the song
        :return: a song object
        """
        if id in self.songs_by_id:
            return self.songs_by_id[id]
        else:
            return None

    def popular_tags(self, num: int):
        """
        :param num: top 'num' tags
        :return: a list contains only the top 'num' tags and their corresponding sizes, in tuples
        """
        tag_num = self.tag_song_num()
        if len(tag_num) < num:
            return tag_num
        else:
            sorted_tag_num = sorted(tag_num.items(), key=lambda item: item[1], reverse=True)
            # using sorting method on https://docs.python.org/3/howto/sorting.html
            return sorted_tag_num[:num]

    def hard_working_artist(self, num: int):
        """
        :param num: the number of songs that the artist must have
        :return: a dictionary contains only the artist with 'num' songs and the Song objects
        """
        artist_num = self.artist_song_num()
        result = {}
        for artist in artist_num:
            if artist_num[artist] >= num:
                result[artist] = self.search_by_artist(artist)
        return result


    # def update_similar(self, lib: str, term: str):
    #     if lib == 'tag':
    #         for song in self.songs_by_tag[term]:
    #             count = 0
    #             for track_id in song.similar_songs:
    #                 if track_id in self.songs_by_id:
    #                     song.similar_songs[count] = self.songs_by_id[track_id]
    #                     count += 1
    #                 else:
    #                     song.similar_songs.remove(track_id)
    #
    #     else:
    #         for song in self.songs_by_artist[term]:
    #             count = 0
    #             for track_id in song.similar_songs:
    #                 if track_id in self.songs_by_id:
    #                     song.similar_songs[count] = self.songs_by_id[track_id]
    #                     count += 1
    #                 else:
    #                     song.similar_songs.remove(track_id)
