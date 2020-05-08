from models.abstract_product import AbstractProduct


class Coffee(AbstractProduct):
    def __init__(self, variety: str, capacity_in_mL: int, packing: str, producer: str,
                 coffee_roasting: str, price_in_UAH):
        super().__init__(variety, capacity_in_mL, packing, producer,
                         coffee_roasting, price_in_UAH)


def __str__(self):
    return "Variety of coffee: " + str(self.variety) + "\n" \
           "Capacity in mL: " + str(self.capacity_in_mL) + "\n" \
           "Packing of coffee: " + str(self.packing) + "\n" \
           "Producer: " + str(self.producer) + "\n" \
           "Type of roasting: " + str(self.coffee_roasting) + "\n" \
           "Price in UAH: " + str(self.price_in_UAH) + "\n"
