"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730531580"


class Simpy:
    """Simps for NumPy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Helper to initialize attributes."""
        self.values = values

    def __str__(self) -> str:
        """"Initializes name as a string."""
        result: str = "Simpy(["
        for i in range(len(self.values)):
            value: str = str(self.values[i])
            # If it's the last value we don't want to concate ', '.
            if i == len(self.values) - 1:
                result += f"{value}])"
            else:
                value: str = str(self.values[i])
                result += f"{value}, "
        return result

    def fill(self, recurring: float, how_many: int) -> None:
        """Function that adds a recurring value to a list."""
        self.values = []
        i: int = 0
        while i < how_many:
            self.values.append(recurring)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills a list of floats within a range of numbers."""
        self.values: list[float] = []
        assert step != 0.0
        i: float = start
        while i < stop:
            self.values.append(i)
            i += step

    def sum(self) -> float:
        """Sum all values in values attribute."""
        result: float = 0.0
        for value in self.values:
            result += value
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overload add operator for Simpy class."""
        # Conditional to determine the type of the rhs.
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        elif isinstance(rhs, float):
            for value in self.values: 
                result.values.append(value + rhs)
        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overload the power operator for Simpy class."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        # Personally had to add this reduancy to make jupyter not produce an error.
        elif isinstance(rhs, float):
            for value in self.values: 
                result.values.append(value ** rhs)
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overload the equals operator for Simpy class."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        # Personally had to add this reduancy to make jupyter not produce an error.
        elif isinstance(rhs, float):
            for value in self.values: 
                result.append(value == rhs)
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overload the greater than operator for Simpy class."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        # Personally had to add this reduancy to make jupyter not produce an error.
        elif isinstance(rhs, float):
            for value in self.values: 
                result.append(value > rhs)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription operator for Simpy class."""
        if isinstance(rhs, int):
            assert len(self.values) > rhs
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])
            assert len(rhs) == len(self.values)
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self.values[i])
            return result