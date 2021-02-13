def cast_bond_data(bond_arr):
    # Clean up data by turning strings to numbers for ease of calculation later
    _bond = 0
    _type = 1
    _term = 2
    _yeild = 3
    bond_arr[_term] = float(bond_arr[_term].split(" ")[0])
    bond_arr[_yeild] = float(bond_arr[_yeild][:-1])
        
    return bond_arr