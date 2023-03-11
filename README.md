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

The automata can be configured by changing the parameters in the `src/constants.py` file. The following parameters can be configured:

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

The purpose of this project is to provide a comprehensive tool to experiment with cellular and mobile automata.

## Examples images and videos

![main-2-rule-2409](https://user-images.githubusercontent.com/95016059/224503561-bd821660-4b69-4b32-8c89-072dae1143e3.jpg)

![main-1-rule-90](https://user-images.githubusercontent.com/95016059/224503557-4e00dec4-dc40-411a-ba3d-3dddde352571.jpg)

https://user-images.githubusercontent.com/95016059/224503537-8b4bc288-1ca1-4ed6-ad17-b034696eba6c.mov

https://user-images.githubusercontent.com/95016059/224503543-693709ce-f2c1-4ef1-9ae3-fde112752639.mov

https://user-images.githubusercontent.com/95016059/224503546-58214c20-5693-481d-a5d4-7faa013e6d6d.mov

https://user-images.githubusercontent.com/95016059/224503548-b7c5b6bf-83ad-4ea4-8d8e-0912c13fe8c3.mov


## Goals:

One-dimensional cellular automata are a class of mathematical models that simulate the behavior of a line of cells, where each cell can have one of a finite number of states. At each time step, the state of each cell is updated based on the state of its neighbors according to a set of rules. These rules are often specified using a lookup table, which maps the current state of a cell and its neighbors to a new state. One-dimensional cellular automata have applications in a variety of fields, including physics, computer science, and biology. The goal of this project is to provide an implementation of a one-dimensional cellular automaton in Python that allows users to explore different rules and initial conditions, and to visualize the evolution of the system over time.

## Features:

The project includes several features that are designed to enhance its usability and functionality. These features include:

- **User-friendly interface**: The project includes a user-friendly interface that is easy to navigate and understand.

- **Customizable settings**: The project includes customizable settings that allow users to tailor the tool to their specific needs.


## Contribution Guidelines:

To contribute to the project, users should follow these guidelines:

- Fork the project repository.
- Make the desired changes.
- Submit a pull request.
- Wait for feedback and approval from the project maintainers.

## Conclusion:

In conclusion, this project was inspired by the groundbreaking work of Stephen Wolfram in "A New Kind of Science". It aimed to explore the fundamental principles of cellular automata and its potential applications in various fields, including computer science, physics, biology, and social sciences. Through the implementation of various algorithms and simulations, this project provided valuable insights into the behavior of cellular automata and their potential implications for real-world phenomena. While there is still much to be explored in this field, the findings of this project serve as a strong foundation for future research and experimentation. Overall, this project represents a significant step forward in our understanding of cellular automata and their potential applications in a wide range of fields.

## License

This project is licensed under the terms of the MIT license.

