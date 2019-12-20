from abc import ABC, abstractmethod


class AbstractWheel(ABC):  # колесо
    """
    Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс.
    Все вариации продукта должны реализовывать этот интерфейс.
    """

    @abstractmethod
    def inflate(self) -> str:  # надуть колесо
        pass


"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteWheelCar(AbstractWheel):  # колесо автомобиля
    def inflate(self) -> str:  # надуть колесо
        return "Надутое колесо автомобиля"


class ConcreteWheelBicycle(AbstractWheel):  # колесо велосипеда
    def inflate(self) -> str:  # надуть колесо
        return "Надутое колесо велосипеда"


class AbstractTransport(ABC):  # средство передвижения
    """
    Базовый интерфейс другого продукта. Все продукты могут взаимодействовать
    друг с другом, но правильное взаимодействие возможно только между продуктами
    одной и той же конкретной вариации.
    """
    @abstractmethod
    def ride(self) -> None:  # ехать
        """
        Продукт Б способен работать самостоятельно...
        """
        pass

    @abstractmethod
    def set_wheel(self, collaborator: AbstractWheel) -> None:  # установить колесо
        """
        ...а также взаимодействовать с Продуктами А той же вариации.

        Абстрактная Фабрика гарантирует, что все продукты, которые она создает,
        имеют одинаковую вариацию и, следовательно, совместимы.
        """
        pass


"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteTransportCar(AbstractTransport):  # конкретное средство передвижения: автомобиль
    def ride(self) -> str:  # ехать
        # проверить колеса: если надо, установить и надуть колеса
        # завести двигатель
        # нажать на педаль газа
        return "Едем на автомобиле"

    """
    Продукт Б1 может корректно работать только с Продуктом A1. Тем не менее, он
    принимает любой экземпляр Абстрактного Продукта А в качестве аргумента.
    """

    def set_wheel(self, collaborator: AbstractWheel) -> str:  # установить колесо(абстрактное колесо)
        result = collaborator.inflate()  # надули колесо
        return f"Результат установки на автомобиль компонента ({result})"


class ConcreteTransportBicycle(AbstractTransport):  # конкретное средство передвижения: велосипед
    def ride(self) -> str:  # ехать
        # проверить колеса: если надо, установить и надуть колеса
        # снять замок
        # крутить педали
        return "Едем на велосипеде"

    def set_wheel(self, collaborator: AbstractWheel):  # установить колесо(абстрактное колесо)
        """
        Продукт Б2 может корректно работать только с Продуктом A2. Тем не менее,
        он принимает любой экземпляр Абстрактного Продукта А в качестве
        аргумента.
        """
        result = collaborator.inflate()
        return f"Результат установки на велосипед компонента ({result})"


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и связаны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимодействовать между собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """
    @abstractmethod
    def create_wheel(self) -> AbstractWheel:  # создать колесо
        pass

    @abstractmethod
    def create_transport(self) -> AbstractTransport:  # создать средство передвижения
        pass


class ConcreteFactoryCar(AbstractFactory):  # будем работать с автомобилем
    """
    Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
    гарантирует совместимость полученных продуктов. Обратите внимание, что
    сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, в то
    время как внутри метода создается экземпляр конкретного продукта.
    """

    def create_wheel(self) -> ConcreteWheelCar:  # создать колесо автомобиля
        return ConcreteWheelCar()

    def create_transport(self) -> ConcreteTransportCar:  # создать автомобиль
        return ConcreteTransportCar()


class ConcreteFactoryBicycle(AbstractFactory):  # будем работать с велосипедом
    """
    Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
    """

    def create_wheel(self) -> ConcreteWheelBicycle:  # создать колесо велосипеда
        return ConcreteWheelBicycle()

    def create_transport(self) -> ConcreteTransportBicycle:  # создать велосипед
        return ConcreteTransportBicycle()


def client_code(factory: AbstractFactory) -> None:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    wheel = factory.create_wheel()  # создем какое-то колесо
    transport = factory.create_transport()  # создаем какое-то средство передвижения

    # устанавливаем на какое-то средство передвижения какое-то колесо
    print(f"{transport.set_wheel(wheel)}")
    print(f"{transport.ride()}")  # едем


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Клиент: Тестируем код клиента с фабрикой автомобилей:")
    client_code(ConcreteFactoryCar())

    print("\n")

    print("Клиент: Тестируем код клиента с фабрикой велосипедов:")
    client_code(ConcreteFactoryBicycle())
