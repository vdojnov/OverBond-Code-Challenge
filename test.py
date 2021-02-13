import unittest
import sys

from modules.split_gov_and_corp_bonds import split_gov_and_corp_bonds
from modules.sort_bond_list_by_term import sort_bond_list_by_term
from modules.calculate_spread_for_corp_bonds import calculate_spread_for_corp_bonds
from modules.read_file import read_file
from modules.write_to_second_param import write_to_second_param
from modules.calc_spread_to_curve import calc_spread_to_curve
from modules.is_valid_bond import is_valid_bond
from modules.create_output_arr import create_output_arr


class TestStringMethods(unittest.TestCase):

    def test_invalid_bond(self):
        # Test filtering out by bond type, corporate vs. government
        bond = ["C1", "government", "11.7 years", "5.7%"]
        result = is_valid_bond(bond, "corporate")
        self.assertFalse(result)

    def test_valid_bond(self):
        bond = ["C1", "government", "11.7 years", 110000]
        result = is_valid_bond(bond, "government")
        self.assertTrue(result)
    
    def test_split_gov_and_corp_bonds(self):
        input_list = [
            ['bond', 'type', 'term', 'yield'],
            ["C1", "corporate", "10.3 years", "5.30%"],
            ["C2", "corporate", "15.2 years", "8.30%"],
            ["G1", "government", "9.4 years", "3.70%"],
            ["G2", "government", "12 years", "4.80%"],
            ["G3", "government", "16.3 years", "5.50%"]
        ]
        _bond = 0
        _type = 1
        _term = 2
        _yeild = 3

        corp_bonds, gov_bonds = split_gov_and_corp_bonds(input_list)
        self.assertEqual(len(corp_bonds), 2)
        self.assertEqual(corp_bonds[0][_bond], 'C1')
        self.assertEqual(corp_bonds[1][_bond], 'C2')

        self.assertEqual(len(gov_bonds), 3)
        self.assertEqual(gov_bonds[0][_bond], 'G1')
        self.assertEqual(gov_bonds[1][_bond], 'G2')
        self.assertEqual(gov_bonds[2][_bond], 'G3')


    def test_sort_bond_list_by_term(self):
        _bond = 0
        _type = 1
        _term = 2
        _yeild = 3
        
        gov_bond_list = [
            ["G1", "government", 9.4, 3.70],
            ["G2", "government", 12, 4.80],
            ["G3", "government", 16.3, 5.50]
        ]
        
        sorted_list = sort_bond_list_by_term(gov_bond_list)

        self.assertEqual(len(sorted_list), 3)
        self.assertEqual(sorted_list[0][_bond], 'G1')
        self.assertEqual(sorted_list[1][_bond], 'G2')

            
    def test_create_output_obj(self):
        corp_bond = ["C1", "corporate", 10.3, 5.30]        
        gov_bond =  ["G1", "government", 9.4, 3.70]

        arr = create_output_arr(corp_bond,gov_bond)
        self.assertEqual(arr[0], 'C1')
        self.assertEqual(arr[1], 'G1')
        self.assertEqual(arr[2], '1.6%')

        

    def test_calculate_spread_for_corp_bonds(self):
        
        corp_bonds = [["C1", "corporate", 10.3, 5.30]]
        gov_bonds= gov_bond_list = [
            ["G1", "government", 9.4, 3.70],
            ["G2", "government", 12, 4.80],
        ]
        
        output_list = calculate_spread_for_corp_bonds(corp_bonds, gov_bonds)

        expected = ["C1", "G1", "1.6%"]

        self.assertEqual(len(output_list), 1)
        self.assertEqual(output_list[0], expected)

    def test_calc_spread_to_curve(self):
        _bond = 0
        _spread_to_curve = 1
        
        corp_bond_list = [
            ["C1", "corporate", 10.3, 5.30],
            ["C2", "corporate", 15.2, 8.30]
        ]
        
        gov_bond_list = [
            ["G1", "government", 9.4, 3.70],
            ["G2", "government", 12, 4.80],
            ["G3", "government", 16.3, 5.50]
        ]

        output_arr = calc_spread_to_curve(corp_bond_list,gov_bond_list)
        self.assertEqual(len(output_arr), 2)
        self.assertEqual(output_arr[0][_bond], "C1")
        self.assertEqual(output_arr[0][_spread_to_curve], "1.22%")
        self.assertEqual(output_arr[1][_bond], "C2")
        self.assertEqual(output_arr[1][_spread_to_curve], "2.98%")





if __name__ == '__main__':
    unittest.main()

