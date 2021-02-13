def calc_spread_to_curve(corp_bonds,gov_bonds):
    cursor = 0
    output_arr = []

    _bond = 0
    _type = 1
    _term = 2
    _yeild = 3
    for corp_bond in corp_bonds:
        # for each corp bond loop through the government bonds to see if term corp bond term is between two gov bond terms
        # Keep a curor of our position as both bond lists are sorted, we can minimize looping
        while gov_bonds[cursor][_term] < corp_bond[_term] and gov_bonds[cursor + 1][_term] < corp_bond[_term]:
            cursor +=1

        # y=mx+b
        # find the slope between the two government bonds
        y2 = gov_bonds[cursor + 1][_yeild]
        y1 = gov_bonds[cursor][_yeild]
        x2 = gov_bonds[cursor + 1][_term]
        x1 = gov_bonds[cursor][_term]

        # Get all slope and intercept which will be used to calculate a trendline for the two gov bond points
        # This equation will help us find the spread to curve 
        slope = ( y2 - y1 )/( x2 - x1)
        intersept = y1 - (slope * x1)

        calculated_yeild = (slope * corp_bond[_term]) + intersept
        corp_bond_yeild = corp_bond[_yeild]
        spread_to_curve = corp_bond_yeild - calculated_yeild

        # Clean up formating and append to the ouput array
        spread_to_curve_string = str(round(spread_to_curve,2)) + "%"
        temp_arr = [corp_bond[_bond], spread_to_curve_string]
        output_arr.append(temp_arr)

    return output_arr
