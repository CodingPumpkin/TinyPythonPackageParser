class Data:
	def __init__(self, packege_type):
		self.data = {}
		self.data["packege_type"] = packege_type
		self.init_data()

	def init_data(self):
		if (self.data["packege_type"] == "SD"):
			self.data["date"] = '01012000'		#DDMMYYYY
			self.data["time"] = '000000'		#HHMMSS
			self.data["lat1"] = 0.0		#float value
			self.data["lat2"] = ''		#char
			self.data["lon1"] = 0.0		#float value
			self.data["lon2"] = ''		#char
			self.data["speed"] = 0		#int km/h
			self.data["course"] = ''	#int [0,359]
			self.data["height"] = 0		#int, m
			self.data["sats"] = 0		#int, number of satellites
		elif (self.data["packege_type"] == "M"):
			self.data["message"] = ''
		else:
			self.data["Error:"] = "Unknown data type"

	def parse_data(self, data_string):
		if (self.data["packege_type"] == "SD"):
			raw_data = data_string.split(';')
			if (not self.is_sd_data_wrong_size(raw_data)):
				self.data["date"] = self.get_date_from_value(raw_data[0])
				self.data["time"] = self.get_time_from_value(raw_data[1])
				self.data["lat1"] = self.get_float_from_value(raw_data[2])
				self.data["lat2"] = raw_data[3]
				self.data["lon1"] = self.get_float_from_value(raw_data[4])
				self.data["lon2"] = raw_data[5]
				self.data["speed"] = self.get_float_from_value(raw_data[6])
				self.data["course"] = self.check_angle(raw_data[7])
				self.data["height"] = self.get_float_from_value(raw_data[8])
				self.data["sats"] = self.get_float_from_value(raw_data[9])
			else:
				print("Not enough items in the input. Setting default values\n")
				self.init_data()
		elif (self.data["packege_type"] == "M"):
			self.data["message"] = data_string

	def is_sd_data_wrong_size(self, raw_data):
		if (len(raw_data)!=10):
			return "SD data privuded is invalid: too few or too many arguments given"
		else:
			return 0
	
	def get_float_from_value(self, value):
		try:
			return float(value);
		except:
			print(f"Error: Couldn't interpret value {value} as a float.")
			return 0.0

	def get_int_from_value(self, value):
		try:
			return int(value);
		except:
			print(f"Error: Couldn't interpret value {value} as a whole number.\n")
			return 0
	
	def check_angle(self, value):
		a = self.get_int_from_value(value)
		if(a>359):
			print(f"Warning! Angle {a} is more that 360 degrees. Converting. . .\n")
			a = a % 360
		elif(a<0):
			print(f"Warning! Angle {a} is less than 0 degrees. Converting. . .\n")
			a = 360 + a
		return a

	def get_date_from_value(self, value):
		if (len(value)!=8):
			print(f"Error: invalid date format {value}. Setting default date\n")
			return "01012000"
		dd = self.get_int_from_value(value[0:2])
		mm = self.get_int_from_value(value[2:4])
		yyyy = self.get_int_from_value(value[4:])
		if(mm<0 or mm>12):
			print(f"Error: invalid month {mm}. Setting default date\n")
			return "01012000"
		else:
			if(dd<0):
				print(f"Error: invalid day {dd}. Setting default date\n")
				return "01012000"
			elif (dd > self.check_max_day(yyyy, mm)):
				print(f"Error: invalid day {dd} for month {mm} year {yyyy}. Setting default date\n")
				return "01012000"
			else:
				return value

	def check_max_day(self, yyyy, mm):
		max_day = 0
		if (mm == 2):
			if ( yyyy % 4 == 0 and yyyy % 100 != 0 ) or ( yyyy % 400 == 0 ):
				max_day = 29
			else:
				max_day = 28
		elif (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm ==12):
			max_day = 31
		else:
			max_day = 30
		return max_day

	def get_time_from_value(self, value):
		if(len(value)!=6):
			print(f"Error: invalid time format {value}. Setting default time\n")
			return "000000"
		hh = self.get_int_from_value(value[0:2])
		mm = self.get_int_from_value(value[2:4])
		ss = self.get_int_from_value(value[4:])
		if (hh<0 or hh>240):
			print(f"Error: invalid hour {hh}. Setting default time\n")
			return "000000"
		elif (mm<0 or mm>59):
			print(f"Error: invalid minute {mm}. Setting default time\n")
			return "000000"
		elif (ss<0 or ss>59):
			print(f"Error: invalid second {ss}. Setting default time\n")
			return "000000"
		else:
			return value

	def __str__(self):
		result = f"Packege type: {self.data['packege_type']}\nData:\n"
		for key in self.data:
			result += f"\t{key}: {self.data[key]}\n"
		return result


def parse():
	#init variables:
	ending = "\r\n"
	separator = '#'
	#read raw input and splt it by separator character:
	input_data = (input().strip(ending)).split(separator)
	#create an object to parse all the data and store it:
	data = Data(input_data[1])
	data.parse_data(input_data[2])
	#print resulting data structure:
	print(data)

if __name__ == "__main__":
	parse()

