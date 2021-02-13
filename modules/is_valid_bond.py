def is_valid_bond(bond_arr, bond_type):
    # Checks if the bond type in the bond_obj matches the desired bond time, 
    # and makes sure there are no missing values
    _bond = 0
    _type = 1
    _term = 2
    _yeild = 3
    if bond_arr[_type] == bond_type:         
        if bond_arr[_bond] is not None and bond_arr[_term] is not None and bond_arr[_yeild] is not None:
            return True
    return False