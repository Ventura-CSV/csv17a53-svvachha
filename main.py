from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    
    keys = list(mapping.keys())

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            x1 = keys[i]
            x2 = keys[j]

            if mapping[x1] == mapping[x2]:
                return (x1, x2)

    return None


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    
    values = set(mapping.values())

    for element in target:
        if element not in values:
            return element

    return None


def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    pass


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    pass