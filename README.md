# Population Simulation

This project simulates population growth over a specified period, taking into account various factors such as birth rates, death rates, child mortality, and random disasters. It visualizes the population changes over time using a line graph.

## Features

-   **Population Growth:** Simulates population growth based on birth, death, and child mortality rates.
-   **Disasters:** Incorporates random medium and large disasters that affect the population.
-   **Visualization:** Plots the population over time using `matplotlib`.

## Requirements

-   Python 3.x
-   `matplotlib` library

## Installation

1.  Clone the repository.
2.  Install the required dependencies:

    ```bash
    pip install matplotlib
    ```

## Usage

Run the script using Python:

```bash
python main.py
```

The script will simulate the population growth and display a graph of the population over the years.

## Configuration

You can adjust the simulation parameters by modifying the constants at the top of `main.py`:

-   `PRINCIPAL_POPULATION`: Starting population.
-   `STARTING_YEAR`: Start year of the simulation.
-   `ENDING_YEAR`: End year of the simulation.
-   `AVERAGE_DEATH_RATE`: Range for death rate (deaths/1000 people).
-   `AVERAGE_BIRTH_RATE`: Range for birth rate (births/1000 people).
-   `CHILD_MORTALITY_RATE`: Range for child mortality rate (deaths/1000 live births).
-   `MEDIUM_DISASTER_RATE`: Frequency range for medium disasters.
-   `MEDIUM_DISASTER_DEATH_RATE`: Death rate range for medium disasters.
-   `LARGE_DISASTER_RATE`: Frequency range for large disasters.
-   `LARGE_DISASTER_DEATH_RATE`: Death rate range for large disasters.
-   `DISASTER_SPACING`: Minimum year gap between medium and large disasters.
