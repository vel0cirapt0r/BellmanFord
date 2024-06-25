# Bellman-Ford Algorithm Implementation

This Python project implements the Bellman-Ford algorithm for finding shortest paths in graphs. It allows users to either generate a new graph with specified nodes and edges or use prepared graphs from a dataset or any other source.

## Project Structure

```
.
├── LICENSE
├── README.md
├── decorators.py
├── graph_parser.py
├── main.py
├── requirements.txt
├── sample_filepaths.py
└── sample_graph_generator.py
```

### Files:

- **`decorators.py`**: Contains decorators for measuring execution time and handling errors.
- **`graph_parser.py`**: Parses graph data from files.
- **`main.py`**: Main script where users can choose to generate a new graph or use a prepared graph to apply the Bellman-Ford algorithm.
- **`requirements.txt`**: Contains the required Python packages. (Note: This file is empty as all packages used are standard built-in.)
- **`sample_filepaths.py`**: Template file for setting dataset paths.
- **`sample_graph_generator.py`**: Generates random graphs for testing purposes.

## Getting Started

### Prerequisites

Ensure Python 3.x is installed on your machine.

### Setting Up Your Dataset

1. **Rename the File**:
   - Rename `sample_filepaths.py` to `filepaths.py`.

2. **Set the Dataset Path**:
   - Open `filepaths.py` and set the `DATASET_PATH` variable to the location of your graph files.

## Usage

1. **Running the Program**:
   - Open a terminal or command prompt.
   - Navigate to the project directory.

2. **Execute `main.py`**:
   - Run the following command:

     ```bash
     python main.py
     ```

3. **Choose Your Option**:
   - You will be prompted to choose:
     ```
     Choose an option:
     1. Generate a new graph
     2. Use a prepared graph
     Option:
     ```

4. **Generating a New Graph (`1`)**:
   - Enter the number of nodes and edges for the new graph when prompted.

5. **Using a Prepared Graph (`2`)**:
   - Enter the path to the folder containing the graph files and the name of the graph files.

6. **Running the Bellman-Ford Algorithm**:
   - After choosing or generating a graph, enter the source vertex from which to compute shortest paths.

7. **Example Output**:
   - Upon completion, the program will display the computed distances from the source vertex to all other vertices.

### How It Works

- **`decorators.py`**: Provides decorators for measuring execution time and handling errors.
- **`graph_parser.py`**: Parses graph data from specified files.
- **`main.py`**: Offers an interactive interface for users to select graph generation or usage, applying the Bellman-Ford algorithm accordingly.
- **`sample_graph_generator.py`**: Generates random graphs for testing purposes.

## Graph Data Sources

This project allows for testing with generated graphs, datasets from the project, or any other graph dataset of choice.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to explore and utilize this Bellman-Ford algorithm implementation for analyzing various graph datasets or testing different scenarios. Whether for educational purposes or practical applications, we hope you find this project valuable and adaptable to your needs. Happy pathfinding with Bellman-Ford!