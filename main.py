# TODO Написать 3 класса с документацией и аннотацией типов
class PC:
    def init(self, memory_ram: int, SSD_space: int):
        if not isinstance(memory_ram, int):
            raise TypeError("Объем памяти должен быть типа int")
        if memory_ram <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.memory_ram = memory_ram

        if not isinstance(SSD_space, (int, float)):
            raise TypeError("Размер SSD должен быть типа int")
        if SSD_space <= 0:
            raise ValueError("Размер дисплея должен быть положительным числом")
        self.SSD_space = SSD_space

    def on(self):
        ... #включить комп

    def off(self):
        ... #выключить комп
    class Dog:
        def init(self, age: int, paw: int):
            if not isinstance(age, int):
                raise TypeError("Возраст пса должен быть типа int")
            if age <= 0:
                raise ValueError("Возраст пса должен быть положительным числом")
                self.age = age

            if not isinstance(paw, int):
                raise TypeError("Количество лап должно быть типа int")
            if paw <= 0:
                raise ValueError("Количество лап должно быть положительным числом")
            self.paw = paw

    def play_with_dog(self):
        ... #играем с псом

    def feed_the_dog(self):
        ... #кормим пса
class Bath:
    def init(self, valume: int):
        if not isinstance(valume, int):
            raise TypeError("Объем ванны должен быть типа int")
        if valume <= 0:
            raise ValueError("Объем ванны должен быть положительным числом")
        self.valume = valume



    def drain_the_bath(self):
        ... #сливаем ванну

    def fill_the_bath(self):
        ... #наполняем ванну

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
