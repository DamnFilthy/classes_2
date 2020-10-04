# Класс жизнь
class Life:
    # Каждое животное дышит
    def breath(self):
        return 'Oooh..'
    # и какает :)
    def poo(self):
        return 'poop'

# Класс животные
class Animals(Life):
    # Инициализируем атрибуты
    def __init__(self):
        self.type_data = []
        self.name_data = []
        self.weight_data = []
        self.cry_data = []

        # Добавляем информацию о животных
    def add_specifications(self, animal):
        self.type_data.append(animal.type)
        self.name_data.append(animal.name)
        self.weight_data.append(animal.weight)
        self.cry_data.append(animal.cry)
        # Выводим информацию о животных
    def get_specifications(self):
        return self.type_data, self.name_data, self.weight_data, self.cry_data
        # Считаем общий вес животных
    def calculate_weight(self):
        result = 0
        for animal in self.weight_data:
            result += animal
        return result
        # Получаем самый большой вес
    def get_max_weight(self):
        return max(self.weight_data)
        # Выводим имя животного с самым большим весом
    def info_max_weight_animal(self):
        for id, i in enumerate(self.weight_data):
            if i == max(self.weight_data):
                return self.name_data[id]
    def morning_cry(self):
        for i in self.cry_data:
            print(i)
# Класс птица
class Bird(Animals):
    # Инициализируем атрибуты
    def __init__(self, type, name, weight, cry):
        self.type = type
        self.name = name
        self.weight = weight
        self.cry = cry

        # Собственный крик
    def get_cry(self):
        return self.cry
        # Метод - покушать
    def set_eat(self, food):
        self.weight += food
        # какает по своему
    def poo(self):
        return 'KeK'
        # Собираем яйца
    def get_eggs(self):
        return print('eggs collected')
        # Возвращает имя животного
    def get_name(self):
        return self.name
        # Возвращает тип животного
    def get_type(self):
        return self.type
# Класс Крупного рогатого скота
class Cattle(Animals):
    # Инициализируем атрибуты
    def __init__(self, type, name, weight, cry):
        self.type = type
        self.name = name
        self.weight = weight
        self.cry = cry

        # Собственный крик
    def get_cry(self):
        return self.cry
        # Метод - покушать
    def set_eat(self, food):
        self.weight += food
        # Доим
    def get_milk(self):
        return print('milk collected')
        # Возвращает имя животного
    def get_name(self):
        return self.name
        # Возвращает тип животного
    def get_type(self):
        return self.type

# Класс овца
class Sheep(Animals):
    # Инициализируем атрибуты
    def __init__(self, type, name, weight, cry):
        self.type = type
        self.name = name
        self.weight = weight
        self.cry = cry

        # Собственный крик
    def get_cry(self):
        return self.cry
        # Метод - покушать
    def set_eat(self, food):
        self.weight += food
        # Дышит по другому
    def breath(self):
        return 'EheeEhhee'
        # Стрижем
    def get_wool(self):
        return print('wool collected')
        # Возвращает имя животного
    def get_name(self):
        return self.name
        # Возвращает тип животного
    def get_type(self):
        return self.type


# Создаем объект на основе класс птицы
duck = Bird('Утра', 'Кря', 12, 'kryaaaa')
print(f'{duck.get_name()} дышит {duck.breath()} и {duck.poo()}')
print(f'{duck.get_type()} кричит {duck.get_cry()}')

# Собираем и кормим
duck.get_eggs()
duck.set_eat(1)
print('\n')

# Создаем объект на основе класса рогатых
cow = Cattle('Корова', 'Буренка', 79, 'moooo')
print(f'{cow.get_name()} дышит {cow.breath()} и {cow.poo()}')
print(f'{cow.get_type()} кричит {cow.get_cry()}')

# Собираем и кормим
cow.get_milk()
cow.set_eat(5)
print('\n')

# Создаем объект на основе класса овец
ram = Sheep('Баран', 'Кучерявый', 37, 'beeee')
print(f'{ram.get_name()} дышит {ram.breath()} и {ram.poo()}')
print(f'{ram.get_type()} кричит {ram.get_cry()}')
# Собираем и кормим
ram.get_wool()
ram.set_eat(8)
print('\n')
# Создаем объект на основе класса животных
farm_animals = Animals()
# Добавляем информацию о животных
farm_animals.add_specifications(duck)
farm_animals.add_specifications(cow)
farm_animals.add_specifications(ram)
farm_animals.morning_cry()
print('\n')
# Выводим информацию о животных
print(farm_animals.get_specifications())
# Считаем общий вес
print(farm_animals.calculate_weight())
# Получаем самый большой вес
print(farm_animals.get_max_weight())
# Получаем имя животного с самым большим весом
print(farm_animals.info_max_weight_animal())
