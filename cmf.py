"""Culmative Distribution Functions."""

from geometric_sigma import standard_deviation_func

def sum(values: list[float]) -> float:
    result: float = 0.0
    for value in values:
        result += value
    return result

def factorial_func(var: int) -> int:
    """gives factorial of any integer input."""
    factors: list[int] = list()
    i: int = 0
    # make a list of (x-1), (x - 2) to [x- (x-1)]
    while i < var:
        factors.append(var - i)
        i += 1
    # multiple all integers in the list together by iterating thru with for...in loop
    factorial: int = 1
    for factor in factors:
        factorial = factor * factorial
    print(f"Factorial of {var} is {factorial})")
    return factorial


def combinations_func(trials: int, amount_successes: int) -> int:
    """determines the total amount of combinations for amount of a certain outcome given n trials"""
    amount_failures: int = trials - amount_successes
    trials_factorial: int = factorial_func(trials)
    amount_certain_outcome_factorial: int = factorial_func(amount_successes)
    compliment_factorial: int = factorial_func(amount_failures)
    # idk how this actually works but it's the formula
    print(f"{trials_factorial} / ({amount_certain_outcome_factorial} * {compliment_factorial}) = {trials_factorial / (amount_certain_outcome_factorial * compliment_factorial)}")
    return trials_factorial / (amount_certain_outcome_factorial * compliment_factorial)



# gather inputs from user
def probability_mass_func(trials: int, amount_successes: int, success_rate: float) -> list[float]:

    probability_mass_values: list[float] = []

    # probability of not certain outcome
    probability_compliment: float = 1 - success_rate

    # figure out total number of combinations
    combinations: int = combinations_func(trials, amount_successes)

    # Log
    print(combinations * (probability_compliment ** (trials - amount_successes)) * (success_rate ** amount_successes))

    # append to a referenced list to store a list of values as we iterate thru this function
    probability_mass: float = combinations * (probability_compliment ** (trials - amount_successes)) * (success_rate ** amount_successes)
    probability_mass_values.append(probability_mass)
    
    return probability_mass_values

def main() -> None:
    trials: int = int(input("how many trials are we doing? (integers only please) "))
    outcome_limit: int = int(input("what is the most amount of this outcome? "))
    success_rate: float = float(input("how likely is this outcome? "))

    #iterate thru pmf until we reach limit
    i: int = 0
    while i <= outcome_limit:
        probability_mass_values: list[float] = probability_mass_func(trials, i, success_rate)
        i += 1
    cmf = sum(probability_mass_values)

    print(f"cmf is {cmf}")

    standard_deviation: float = standard_deviation_func(success_rate)
    print(f"standard deviation for geometric variable is {standard_deviation}")

if __name__ == '__main__':
    main()


