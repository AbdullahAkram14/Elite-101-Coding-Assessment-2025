# Level 3: Find Free Tables for a Party Size Across All Timeslots
# Pseudocode:
# 1. Create an empty list to store tables that are free and can fit the party size.
# 2. Loop through each timeslot (rows 1 to 6).
# 3. For each timeslot, check if the table is free and its capacity is enough for the party size.
# 4. Add the table ID to the list if it meets the requirements.
# 5. Return the list of tables that are free and fit the party size.

def get_available_tables_for_party(tables, party_size):
  
    available_tables = []

    # Loop through each table to check if it fits the party size and is free
    for table in tables:
        # Parse the capacity from the table label (e.g., "T2(4)" -> capacity 4)
        capacity = int(table["label"].split("(")[1].split(")")[0])

        # Check if the table's capacity is enough and it's free (indicated by 'o' in layout)
        if capacity >= party_size and table["layout"] == "o":
            available_tables.append(table["table_id"])

    return available_tables

# Output
def display_available_tables_for_party(available_tables, tables):
    for table_id in available_tables:
        table = next(t for t in tables if t["table_id"] == table_id)
        print(f"Table {table['table_id']} is free and can seat {table['capacity']} people.")

