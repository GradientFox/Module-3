from typing import List, Union
import doctest



class Engine:
    """
    Двигатель
    """
    def __init__(self, power: int, fuel: str) -> None:
        """
        Конструктор

        :param power: int: Мощность двигателя
        :param fuel: str: Тип топлева
        """
        self._power: int = power
        self._fuel: str = fuel
    
    def get_info(self) -> str:
        """
        Вывод информации

        :return: str: Сводная информация о двигателе
        """
        return f"Мощность: {self._power}\nТопливо: {self._fuel}"
    
    def get_fuel(self) -> str:
        """
        Получение содержимого скрытого свойства

        :return: str: Топливо подходящее для этого двигателя
        """
        return self._fuel
    
class CarBody:
    """
    Кузов машины
    """
    def __init__(self, body: str, doors: int) -> None:
        """
        Конструктор

        :param body: str: Тип кузова
        :param doors: int: Количество дверей
        """
        self._body: str = body
        self._doors: int = doors
    
    def get_info(self) -> str:
        """
        Вывод информации

        :return: str: Сводная информация о кузове машины
        """
        return f"Тип кузова: {self._body}\nКоличество дверей: {self._doors}"

class Wheel:
    """
    Колесо
    """
    def __init__(self, diameter: Union[int, float], tire: str) -> None:
        """
        Консруктор

        :param diameter: Union[int, float]: Диаметр колеса
        :param tire: str: Тип резины 
        """

        self._diameter: Union[int, float] = diameter
        self._tire: str = tire
    
    def get_info(self) -> str:
        """
        Вывод информации

        :return: str: Сводная информация о колесе
        """
        return f"Диаметр: {self._diameter}\nТип резины: {self._tire}"

class Car:
    """
    Машина
    """
    def __init__(self, body: str="седан", doors: int=4, power: int=100, fuel: str="бензин", wheel_diameter: int=16, tire: str="летняя") -> None:
        """
        конструктор машины
        """
        self._car_body: CarBody = CarBody(body, doors)
        self._engine: Engine = Engine(power, fuel)
        self._wheels: List[Wheel] = [Wheel(wheel_diameter, tire) for _ in range(4)]

    def display_engine_info(self) -> str:
        """
        Вывод информации о двигателе
        """
        return f"Двигатель:\n{self._engine.get_info()}"
    
    def display_car_body_info(self) -> str:
        """
        Вывод информации о кузове
        """
        return f"Кузов:\n{self._car_body.get_info()}"

    def display_wheel_info(self) -> str:
        """
        Вывод информации о колесах
        """
        return f"Колеса:\n{'\n'.join([wheel.get_info() for wheel in self._wheels])}"
    
    def start(self, fuel: str) -> str:
        """
        Запуск двигателя с указанием залитого топлива в бак
        
        :param fuel: str: Залитое топливо.
        :return: str: Двигатель запущен
        :raise ValueError: Залито неверное топливо

        >>> car = Car(body="внедорожник", doors=6, power=250, fuel="дизель", wheel_diameter=20, tire="зимняя")
        >>> car.start("дизель")
        'Двигатель запущен'
        >>> car.start("бензин")
        Traceback (most recent call last): 
        ValueError: Залито неверное топливо
        """
        if fuel != self._engine.get_fuel():
            raise ValueError("Залито неверное топливо")
        return "Двигатель запущен"



car1 = Car()
car2 = Car(body="внедорожник", doors=6, power=250, fuel="дизель", wheel_diameter=20, tire="зимняя")
car3 = Car(body="седан", doors=2, wheel_diameter=18.5, tire="зимняя")

print(car1.display_car_body_info(), car2.display_car_body_info(), car2.display_engine_info(), car3.display_engine_info(), car3.display_wheel_info(), sep="\n\n")


doctest.testmod()