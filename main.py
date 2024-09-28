class Animal:
    """Класс животных"""
    alive = True            # живой / неживой
    fed = False             # накормленный / голодный
    name = None             # индивидуальное название каждого животного
    def eat(self, food):
        if food.edible:  # если растение съедобное
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    """Класс растений"""
    edible = False          # съедобный / несъедобный
    name = None             # индивидуальное название каждого растения



class Mammal(Animal):
    """Дочерний класс от класса животных.
    Ему доступен метод eat() из родительского класса"""
    def __init__(self, name):
        self.name = name    # переопределяем атрибут name


class Predator(Animal):
    """Дочерний класс от класса животных.
    Ему доступен метод eat() из родительского класса"""
    def __init__(self, name):
        self.name = name    # переопределяем атрибут name


class Flower(Plant):
    """Дочерний класс от класса растений.
    Ему доступны атрибуты из родительского класса"""
    def __init__(self, name):
        self.name = name    # переопределяем атрибут name


class Fruit(Plant):
    """Дочерний класс от класса растений.
    Ему доступны атрибуты из родительского класса"""
    def __init__(self, name):
        self.name = name    # переопределяем атрибут name
        self.edible = True  # переопределяем атрибут на съедобный


if __name__ == '__main__':

# Выполняемый код(для проверки):
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
