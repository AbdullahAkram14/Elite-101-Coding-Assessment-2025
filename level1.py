# Level 1: Find Free Tables
# Pseudocode:
# 1. Create an empty list to store free tables.
# 2. Loop through each table and check if it is occupied.
# 3. If a table is free, add it to the list of free tables.
# 4. Return the list of free tables.
def get_free_tables(tables):

    free_tables = []  # List to hold the free tables' IDs

    for table in tables:  # Loop through all tables in the list
        if table.get("occupied") == False:  # Using .get() to check for occupation status
            free_tables.append(table["table_id"])  # Add table ID to list if it's free

    return free_tables  # Return the free table IDs

# Output
def display_free_tables(free_tables, tables):
    for table_id in free_tables:
        table = next(t for t in tables if t["table_id"] == table_id)
        print(f"Table {table['table_id']} is free and can seat {table['capacity']} people.")

