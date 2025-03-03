# Level 4: Check for Adjacent Tables
# Pseudocode:
# 1. Create an empty list to store combinations of tables.
# 2. Loop through each timeslot (rows 1 to 6) and each table in that timeslot.
# 3. Check if the current table can fit the party size.
# 4. If not, check the next adjacent table.
# 5. If both tables are free and their combined capacity is enough, add them to the list.
# 6. Return the list of single tables and adjacent table combinations.

def find_tables_including_combos(restaurant_tables, party_size):
    available_combos = []

    # Step 1: Loop through each timeslot (rows 1 to 6)
    for row in range(1, len(restaurant_tables)):
        # Step 2: Loop through each table in the timeslot (columns 1 to 6)
        for i in range(1, len(restaurant_tables[row])):
            table_status = restaurant_tables[row][i]  # 'o' or 'x' (free or occupied)
            table_label = restaurant_tables[0][i]     # Table label (e.g., 'T1(2)', 'T2(4)')
            table_capacity = int(table_label.split("(")[1].split(")")[0])  # Extract capacity

            # Step 3: Check if the table is free and can fit the party size
            if table_status == 'o' and table_capacity >= party_size:
                available_combos.append((i,))  # Single table combination (by index)
            
            # Step 4: I would now need to check for adjacent tables, but couldn't finish.
            # This is where the combination of adjacent tables should be handled.
            # If the next table is free, I would check if their combined capacity meets the party size.

    # Step 5: Return the available combinations once the code is completed
    return available_combos


