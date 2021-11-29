"""Statistical probabiliites with a Sample of population."""
from typing import Union
from scipy.stats import norm

Z: float = 1.645


def average(myList: list[int]) -> int:
    sum: int = 0
    for i in myList:
        sum += i
    sample_average: float = sum / len(myList)
    return sample_average


class Sample:
    sample_size: int
    expected_value: float
    sample_average: int
    pop_standard_deviation: float
    standard_error: Union[None, float]
    z_score: Union[None, float]
    sample_standard_deviation: Union[float, None]

    def __init__(self, sample_size: int, expected_value: Union[float, None], sample_average: Union[None, int], pop_standard_deviation: float, standard_error: Union[float, None], z_score: Union[float, None], sample_standard_deviation: Union[float, None]):
        """Constructor definition for initialization of attributes."""
        self.sample_size = sample_size
        self.expected_value = expected_value
        self.sample_average = sample_average
        self.pop_standard_deviation = pop_standard_deviation
        self.standard_error = standard_error
        self.z_score = z_score
        self.sample_standard_deviation = sample_standard_deviation

    def z_value_population(self):
        z: float = 0.0
        z = (self.sample_average - self.expected_value) / self.pop_standard_deviation
        print(f"z value is {z}")
        return z 

    def z_value_sample(self):
        z: float = 0.0
        z = (self.sample_average - self.expected_value) / (self.pop_standard_deviation / (self.sample_size ** .5))
        print(f"z value is {z}")
        return z 

    def confidence_interval_func(self, z: float):
        global Z
        interval: dict[str, float] = {}
        if Z != None:
            if self.standard_error != None: 
                distance: float = self.standard_error * Z
    
                interval['min'] = self.sample_average - distance 
                interval['max'] = self.sample_average + distance
            else:
                self.standard_error = self.pop_standard_deviation / self.sample_size ** .5
                distance: float = self.standard_error * z
                
                interval['min'] = self.sample_average - distance 
                interval['max'] = self.sample_average + distance
        else:
            if self.standard_error != None: 
                distance: float = self.standard_error * z
    
                interval['min'] = self.sample_average - distance 
                interval['max'] = self.sample_average + distance
            else:
                self.standard_error = self.pop_standard_deviation / self.sample_size ** .5
                distance: float = self.standard_error * z
                
                interval['min'] = self.sample_average - distance 
                interval['max'] = self.sample_average + distance
        print(f"the confidence interval's min = {interval['min']} and max {interval['max']}")            

    def percent_pop(self) -> float:
        """Take a Z score and gives the percent of the population."""
        percent: float = 0.0
        if self.z_score == None:
            global Z
            percent = norm.cdf(Z)
        else:
            percent = norm.cdf(self.z_score)
        print(f"Percent of population is {percent}")




def main() -> None:
    a_sample: Sample = Sample(5534, None, 23.44, 4.72, None, None)
    # z: float = a_sample.z_value_population()
    # print(f"z value is {z}")
    # a_sample.z_score = a_sample.z_value_sample()
    a_sample.confidence_interval_func(Z)
    a_sample.percent_pop()



if __name__ == '__main__':
    main()