"""Find standard deviation for a geometric variable question."""
def geometric_variable_func(trails_until_success: int, success_rate: float) -> float:
    failure_rate: float = 1 - success_rate
    result: float = 0.0
    result = (failure_rate ** (trails_until_success - 1)) * success_rate 
    return result



def standard_deviation_func(success_rate: float) -> float:
    """produce standard_deviation"""
    variance: float = (1 - success_rate) / success_rate ** 2
    standard_deviation: float = variance ** .5
    return standard_deviation

def main() -> None:
    """Starting point."""
    # collect variables
    trails_until_success: int = int(input("how many trials until first success "))
    success_rate: float = float(input("what is the success rate? "))
    # show results in print
    print(geometric_variable_func(trails_until_success, success_rate))
    print(standard_deviation_func(success_rate))

if __name__ == '__main__':
    main() 