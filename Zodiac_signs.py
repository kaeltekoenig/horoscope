def get_day_number_by_date(date):
	'''формат ввода xx.xx.xxxx'''
	day = int(date[:2])
	months = int(date[3:5])
	for month in range(1, months):
		day += day_in_month[month]

	return day

day_in_month = {1:31,
				2:28,
				3:31,
				4:30,
				5:31,
				6:30,
				7:31,
				8:31,
				9:30,
				10:31,
				11:30,
				12:31}