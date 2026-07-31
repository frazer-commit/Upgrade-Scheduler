from dataclasses import dataclass

@dataclass(frozen=True)
class Upgrade:
    name: str
    cost: float
    rate: float

    @property
    def roi(self) -> float:  # Return On Investment
        return self.cost / self.rate

if __name__ == "__main__":
    u1 = Upgrade("Cursor", 15, 0.1)
    print(u1.roi)
