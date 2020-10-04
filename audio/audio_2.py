# Создаем класс Album
class Album:
    # Инициализируем атрибуты класса
    def __init__(self, name):
        # Хранилище для имен песен в альбоме
        self.data = []
        # Хранилище для времени песен
        self.duration = []
        # Имя альбома
        self.name = name

    def add_track(self, track):
        # Добавляем в хранилище имен - имя песни
        self.data.append(track.name)
        # Добавляем в хранилище времени - длину песни
        self.duration.append(track.duration)

    def get_all_tracks(self):
        # Выводим список всех имен песен
        return self.data
    def __str__(self):
        return f' album {self.name}, треки {self.data} длина {self.duration}'

    def get_album_info(self):
        # Выводим имя альбома
        return self.name

    def get_album_duration(self):
        # Считаем время всех песен альбома
        result = 0
        for track in self.duration:
            result += track
        return round(result, 2)

# Создаем класс Track
class Track():
    # Инициализруем атрибуты
    def __init__(self, name, duration):
        # Имя песни
        self.name = name
        # Длина песни
        self.duration = duration

    # def get_info(self):
    #     # Получаем информацию по конкретной песне
    #     return self.name, self.duration
    def __str__(self):
        return f' song {self.name} : {self.duration}'

    def __lt__(self, other):
        return self.duration > other.duration

# Создаем первые три песни
song_1 = Track('pain', 3.14)
song_2 = Track('suffering', 7.77)
song_3 = Track('unhappy', 4.12)
# Создаем вторые три песни
song_4 = Track('love', 2.18)
song_5 = Track('wow', 1.45)
song_6 = Track('somebody', 4.55)

# print(song_1.get_info())
print(song_1, song_2, song_3)
# Сравниваем треки по длительности
print(song_1 > song_2)
print('\n')

# Создаем два альбома
album_1 = Album('Painfull')
album_2 = Album('Happyness')
# Добавляем песни в первый альбом
album_1.add_track(song_1)
album_1.add_track(song_2)
album_1.add_track(song_3)
# Добавляем песни во второй альбом
album_2.add_track(song_4)
album_2.add_track(song_5)
album_2.add_track(song_6)
print(album_1)
print(album_2)
print('\n')

# Выводим информацию по альбомам
print(f'Album: {album_1.get_album_info()} tracks: {album_1.get_all_tracks()} \
Общая длинна альбома: {album_1.get_album_duration()} минут')
print(f'Album: {album_2.get_album_info()} tracks: {album_2.get_all_tracks()} \
Общая длинна альбома: {album_2.get_album_duration()} минут')
