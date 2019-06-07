from dataclasses import dataclass
@dataclass
class Armor:
    armor: float
    description: str
    level: int = 1

    def power(self) -> float:
        return self.armor * self.level

armor = Armor(5.2, "Common armor.", 2)
armor.power()

print(armor)