from operator import itemgetter

def sort_bond_list_by_term(bond_list):
    # Sort the list of lists by the term ascending
    return sorted(bond_list, key=itemgetter(2))