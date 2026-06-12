import csv

# Load CSV data into memory
def load_csv(filename):
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data

def select_columns(data, columns):

    result = []

    for row in data:

        new_row = {}

        for col in columns:
            if col not in row:
                raise Exception(f"Column '{col}' not found")
            new_row[col] = row[col]

        result.append(new_row)

    return result

def filter_rows(data, column, operator, value):

    result = []

    for row in data:

        row_value = int(row[column])
        compare_value = int(value)

        if operator == ">":
            if row_value > compare_value:
                result.append(row)

        elif operator == "<":
            if row_value < compare_value:
                result.append(row)

        elif operator == ">=":
            if row_value >= compare_value:
                result.append(row)

        elif operator == "<=":
            if row_value <= compare_value:
                result.append(row)

        elif operator == "=":
            if row_value == compare_value:
                result.append(row)

        elif operator == "!=":
            if row_value != compare_value:
                result.append(row)

    return result

def count_rows(data):
    return len(data)

# Execute SQL query
def execute_query(parsed_query, data):

    if "where" in parsed_query:

        condition = parsed_query["where"]

        data = filter_rows(
            data,
            condition["column"],
            condition["operator"],
            condition["value"]
        )

    if parsed_query["select"] == "COUNT(*)":
        return count_rows(data)

    if parsed_query["select"] == "*":
        return data

    columns = parsed_query["select"].split(",")

    return select_columns(data, columns)