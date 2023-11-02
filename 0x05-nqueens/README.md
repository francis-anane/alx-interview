# N Queens Challenge

This Python script solves the N Queens problem, which involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. The script takes an argument `N` to determine the size of the chessboard.

## Usage
Ensure you have Python 3 installed. To run the script, use the following command:
where `N` is an integer representing the size of the chessboard.

## Requirements
- Python 3

## Script Description
The script implements a backtracking algorithm to find all possible solutions for the N Queens problem. It starts by placing queens on the chessboard one by one and checks if the placement is safe. If a queen can be placed safely, it moves to the next row. If it cannot find a safe spot, it backtracks to the previous row and tries a different position.

## Sample Output
The script prints all the solutions in the form of a list of coordinates where the queens are placed.

## File Structure
- `nqueens.py`: The main Python script.
- `README.md`: This file, containing information about the script.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

