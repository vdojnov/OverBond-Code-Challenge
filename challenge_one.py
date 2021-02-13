from modules.split_gov_and_corp_bonds import split_gov_and_corp_bonds
from modules.sort_bond_list_by_term import sort_bond_list_by_term
from modules.calculate_spread_for_corp_bonds import calculate_spread_for_corp_bonds
from modules.read_file import read_file
from modules.write_to_second_param import write_to_second_param
from modules.calc_spread_to_curve import calc_spread_to_curve


def main():
    # Read from the CSV file passed as the first parameter in CLI
    input_data = read_file()

    # Split gov bond and corp bond objects into two lists
    corp_bonds, gov_bonds = split_gov_and_corp_bonds(input_data)

    # Sort corp and gov bonds lists by bond term
    corp_bonds = sort_bond_list_by_term(corp_bonds)
    gov_bonds = sort_bond_list_by_term(gov_bonds)

    # Create a list with objects for each corp bond id, its counterpart gov bond id, and their spread
    output_list = calculate_spread_for_corp_bonds(corp_bonds,gov_bonds)

    # Format data to requirement to be outputted to file, adding nessecary headers
    field_names = ["bond", "benchmark", "spread_to_benchmark"]
    output_list.insert(0, field_names)

    # Write to the solution the the CSV file passed as second parameter 
    write_to_second_param(output_list, "output_challenge_one.csv")

if __name__ == "__main__":
    main()

