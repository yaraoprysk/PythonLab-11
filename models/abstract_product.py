from abc import ABC


class AbstractProduct(ABC):

    def __init__(self, variety: str, capacity_in_mL: int, packing: str, producer: str,
                 coffee_roasting: str, price_in_UAH):
        self.variety = variety
        self.capacity_in_mL = capacity_in_mL
        self.packing = packing
        self.producer = producer
        self.coffee_roasting = coffee_roasting
        self.price_in_UAH = price_in_UAH
