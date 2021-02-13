def create_output_arr(corp_bond, gov_bond):
    # This function rearanges and casts data as needed to be outputted to a CSV file 

    _bond = 0
    _type = 1
    _term = 2
    _yeild = 3
    
    bond = corp_bond[_bond]
    benchmark = gov_bond[_bond]
    spread_to_benchmark = str(round(float(corp_bond[_yeild] - gov_bond[_yeild]),2)) + "%"
    arr = [bond,benchmark,spread_to_benchmark]
    return arr