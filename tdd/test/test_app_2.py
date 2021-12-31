import unittest
from app import ProcessTxns

class TestMyApp(unittest.TestCase):

	def test_returns_empty_json_when_only_txn_in_txn_list(self):    
		json_list = [{
  				'id': 123,
  				'sourceAccount': 'my_account',
  				'targetAccount': 'coffee_shop',
  				'amount': -30,
  				'category': 'eating_out',
  				'time': '2018-03-12T12:34:00Z'
                                }]
		app = ProcessTxns(json_list)
		resulttxns = app.get_list_of_dupe_txns()
		self.assertListEqual(resulttxns, [])


	def test_returns_expected_dupe_txns_when_2_dupe_txns_are_in_the_input_txns_list(self): 
		json_list = [{
                                'id': 123,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -30,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:34:00Z'
                                },
                                {
                                'id': 133,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -30,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:35:00Z'
                                }]
		app = ProcessTxns(json_list)
		resulttxns = app.get_list_of_dupe_txns()
		self.assertListEqual(resulttxns, json_list)

	def test_returns_expected_dupe_txns_when_multiple_dupe_and_unique_txns_are_in_the_input_txns_list(self):
		json_list = [{
                                'id': 123,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -30,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:35:00Z'
                                },
                                {
                                'id': 133,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -30,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:34:00Z'},
				{'id': 134,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -130,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:35:00Z'},
				{'id': 121,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -10,
                                'category': 'eating_out',
                                'time': '2018-03-12T13:34:00Z'
                                },
                                {
                                'id': 122,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -10,
                                'category': 'eating_out',
                                'time': '2018-03-12T13:35:00Z'
                                }]
		app = ProcessTxns(json_list)
		resulttxns = app.get_list_of_dupe_txns()
		expected_output_list = [{'id': 133,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -30,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:34:00Z'
                                },
                                {
                                'id': 123,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -30,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:35:00Z'},
                                {'id': 121,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -10,
                                'category': 'eating_out',
                                'time': '2018-03-12T13:34:00Z'
                                },
                                {
                                'id': 122,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -10,
                                'category': 'eating_out',
                                'time': '2018-03-12T13:35:00Z'}]
		self.assertListEqual(resulttxns, expected_output_list)
