#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    @abstractmethod
    def coat(self):
        pass

    @property
    @abstractmethod
    def suit(self):
        pass

    @property
    @abstractmethod
    def summ(self):
        pass


class Coat(Clothes):
    def coat(self):
        coatconsumption = v / 6.5 + 0.5
        print(coatconsumption)

    def suit(self):
        pass

    def summ(self):
        pass


class Suit(Clothes):

    def coat(self):
        pass

    def suit(self):
        coatconsumption = 2 * h + 0.3
        print(coatconsumption)

    def summ(self):
        pass


class Summ(Clothes):

    def coat(self):
        pass

    def suit(self):
        pass

    def summ(self):
        summ = (v / 6.5 + 0.5) + (2 * h + 0.3)
        print(summ)


v = 5
h = 4


mc = Coat()
mc.coat()

ms = Suit()
ms.suit()

msm = Summ()
msm.summ()

