from .cast_bond_data import cast_bond_data
from .is_valid_bond import is_valid_bond

def split_gov_and_corp_bonds(input_arr):
    # Split Government and Corporate bonds into their own arrays after filetering
    output_corp_bonds = [cast_bond_data(bond) for bond in input_arr if is_valid_bond(bond, "corporate")]
    output_gov_bonds = [cast_bond_data(bond) for bond in input_arr if is_valid_bond(bond, "government")]

    return output_corp_bonds, output_gov_bonds
