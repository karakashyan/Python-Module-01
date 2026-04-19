class Plant:
    def __init__(
        self, name: str = "", height: float = 0.0, days: int = 0
    ) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    rose.show()
    start_height = rose.height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")
