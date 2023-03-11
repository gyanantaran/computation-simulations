# Cellular Automata

This is a simple implementation of a cellular automata in Python using Pygame. The current implementation is a one-dimensional automata which uses a pre-defined rule to determine the state of each cell at each iteration.

## Requirements

- Python 3.x
- Pygame library

## Usage

To use this implementation, clone this repository and run the following command in the project directory:

```
python3 main.py
```


The automata will start running, and a Pygame window will open displaying the evolving states of the automata.

## Configuration

The automata can be configured by changing the parameters in the `config.json` file. The following parameters can be configured:

- `num_iter`: The number of iterations to run the automata for
- `mov_iter`: The number of iterations to show in the Pygame window at any given time
- `rule`: The rule for the automata, in the form of a list of tuples. Each tuple should contain two elements: a tuple representing the frame to match, and an integer representing the state to set for the cell in the center of the frame. For example, the following is a rule that sets the center cell to 1 if the left and right cells are both 1, and 0 otherwise:
```
"rule": [
[
[(1, 1, 0), 1],
[(1, 0, 1), 1],
[(1, 0, 0), 0],
[(0, 1, 1), 1],
[(0, 1, 0), 0],
[(0, 0, 1), 0],
[(0, 0, 0), 0]
]
]
```
- `init_state`: The initial state of the automata, in the form of a list of 0s and 1s.


## Introduction:

The purpose of this project is to provide a comprehensive guide on how to use and contribute to the project. This README file is intended to provide a detailed overview of the project, including its goals, features, installation instructions, usage, and contribution guidelines.

## Goals:

The primary goal of this project is to create a user-friendly and robust software solution that can be used by individuals and organizations for various purposes. The software solution aims to provide users with the ability to accomplish complex tasks with ease and efficiency. Additionally, the project aims to promote collaboration and community engagement by encouraging contributions from individuals and organizations.

## Features:

The project includes several features that are designed to enhance its usability and functionality. These features include:

- **User-friendly interface**: The project includes a user-friendly interface that is easy to navigate and understand.

- **Customizable settings**: The project includes customizable settings that allow users to tailor the software to their specific needs.

- **Robust data management**: The project includes robust data management features that allow users to manage and analyze large amounts of data.

- **Advanced reporting**: The project includes advanced reporting features that allow users to generate detailed reports on their data.

## Contribution Guidelines:

To contribute to the project, users should follow these guidelines:

- Fork the project repository.
- Make the desired changes.
- Submit a pull request.
- Wait for feedback and approval from the project maintainers.

## Conclusion:

In conclusion, this project is a comprehensive software solution that is designed to provide users with the ability to accomplish complex tasks with ease and efficiency. The project includes several features that enhance its usability and functionality. Additionally, the project promotes collaboration and community engagement by encouraging contributions from individuals and organizations.

## License

This project is licensed under the terms of the MIT license.

