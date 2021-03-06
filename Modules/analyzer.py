from numpy import std

class Import(object):
	"""Import program argument
	
	Tries to import provided if it's a file and if it's provided"""
	import argparse
	import subprocess
	
	def __init__(self, infile):
		self.infile = infile

	parser = argparse.ArgumentParser('Select a picture to have color corrected.')
 	parser.add_argument('-i', action='store', dest='input_pic', 
			   type=file, help='use to select your picture')

	try:
		results = parser.parse_args()
		infile = results.input_pic
		infile = str(infile.name)

	except IOError:
		print "You didn't select a file or the path is broken. Please try again."
		quit()
	except AttributeError:
		print "You didn't select a file"
		quit()


class Processor(Import):
	"""Processes the argument through Python Image Libary

	Takes the image and puts its RGB values into a list, the image is 1/10 scale"""
	from PIL import Image
	
	def __init__(self):
		pass


	try:
		image = Image.open(Import.infile, 'r')
		image = image.resize((int(image.size[0]*.1),int(image.size[1]*.1)), Image.ANTIALIAS)
		pix_vals = list(image.getdata())

		pixels = []

	

		for i in pix_vals:
			pixels.append(list(i))
	
	except IOError:
		print "The file you selected isn't a picture. Try again."


class Bands(Import):
	"""Sorts RGB values into bands

	Each color has a 10 part band that the RGB values are sorted into
	"""

	def __init__(self):
		pass
	
	red_1 = []
	red_2 = []
	red_3 = []
	red_4 = []
	red_5 = []
	red_6 = []
	red_7 = []
	red_8 = []
	red_9 = []
	red_10 = []
	
	blue_1 = []
	blue_2 = []
	blue_3 = []
	blue_4 = []
	blue_5 = []
	blue_6 = []
	blue_7 = []
	blue_8 = []
	blue_9 = []
	blue_10 = []
	
	green_1 = []
	green_2 = []
	green_3 = []
	green_4 = []
	green_5 = []
	green_6 = []
	green_7 = []
	green_8 = []
	green_9 = []
	green_10 = []
	

	gray_1 = []
	gray_2 = []
	gray_3 = []
	gray_4 = []
	gray_5 = []
	gray_6 = []
	gray_7 = []
	gray_8 = []
	gray_9 = []
	gray_10 = []

	src_red_1 = []
	src_red_2 = []
	src_red_3 = []
	src_red_4 = []
	src_red_5 = []
	src_red_6 = []
	src_red_7 = []
	src_red_8 = []
	src_red_9 = []
	src_red_10 = []

	src_green_1 = []
	src_green_2 = []
	src_green_3 = []
	src_green_4 = []
	src_green_5 = []
	src_green_6 = []	
	src_green_7 = []
	src_green_8 = []
	src_green_9 = []
	src_green_10 = []

	src_blue_1 = []
	src_blue_2 = []
	src_blue_3 = []
	src_blue_4 = []
	src_blue_5 = []
	src_blue_6 = []
	src_blue_7 = []
	src_blue_8 = []
	src_blue_9 = []
	src_blue_10 = []

	src_gray_1 = []
	src_gray_2 = []
	src_gray_3 = []
	src_gray_4 = []
	src_gray_5 = []
	src_gray_6 = []
	src_gray_7 = []
	src_gray_8 = []
	src_gray_9 = []
	src_gray_10 = []

	wb_reds = []
	wb_greens = []
	wb_blues = []

	def bands(self, px):
		# Sorts the pixels into RGB bands

		self.px = px

		stdev = 4.25
		px_list = px
		num_red = []
		num_green = []
		num_blue = []
		num_gray = []
	
		for v in px_list:
			if std(v) <= stdev:
				num_gray.append(v)
			elif v[0] <= 20 and v[1] <= 20 and v[2] <= 20:
				num_gray.append(v)
			elif max(v) == v[0] and v[0] > 20:
				num_red.append(v)
			elif max(v) == v[1] and v[1] > 20:
				num_green.append(v)
			elif max(v) == v[2] and v[2] > 20:
				num_blue.append(v)
			else:
				continue

		for v in num_red:
			if 0 <= v[0] < 25:
				Bands.red_1.append(v)
			elif 25 <= v[0] < 50:
				Bands.red_2.append(v)
			elif 50 <= v[0] < 75:
				Bands.red_3.append(v)
			elif 75 <= v[0] < 100:
				Bands.red_4.append(v)
			elif 100 <= v[0] < 125:
				Bands.red_5.append(v)
			elif 125 <= v[0] < 150:
				Bands.red_6.append(v)
			elif 150 <= v[0] < 175:
				Bands.red_7.append(v)
			elif 175 <= v[0] < 200:
				Bands.red_8.append(v)
			elif 200 <= v[0] < 250:
				Bands.red_9.append(v)
			elif 250 <= v[0] < 256:
				Bands.red_10.append(v)
			else:
				continue
	
		for v in num_blue:
			if 0 <= v[2] < 25:
				Bands.blue_1.append(v)
			elif 25 <= v[2] < 50:
				Bands.blue_2.append(v)
			elif 50 <= v[2] < 75:
				Bands.blue_3.append(v)
			elif 75 <= v[2] < 100:
				Bands.blue_4.append(v)
			elif 100 <= v[2] < 125:
				Bands.blue_5.append(v)
			elif 125 <= v[2] < 150:
				Bands.blue_6.append(v)
			elif 150 <= v[2] < 175:
				Bands.blue_7.append(v)
			elif 175 <= v[2] < 200:
				Bands.blue_8.append(v)
			elif 200 <= v[2] < 250:
				Bands.blue_9.append(v)
			elif 250 <= v[2] < 256:
				Bands.blue_10.append(v)
			else:
				continue
	
		for v in num_green:
			if 0 <= v[1] < 25:
				Bands.green_1.append((v))
			elif 25 <= v[1] < 50:
				Bands.green_2.append((v))
			elif 50 <= v[1] < 75:
				Bands.green_3.append(v)
			elif 75 <= v[1] < 100:	
				Bands.green_4.append(v)
			elif 100 <= v[1] < 125:
				Bands.green_5.append(v)
			elif 125 <= v[1] < 150:
				Bands.green_6.append(v)
			elif 150 <= v[1] < 175:
				Bands.green_7.append(v)
			elif 175 <= v[1] < 200:
				Bands.green_8.append(v)
			elif 200 <= v[1] < 250:
				Bands.green_9.append(v)
			elif 250 <= v[1] < 256:
				Bands.green_10.append(v)
			else:
				continue
		
		for v in num_gray:
			if 0 <= max(v) < 25:
				Bands.gray_1.append(v)
			elif 25 <= max(v) < 50:
				Bands.gray_2.append(v)
			elif 50 <= max(v) < 75:
				Bands.gray_3.append(v)
			elif 75 <= max(v) < 100:
				Bands.gray_4.append(v)
			elif 100 <= max(v) < 125:
				Bands.gray_5.append(v)
			elif 125 <= max(v) < 150:
				Bands.gray_6.append(v)
			elif 150 <= max(v) < 175:
				Bands.gray_7.append(v)
			elif 175 <= max(v) < 200:
				Bands.gray_8.append(v)
			elif 200 <= max(v) < 250:
				Bands.gray_9.append(v)
			elif 250 <= max(v) < 256:
				Bands.gray_10.append(v)
			else:
				continue

	def src_bands(self):
		# Copies the bands into permanent source lists
  
		Bands.src_red_1 = Bands.red_1[:]
		Bands.src_red_2 = Bands.red_2[:]
		Bands.src_red_3 = Bands.red_3[:]
		Bands.src_red_4 = Bands.red_4[:]
		Bands.src_red_5 = Bands.red_5[:]
		Bands.src_red_6 = Bands.red_6[:]
		Bands.src_red_7 = Bands.red_7[:]
		Bands.src_red_8 = Bands.red_8[:]
		Bands.src_red_9 = Bands.red_9[:]
		Bands.src_red_10 = Bands.red_10[:]

		Bands.src_green_1 = Bands.green_1[:]
		Bands.src_green_2 = Bands.green_2[:]
		Bands.src_green_3 = Bands.green_3[:]
		Bands.src_green_4 = Bands.green_4[:]
		Bands.src_green_5 = Bands.green_5[:]
		Bands.src_green_6 = Bands.green_6[:]		
		Bands.src_green_7 = Bands.green_7[:]
		Bands.src_green_8 = Bands.green_8[:]
		Bands.src_green_9 = Bands.green_9[:]
		Bands.src_green_10 = Bands.green_10[:]

		Bands.src_blue_1 = Bands.blue_1[:]
		Bands.src_blue_2 = Bands.blue_2[:]
		Bands.src_blue_3 = Bands.blue_3[:]
		Bands.src_blue_4 = Bands.blue_4[:]
		Bands.src_blue_5 = Bands.blue_5[:]
		Bands.src_blue_6 = Bands.blue_6[:]
		Bands.src_blue_7 = Bands.blue_7[:]
		Bands.src_blue_8 = Bands.blue_8[:]
		Bands.src_blue_9 = Bands.blue_9[:]
		Bands.src_blue_10 = Bands.blue_10[:]

		Bands.src_gray_1 = Bands.gray_1[:]
		Bands.src_gray_2 = Bands.gray_2[:]
		Bands.src_gray_3 = Bands.gray_3[:]
		Bands.src_gray_4 = Bands.gray_4[:]
		Bands.src_gray_5 = Bands.gray_5[:]
		Bands.src_gray_6 = Bands.gray_6[:]
		Bands.src_gray_7 = Bands.gray_7[:]
		Bands.src_gray_8 = Bands.gray_8[:]
		Bands.src_gray_9 = Bands.gray_9[:]
		Bands.src_gray_10 = Bands.gray_10[:]

		Bands.wb_reds = [
			Bands.src_red_1, 
			Bands.src_red_2, 
			Bands.src_red_3, 
			Bands.src_red_4,
			Bands.src_red_5, 
			Bands.src_red_6, 
			Bands.src_red_7, 	
			Bands.src_red_8, 
			Bands.src_red_9, 
			Bands.src_red_10,	
			]	
		
		Bands.wb_greens = [
			Bands.src_green_1, 
			Bands.src_green_2, 
			Bands.src_green_3, 
			Bands.src_green_4, 
			Bands.src_green_5, 
			Bands.src_green_6,
			Bands.src_green_7, 
			Bands.src_green_8, 
			Bands.src_green_9, 
			Bands.src_green_10
			]
	
		Bands.wb_blues = [
			Bands.src_blue_1, 
			Bands.src_blue_2, 
			Bands.src_blue_3, 
			Bands.src_blue_4, 
			Bands.src_blue_5, 
			Bands.src_blue_6, 
			Bands.src_blue_7, 
			Bands.src_blue_8, 
			Bands.src_blue_9, 
			Bands.src_blue_10
			]
	
	def clear_bands(self):
		# clears the bands lists.

		del Bands.red_1[:]
		del Bands.red_2[:]
		del Bands.red_3[:]
		del Bands.red_4[:]
		del Bands.red_5[:]
		del Bands.red_6[:]
		del Bands.red_7[:]
		del Bands.red_8[:]
		del Bands.red_9[:]
		del Bands.red_10[:]
	
		del Bands.green_1[:]
		del Bands.green_2[:]
		del Bands.green_3[:]
		del Bands.green_4[:]
		del Bands.green_5[:]
		del Bands.green_6[:]
		del Bands.green_7[:]
		del Bands.green_8[:]
		del Bands.green_9[:]
		del Bands.green_10[:]
	
		del Bands.blue_1[:]
		del Bands.blue_2[:]
		del Bands.blue_3[:]
		del Bands.blue_4[:]
		del Bands.blue_5[:]
		del Bands.blue_6[:]
		del Bands.blue_7[:]
		del Bands.blue_8[:]
		del Bands.blue_9[:]
		del Bands.blue_10[:]

		del Bands.gray_1[:]
		del Bands.gray_2[:]
		del Bands.gray_3[:]
		del Bands.gray_4[:]
		del Bands.gray_5[:]
		del Bands.gray_6[:]
		del Bands.gray_7[:]
		del Bands.gray_8[:]
		del Bands.gray_9[:]
		del Bands.gray_10[:]
		
			
			
