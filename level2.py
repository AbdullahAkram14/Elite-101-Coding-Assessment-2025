# Level 2: Find Tables for a Given Party Size
# Pseudocode:
# 1. Create an empty list to store tables that can seat the party.
# 2. Loop through each table and check if it's free and has enough capacity for the party size.
# 3. If a table is free and fits, add it to the list.
# 4. Return the list of tables that meet the requirement.



def assign_table_to_party(tables, party_size):
    
    available_tables = [table for table in tables if not table["occupied"] and table["capacity"] >= party_size]

    if available_tables:
        return available_tables[0]["table_id"]
    else:
        return None
# Output
def display_suitable_tables(suitable_tables, tables):
    for table_id in suitable_tables:
        table = next(t for t in tables if t["table_id"] == table_id)
        print(f"Table {table['table_id']} is free and can seat {table['capacity']} people.")
