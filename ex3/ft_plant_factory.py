class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"Created: {self.name}: {round(self.height, 1)}cm, "
              f"{self.days} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()

    oak = Plant("Oak", 200.0, 365)
    oak.show()

    cactus = Plant("Cactus", 5.0, 90)
    cactus.show()

    sunflower = Plant("Sunflower", 80.0, 45)
    sunflower.show()

    fern = Plant("Fern", 15.0, 120)
    fern.show()
