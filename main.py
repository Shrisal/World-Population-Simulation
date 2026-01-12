import random
import matplotlib.pyplot as plt

PRINCIPAL_POPULATION = 255000000 # Starting population
STARTING_YEAR = 1 # Starting year of simulation
ENDING_YEAR = 2025 # Ending year of simulation

AVERAGE_DEATH_RATE = (11, 23) # Death rate expressed as (a, b) where a is the minimum death rate and b is the maximum death rate. a and b are both expressed as deaths/1000 people. a and b are both integers.
AVERAGE_BIRTH_RATE = (20, 34) # Live birth rate expressed as (a, b) where a is the minimum birth rate and b is the maximum birth rate. a and b are both expressed as births/1000 people. a and b are both integers.
CHILD_MORTALITY_RATE = (150, 375) # Child mortality rate expressed as (a, b) where a is the minimum mortality rate and b is the maximum mortality rate. a and b are both expressed as deaths/1000 live births. a and b are both integers.

MEDIUM_DISASTER_RATE = (80, 150) # The year range of a medium-sized disaster expressed as (a, b) where a is the minimum disaster rate and b is the maximum disaster rate. a medium-sized disaster will happen any time between a and b. a and b are both integers.
MEDIUM_DISASTER_DEATH_RATE = (50, 100) # The death rate of a medium-sized disaster expressed as (a, b) where a is the minimum death rate and b is the maximum death rate. a and b are both expressed as deaths/1000 people. a and b are both integers.

LARGE_DISASTER_RATE = (200, 400) # The year range of a large-sized disaster expressed as (a, b) where a is the minimum disaster rate and b is the maximum disaster rate. a large-sized disaster will happen any time between a and b. a and b are both integers.
LARGE_DISASTER_DEATH_RATE = (150, 300) # The death rate of a large-sized disaster expressed as (a, b) where a is the minimum death rate and b is the maximum death rate. a and b are both expressed as deaths/1000 people. a and b are both integers.

DISASTER_SPACING = 75 # The minimum year gap between a medium and large disaster.

class PopulationEstimation:

    def __init__(self):
        self.population = PRINCIPAL_POPULATION
        self.population_graph = [self.population]

        self.year = STARTING_YEAR
        self.year_graph = [self.year]

        self.reset_variable_parameters(disasters=True)

    def death_rate(self):
        return random.uniform(*AVERAGE_DEATH_RATE) / 1000

    def birth_rate(self):
        return random.uniform(*AVERAGE_BIRTH_RATE) / 1000
    
    def child_mortality_rate(self):
        return random.uniform(*CHILD_MORTALITY_RATE) / 1000

    def medium_disaster_data(self, adapt=False):
        medium_disaster = {"year": self.year + random.randint(*MEDIUM_DISASTER_RATE), "rate": random.uniform(*MEDIUM_DISASTER_DEATH_RATE) / 1000}
        if adapt:
            time = 0
            while abs(medium_disaster["year"] - self.large_disaster["year"]) <= DISASTER_SPACING:
                medium_disaster = {"year": self.year + random.randint(*MEDIUM_DISASTER_RATE), "rate": random.uniform(*MEDIUM_DISASTER_DEATH_RATE) / 1000}
                if time >= 100:
                    medium_disaster = {"year": self.year + max(list(range(*MEDIUM_DISASTER_RATE)) + [MEDIUM_DISASTER_RATE[1]], key=lambda x: abs(x - self.large_disaster["year"])), "rate": random.uniform(*MEDIUM_DISASTER_DEATH_RATE) / 1000}
                    break
                time += 1

        return medium_disaster

    def large_disaster_data(self, adapt=False):
        large_disaster = {"year": self.year + random.randint(*LARGE_DISASTER_RATE), "rate": random.uniform(*LARGE_DISASTER_DEATH_RATE) / 1000}
        if adapt:
            time = 0
            while abs(self.medium_disaster["year"] - large_disaster["year"]) <= DISASTER_SPACING:
                large_disaster = {"year": self.year + random.randint(*LARGE_DISASTER_RATE), "rate": random.uniform(*LARGE_DISASTER_DEATH_RATE) / 1000}
                if time >= 100:
                    large_disaster = {"year": self.year + max(list(range(*LARGE_DISASTER_RATE)) + [LARGE_DISASTER_RATE[1]], key=lambda x: abs(x - self.medium_disaster["year"])), "rate": random.uniform(*LARGE_DISASTER_DEATH_RATE) / 1000}
                    break
                time += 1

        return large_disaster

    def new_disasters(self):
        self.medium_disaster = self.medium_disaster_data()
        self.large_disaster = self.large_disaster_data()

        while abs(self.medium_disaster["year"] - self.large_disaster["year"]) <= DISASTER_SPACING:
            self.medium_disaster = self.medium_disaster_data()

    def reset_variable_parameters(self, disasters=False):
        self.current_death_rate = self.death_rate()
        self.current_birth_rate = self.birth_rate()
        self.current_child_mortality_rate = self.child_mortality_rate()

        if disasters:
            self.medium_disaster = {"year": None, "rate": None}
            self.large_disaster = {"year": None, "rate": None}
            self.new_disasters()

    def next_year(self):
        population_difference = 0
        
        medium_disaster = False
        large_disaster = False
        if self.medium_disaster["year"] == self.year:
            medium_disaster = True
        if self.large_disaster["year"] == self.year:
            large_disaster = True

        # Children birth
        births = int(self.population * self.current_birth_rate)
        population_difference += births
        
        # Children death
        child_morality = int(births * self.current_child_mortality_rate)
        population_difference -= child_morality
        
        # Normal death
        deaths = int(self.population * self.current_death_rate)
        population_difference -= deaths

        # Medium disaster handling
        if medium_disaster:
            medium_disaster_deaths = int(self.population * self.medium_disaster["rate"])
            population_difference -= medium_disaster_deaths

            self.medium_disaster = self.medium_disaster_data(adapt=True)

        # Large disaster handling
        elif large_disaster:
            large_disaster_deaths = int(self.population * self.large_disaster["rate"])
            population_difference -= large_disaster_deaths

            self.large_disaster = self.large_disaster_data(adapt=True)

        # Changing everything
        self.year += 1
        self.population += population_difference

        self.year_graph.append(self.year)
        self.population_graph.append(self.population)

        # Changing parameters for next iteration
        self.reset_variable_parameters()

    def plot(self):
        plt.plot(self.year_graph, self.population_graph, color='orange')
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Simulation")
        plt.grid(True)
        plt.show()

population = PopulationEstimation()
for year in range(STARTING_YEAR, ENDING_YEAR):
    population.next_year()
population.plot()
