from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise TypeError('error')
    print(f"moveu para {direction.name}")


move(Directions.right)
move(Directions.left)
move(Directions.up)

print()
for direction in Directions:
    print(f"{direction} ## {direction.value} ## {direction.name}")
