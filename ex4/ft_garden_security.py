class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._days += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._days = days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25.0)
    print(f"Height updated: {int(rose.get_height())}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    rose.set_height(-5.0)
    print("Height update rejected")
    rose.set_age(-1)
    print("Age update rejected")
    print("Current state: ", end="")
    rose.show()
