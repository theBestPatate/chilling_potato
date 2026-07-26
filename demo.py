"""chilling-potato demo — a tour of syntax highlighting."""

import os
from dataclasses import dataclass
from typing import Optional, Callable

# TODO: add more recipes — especially soups
RECIPES = ["gazpacho", "borscht", "vichyssoise"]


@dataclass
class Potato:
    """A humble tuber with ambition."""

    name: str
    temperature: float = 20.0
    seasoned: bool = False

    def chill(self, degrees: float = 5.0) -> None:
        self.temperature -= degrees
        if self.temperature < 0:
            raise ValueError("Potato is frozen solid!")

    def season(self, *spices: str) -> str:
        self.seasoned = True
        return f"Seasoned with {', '.join(spices)}"


def cook(potato: Potato, method: Callable[[Potato], str] | None = None) -> str:
    """Apply heat to a potato. Returns a status string."""
    if method is None:
        return f"{potato.name} is raw at {potato.temperature}°C"
    return method(potato)


if __name__ == "__main__":
    p = Potato(name="russet", temperature=22.5)
    p.season("salt", "pepper", "paprika")
    print(cook(p))