from engine import load_csv, execute_query
from parser import parse_query



while True:

    query = input("SQL> ")

    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    try:

        parsed_query = parse_query(query)
        table_name = parsed_query["table"]

        filename = table_name + ".csv"

        data = load_csv(filename)

        result = execute_query(parsed_query, data)

        if isinstance(result, int):
            print(result)
        else:
            for row in result:
                print(row)

    except Exception as e:
        print("Error:", e)