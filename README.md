# Mini SQL Engine

## Overview

The Mini SQL Engine is a simplified SQL query processor implemented in Python. The project demonstrates how SQL queries are parsed and executed internally without using a database management system.

The engine loads data from CSV files into memory and allows users to execute SQL-like queries through an interactive command-line interface (CLI).

## Features

* Load CSV files into memory as Python dictionaries
* Support multiple datasets (tables)
* Parse SQL queries containing SELECT, FROM, and WHERE clauses
* Select all columns using SELECT *
* Select specific columns
* Filter data using WHERE conditions
- Support comparison operators:
  - `=`
  - `!=`
  - `>`
  - `<`
  - `>=`
  - `<=`
* Support COUNT(*) aggregation
* Interactive SQL command-line interface
* Error handling for invalid queries and missing columns

## Setup Instructions

### Requirements

* Python 3.10 or higher
* Visual Studio Code (optional)

### Project Structure

sql_engine_project/

├── main.py

├── parser.py

├── engine.py

├── employees.csv

├── students.csv

└── README.md

### Run the Project

Open a terminal in the project folder and run:

python main.py

To exit:

exit

or

quit

## Supported SQL Queries

### Select All Columns

SELECT * FROM employees

### Select Specific Columns

SELECT name,age FROM employees

SELECT name,marks FROM students

### WHERE Clause

SELECT * FROM employees WHERE age > 30

SELECT * FROM employees WHERE age <= 28

SELECT * FROM students WHERE marks >= 80

### COUNT

SELECT COUNT(*) FROM employees

SELECT COUNT(*) FROM students

### Multiple Tables

SELECT * FROM employees

SELECT * FROM students

## Example Outputs

### Query

SELECT * FROM employees

### Output

{'id': '1', 'name': 'John', 'age': '25', 'country': 'USA'}

{'id': '2', 'name': 'Alice', 'age': '35', 'country': 'Canada'}

### Query

SELECT COUNT(*) FROM employees

### Output

5

## Internal Working

1. User enters a SQL query.
2. The parser extracts SELECT, FROM, and WHERE information.
3. The corresponding CSV file is loaded.
4. WHERE conditions are applied.
5. SELECT or COUNT operations are executed.
6. Results are displayed in the terminal.

## Limitations

* Supports only one WHERE condition
* Supports only COUNT(*) aggregation
* Does not support JOIN operations
* Does not support GROUP BY
* Does not support ORDER BY
* Does not support INSERT, UPDATE, or DELETE

## Future Improvements

* Support AND / OR conditions
* Support GROUP BY
* Support ORDER BY
* Support JOIN operations
* Add aggregate functions such as:

  * SUM
  * AVG
  * MIN
  * MAX

## Technologies Used

* Python
* CSV Module
* Lists
* Dictionaries
* Command Line Interface (CLI)

## Educational Purpose

This project was developed to understand how SQL engines work internally, including query parsing, filtering, projection, and aggregation.
