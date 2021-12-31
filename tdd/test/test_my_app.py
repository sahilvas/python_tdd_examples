import unittest
from app import ProcessTxns

class TestMyApp(unittest.TestCase):

	def test_amount_returns_zero_given_empty_txn_list_json(self):
		json_list = {}
		category = 'ABC'
		start_time = '2018-03-12T12:34:00Z'
		end_time = '2018-03-12T12:36:00Z'
		app = ProcessTxns(json_list)
		amount = app.getAmountByCategoryInPeriod(category, start_time, end_time)
		self.assertEqual(amount, 0)

	def test_amount_returns_right_result_with_valid_arguments(self):
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
                                'amount': 10,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:35:00Z'
                                }]
		category = 'eating_out'
		start_time = '2018-03-12T12:34:00Z'
		end_time = '2018-03-12T12:36:00Z'
		app = ProcessTxns(json_list)
		amount = app.getAmountByCategoryInPeriod(category, start_time, end_time)
		self.assertEqual(amount, -20)


	def test_amount_returns_right_result_with_diff_time_ranges_in_input_txns_list(self):
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
                                'amount': 10,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:37:00Z'
                                }]
		category = 'eating_out'
		start_time = '2018-03-12T12:34:00Z'
		end_time = '2018-03-12T12:36:00Z'
		app = ProcessTxns(json_list)
		amount = app.getAmountByCategoryInPeriod(category, start_time, end_time)
		self.assertEqual(amount, -30)


	def test_amount_returns_right_result_with_diff_time_ranges_and_diff_categories_in_input_txns_list(self):
		json_list = [{
                                'id': 123,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': -30,
                                'category': 'eating_out1',
                                'time': '2018-03-12T12:34:00Z'
                                },
                                {
                                'id': 133,
                                'sourceAccount': 'my_account',
                                'targetAccount': 'coffee_shop',
                                'amount': 10,
                                'category': 'eating_out',
                                'time': '2018-03-12T12:37:00Z'
                                }]
		category = 'eating_out'
		start_time = '2018-03-12T12:34:00Z'
		end_time = '2018-03-12T12:38:00Z'
		app = ProcessTxns(json_list)
		amount = app.getAmountByCategoryInPeriod(category, start_time, end_time)
		self.assertEqual(amount, 10)
