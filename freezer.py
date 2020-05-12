class Freezer:
    store = "Epicenter"

    def __init__(self, producer="LG", total_volume=0, weight_in_kilogramms=0, consuming_power_in_watts=0,
                 body_material="aluminum", color="grey", country_where_produced="Italy"):
        self.producer = producer
        self.total_volume = total_volume
        self.weight_in_kilogramms = weight_in_kilogramms
        self.consuming_power_in_watts = consuming_power_in_watts
        self.body_material = body_material
        self.color = color
        self.country_where_produced = country_where_produced

    def __str__(self):
        return \
            f"producer: {self.producer}\n" \
            f"total_volume: {self.total_volume}\n" \
            f"weight_in_kilogramms: {self.weight_in_kilogramms}\n" \
            f"consuming_power_in_watts: {self.consuming_power_in_watts}\n" \
            f"body_material: {self.body_material}\n" \
            f"color: {self.color}\n" \
            f"country_where_produced: {self.country_where_produced}\n"

    def __del__(self):
        print("deleting instance of Freezer class")

    @staticmethod
    def get_store():
        return Freezer.store


if __name__ == '__main__':
    firstFreezer = Freezer("LG", 30, 40, 4, "aluminum", "metallic gray", "Germany")
    secondFreezer = Freezer("Bosch", 40, 50, 6, "steel")
    thirdFreezer = Freezer("Samsung", 20, 30, 3, "plastic")

    print(firstFreezer)
    print(secondFreezer)
    print(thirdFreezer)
