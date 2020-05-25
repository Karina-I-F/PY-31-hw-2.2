class Animal:
  """ Модель простого животного """
  name = 'Животное'
  weight = 0.1  # kg
  gender = 'ж'
  state = 'Голодный'
  voice = 'Звуки неопределенного животного'

  def get_name(self):
    """ Возвращает имя """
    return self.name

  def get_weight(self):
    """ Возвращает вес """
    return self.weight

  def feed(self):
    """ Кормит животное """
    self.state = 'Голодный'
    answer = input('Чтобы покормить животное введите любой символ: ')
    if answer:
      self.state = 'Сытый'
      print('Животное накормлено.')
    else:
      print(self.state)

  def voice_recognition(self):
    """ Определяет животное по голосу """
    if self.voice == 'Га-га-га':
      print('\nЭто гусь')
    elif self.voice == 'Му-у':
      print('\nЭто корова')
    elif self.voice == 'Бе-е':
      print('\nЭто овца')
    elif self.voice == 'Ме-е':
      print('\nЭто коза')
    elif self.voice == 'Ко-ко-ко':
      print('\nЭто курица')
    elif self.voice == 'Кря-кря':
      print('\nЭто утка')
    else:
      print('\nНе удалось определить животное по голосу')


class Mammal(Animal):
  """ Модель млекопитающего """
  def __init__(self, gender: str):
    self.gender = gender
    self.milk = 'Молока нет'

  def milk(self):
    """ Доит млекопитающее """
    if self.gender == 'ж':
      self.milk = 'Молоко есть'
      answer = input('Чтобы подоить животное введите любой символ: ')
      if answer:
        self.milk = 'Молока нет'
        print('Животное успешно подоено.')
      else:
          print(self.milk)
    else:
      print('Это животное не нужно доить.')


class Sheep(Mammal):
  """ Модель овцы """
  def __init__(self, name: str, weight: float, gender: str):
    self.name = name
    self.weight = weight
    self.gender = gender
    self.voice = 'Бе-е'

  def wool_picking(self):
    """ Стрижёт овцу """
    self.wool = 'Животное обросло'
    answer = input('Чтобы постричь животное введите любой символ: ')
    if answer:
      self.wool = 'Шерсти нет'
      print('Стрижка прошла успешно.')
    else:
      print(self.wool)


class Cow(Mammal):
  """ Модель коровы """
  def __init__(self, name: str, weight: float, gender: str):
    self.name = name
    self.weight = weight
    self.gender = gender
    self.voice = 'Му-у'


class Goat(Mammal):
  """ Модель козы """
  def __init__(self, name: str, weight: float, gender: str):
    self.name = name
    self.weight = weight
    self.gender = gender
    self.voice = 'Ме-е'


class Bird(Animal):
  """ Модель птицы """
  def __init__(self, gender):
    self.gender = gender
    self.eggs = 'Яиц нет'

  def collecting_eggs(self):
    """ Собирает яйца """
    if self.gender == 'ж':
      self.eggs = 'Яйца есть'
      answer = input('Чтобы собрать яйца введите любой символ: ')
      if answer:
        self.eggs = 'Яиц нет'
        print('Яйца успешно собраны.')
      else:
        print(self.eggs)
    else:
      print('Собирать нечего.')


class Chicken(Bird):
  """ Модель курицы """
  def __init__(self, name: str, weight: float, gender: str):
    self.name = name
    self.weight = weight
    self.gender = gender
    self.voice = 'Ко-ко-ко'


class Duck(Bird):
  """ Модель утки """
  def __init__(self, name: str, weight: float, gender: str):
    self.name = name
    self.weight = weight
    self.gender = gender
    self.voice = 'Кря-кря'


class Goose(Bird):
  """ Модель гуся """
  def __init__(self, name: str, weight: float, gender: str):
    self.name = name
    self.weight = weight
    self.gender = gender
    self.voice = 'Га-га-га'


animal_dict = {}

def get_total_weight(dict_for_sum):
  """ Считает общий вес всех животных """
  total_weight = sum(dict_for_sum.values())
  print(f'\nОбщий вес всех животных - {total_weight} кг.')

def get_heaviest_animal(dict_for_heaviest):
  """ Выводит имя самого тяжёлого животного """
  maximum = max(dict_for_heaviest.values())
  for key, value in dict_for_heaviest.items():
    if value == maximum:
      print(f'Самое тяжёлое животное {key} - {maximum} кг.')

goose1 = Goose('Серый', 5, 'м')
goose1.voice_recognition()
goose1.feed()
goose1.collecting_eggs()
animal_dict[goose1.get_name()] = goose1.get_weight()

goose2 = Goose('Белый', 7.1, 'ж')
goose2.voice_recognition()
goose2.feed()
goose2.collecting_eggs()
animal_dict[goose2.get_name()] = goose2.get_weight()

cow = Cow('Манька', 450, 'ж')
cow.voice_recognition()
cow.feed()
cow.milk()
animal_dict[cow.get_name()] = cow.get_weight()

sheep1 = Sheep('Барашек', 90, 'м')
sheep1.voice_recognition()
sheep1.feed()
sheep1.wool_picking()
sheep1.milk()
animal_dict[sheep1.get_name()] = sheep1.get_weight()

sheep2 = Sheep('Кудрявый', 87, 'м')
sheep2.voice_recognition()
sheep2.feed()
sheep2.wool_picking()
sheep2.milk()
animal_dict[sheep2.get_name()] = sheep2.get_weight()

chicken1 = Chicken('Ко-Ко', 2, 'ж')
chicken1.voice_recognition()
chicken1.feed()
chicken1.collecting_eggs()
animal_dict[chicken1.get_name()] = chicken1.get_weight()

chicken2 = Chicken('Кукареку', 2.5, 'м')
chicken2.voice_recognition()
chicken2.feed()
chicken2.collecting_eggs()
animal_dict[chicken2.get_name()] = chicken2.get_weight()

goat1 = Goat('Рога', 45, 'м')
goat1.voice_recognition()
goat1.feed()
goat1.milk()
animal_dict[goat1.get_name()] = goat1.get_weight()

goat2 = Goat('Копытка', 50, 'ж')
goat2.voice_recognition()
goat2.feed()
goat2.milk()
animal_dict[goat2.get_name()] = goat2.get_weight()

duck = Duck('Кряква', 2, 'ж')
duck.voice_recognition()
duck.feed()
duck.collecting_eggs()
animal_dict[duck.get_name()] = duck.get_weight()

get_total_weight(animal_dict)
get_heaviest_animal(animal_dict)