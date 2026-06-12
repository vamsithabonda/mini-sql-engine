def parse_query(query):

    query = query.strip()
    query = query.replace(";", "")

    parts = query.split()

    if len(parts) < 4:
        raise Exception("Invalid SQL query")

    if parts[0].upper() != "SELECT":
        raise Exception("Query must start with SELECT")

    if parts[2].upper() != "FROM":
        raise Exception("Missing FROM clause")

    parsed = {}

    parsed["select"] = parts[1]
    parsed["table"] = parts[3]

    if "WHERE" in parts:

        where_index = parts.index("WHERE")

        parsed["where"] = {
            "column": parts[where_index + 1],
            "operator": parts[where_index + 2],
            "value": parts[where_index + 3]
        }

    return parsed