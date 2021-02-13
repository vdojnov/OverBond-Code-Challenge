from .create_output_arr import create_output_arr

def calculate_spread_for_corp_bonds(corp_bonds,gov_bonds):
    cursor = 0
    min_abs_val = float('inf')
    output_list = [] 
    last_gov_bond = False

    _bond = 0
    _type = 1
    _term = 2
    _yeild = 3

    # Go through each corporate bond, and find the corresponding govenrment bond 
    for corp_bond in corp_bonds:
        # loop through gov bonds, but keeping track of cursor so you dont loop from start       
        while abs(gov_bonds[cursor][_term] - corp_bond[_term]) < min_abs_val:
            min_abs_val = min(abs(gov_bonds[cursor][_term] - corp_bond[_term]),min_abs_val)
            if cursor == len(gov_bonds) - 1:
                last_gov_bond = True
                break
            cursor += 1
            
        # To avoid Index out of range error, if the cursor is on the last element in array, 
        # the closest gov bond will always be the last in the sorted list
        if last_gov_bond:
            temp_obj = create_output_arr(corp_bond, gov_bonds[cursor])
            output_list.append(temp_obj)
        else:
            cursor -= 1
            temp_obj = create_output_arr(corp_bond, gov_bonds[cursor])
            output_list.append(temp_obj)
        min_abs_val = float('inf')
    return output_list