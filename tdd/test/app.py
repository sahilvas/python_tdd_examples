import datetime

class ProcessTxns:
	def __init__(self, transactionsList):
		self.transactionsList = transactionsList

	def getAmountByCategoryInPeriod(self, category, startTime, endTime):
		amount = 0
		for txns in self.transactionsList:
			if txns['category'] == category and txns['time'] >= startTime and txns['time'] < endTime:
				amount += txns['amount']

		return amount
	def get_list_of_dupe_txns(self):
		dupe_txns_list = []
		for txns_o in self.transactionsList:
			for txns_i in self.transactionsList:
				if txns_o['amount'] == txns_i['amount'] and txns_o['category'] == txns_i['category'] and txns_o['id'] != txns_i['id']:
					dupe_txns_list.append(txns_o)
		return self.get_sorted_list(dupe_txns_list)
	
	@staticmethod
	def get_sorted_list(unsorted_list):
		sorted_list = []
		#print(datetime.datetime.strptime(unsorted_list['time'], '%Y-%m-%dT%H:%M:%SZ')))
		print('1 -', unsorted_list)
		#print(datetime.datetime.strptime(unsorted_list[0]['time'], '%Y-%m-%dT%H:%M:%SZ'))
		while unsorted_list:
			minimum = datetime.datetime.strptime(unsorted_list[0]['time'], '%Y-%m-%dT%H:%M:%SZ')
			y = unsorted_list[0]
			for txns in unsorted_list:
				x = datetime.datetime.strptime(txns['time'], '%Y-%m-%dT%H:%M:%SZ')
				if x < minimum:
					print(x, minimum)
					minimum = x
					y = txns
			sorted_list.append(y)
			unsorted_list.remove(y)
		print('2 -', sorted_list)
		return sorted_list
