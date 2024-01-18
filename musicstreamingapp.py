"""
You are part of a team developing a new music streaming app called "MFun." Your task is to design the core functionality that manages the user's music library and playlist creation. Consider the following requirements:

Music library:
Needs to store a collection of songs and their associated metadata (title, artist, album, genre, length).
Must efficiently retrieve songs by various criteria (artist, album, genre, title).
Must prevent duplicate song entries.

Playlists:
Users can create unlimited playlists.
Each playlist can contain any number of songs, but a song cannot be added multiple times to the same playlist.
Songs can be added, removed, or reordered within playlists.
The app should display songs in the order they were added to the playlist.

Which data structure model(s) would you choose to implement the music library and playlist features? Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.

Data structures to consider:
       Tuples, Sets, Lists, Dictionaries, Trees, Graphs, Stacks, Queues
"""
# Prototype code, you can follow different implementation process


class Song:
    def __init__(self, title, artist, album , genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length


class MusicLibrary:
    def __init__(self):
        self.songs = {}

    def add_song(self, song):
        if song.title not in self.songs:
            self.songs[song.title] = song
        else:
            print(f"Song '{song.title}' already exists in the library.")

    def get_songs_by_artist(self, artist):
        songs_by_artist = [
            song for song in self.songs.values() if song.artist == artist
        ]
        if songs_by_artist != []:
            print(f"\nSongs by {artist}: ")
            for song in songs_by_artist:
                print(f"{song.title} - {song.album}")
        else:
            print(f'\nNo songs found by {artist}.\n')

    def get_songs_by_album(self, album):
        songs_by_album = [
            song for song in self.songs.values() if song.album == album
        ]
        if songs_by_album != []:
            print(f"\nSongs in {album}: ")
            for song in songs_by_album:
                print(f"{song.title} - {song.artist}")
        else:
            print(f'\nNo songs found in {album}.\n')

    def get_songs_by_genre(self, genre):
        songs_by_genre = [
            song for song in self.songs.values() if song.genre == genre
        ]
        if songs_by_genre != []:
            print(f"\nSongs in {genre}: ")
            for song in songs_by_genre:
                print(f"{song.title} - {song.artist}")
        else:
            print(f'\nNo songs found in {genre}.\n')

    def get_songs_by_title(self, title):
        song = self.songs.get(title)
        if song is not None:
            print(f"{song.title} - {song.artist}")
        else:
            print("No songs found.")
    

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        else:
            print(f"\nSong '{song.title}' already exists in the playlist '{self.name}'.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print(f"\nSong '{song.title}' not found in the playlist '{self.name}'.")

    def display_playlist(self):
        print(f"\nPlaylist: {self.name}")
        for index, song in enumerate(self.songs, start=1):
            print(f"{index}. {song.title} - {song.artist}")


# Main Requirement:
# Create song example
song1 = Song("Starboy", "The Weeknd", "Star Album", "Hip Hop & Rap", "3:30")
song2 = Song("Su Kleat", "Vong Dararathana", "Volume 2", "Hip Hop", "4:15")
song3 = Song("Prek Lerng Srey Kroak Dam Bay", "Him Sivorn", "Volume 27", "Sentimental Ballard", "2:55")

# Create a music library
music_library = MusicLibrary()

# Add songs to the music library
music_library.add_song(song1)
music_library.add_song(song2)

# Create playlists
playlist1 = Playlist("Ego Playlist")
playlist2 = Playlist("The Khmer Farmers Dream Playlist")

# Add songs to playlists
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist2.add_song(song3)

#add duplicate songs
playlist1.add_song(song1)

# Display playlists
playlist1.display_playlist()
playlist2.display_playlist()

# Searching for songs by artist
music_library.get_songs_by_artist("The Weeknd")
music_library.get_songs_by_album("Volume 2")

# if no songs found
music_library.get_songs_by_artist("Artist 1")
music_library.get_songs_by_title("Stueng Saen Paris")

# delete songs from playlist
playlist1.remove_song(song1)

#display playlist 1
playlist1.display_playlist()


# Main Requirement:
# Create song example
# Create a music library
# Add songs to the music library
# Get songs by artist
# Create playlists
# Add songs to playlists
# Display playlists
# Searching for songs by artist

# Sample Output:
# Playlist: My Playlist 1
# 1. Song 1 - Artist 1
# 2. Song 2 - Artist 2

# Songs by Artist 1:
# Song 1 - Album 1
