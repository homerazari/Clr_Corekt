import analyzer
import copy
from numpy import std


class Standard_Dev(object):
	"""Return standard deviation of white balance/rgb

	Loops through list until the pixels that deviate
	from the rest of the list are singled out
	"""
	
	def __init__(self):
		pass

	def wb_stdv(self, color_list):
		self.color_list = color_list

		global bw_tmp_val
		base_val = [0]
		tmp_num = 0
		bw_tmp_val = []
		wb_stdev = 20
		found = False
	
		while found == False:
			for i in color_list:
				if std(i) < wb_stdev:	
					bw_tmp_val.append(i)
		
			tmp_num = len(bw_tmp_val)
			base_val.append(tmp_num % len(color_list))	
	
			if len(base_val) > 2 and (base_val[-1] / float(base_val[-2])) < .9:
				found = True	
			else:
				bw_tmp_val = []
				wb_stdev -= 1
		
		return wb_stdev
	
	def rgb_stdv(self, color_list):
		self.color_list = color_list

		global rgb_tmp_val
		base_val = [0]
		tmp_num = 0
		rgb_tmp_val = []
		rgb_stdev = .25
		found = False
		while found == False:
			for i in color_list:
				srt_val = sorted(i, reverse=True)
				pct = srt_val[1] / float(srt_val[0])			
				if std((.5, pct)) < rgb_stdev:	
					rgb_tmp_val.append(i)
			
			tmp_num = len(rgb_tmp_val)
			base_val.append(tmp_num % len(color_list))
			if len(base_val) > 2 and (base_val[-1] / float(base_val[-2])) < .9:
				found = True	
			else:
				rgb_tmp_val = []
				rgb_stdev -= .02
	
		return rgb_stdev
		

class Corrector(object):
	""" Methods that correct the RGB list

	Corrects the white balance and RGB lists and then compares them to the source
	"""

	def __init__(self):
		pass

	curves = ""
	
	def WB_correct(self, color_list, wb_stdev):
		self.color_list = color_list
		self.wb_stdev = wb_stdev	
		
		stdev = 4.25
		tmp_stdev = wb_stdev
		std_met = False
	
		if color_list == 'reds_list':	
			while std_met == False:
				for i in color_list:
					if i[1] < i[0] > i[2] and stdev < std(i) < tmp_stdev:
						i[1] += 1
						i[2] += 1	
					elif i[1] < i[0] <= i[2] and stdev < std(i) < tmp_stdev:
						i[1] += 1
						i[2] = i[0]	
					elif i[2] < i[0] <= i[1] and stdev < std(i) < tmp_stdev:
						i[1] = i[0]
						i[2] += 1
					else:
						continue
	
			
				tmp_len = len(color_list)
				len_check = 0
				for i in color_list:
					if std(i) >= tmp_stdev:
						len_check += 1
					else:
						continue
				if len_check == tmp_len:
					std_met = True
				else:
					continue
	
	
		elif color_list == 'greens_list':	
			while std_met == False:
				for i in color_list:
					if i[0] < i[1] > i[2] and stdev < std(i) < tmp_stdev:
						i[0] += 1
						i[2] += 1	
					elif i[0] < i[1] <= i[2] and stdev < std(i) < tmp_stdev:
						i[0] += 1
						i[2] = i[1]	
					elif i[2] < i[1] <= i[0] and stdev < std(i) < tmp_stdev:
						i[0] = i[1]
						i[2] += 1
					else:
						continue
	
			
				tmp_len = len(color_list)
				len_check = 0
				for i in color_list:
					if std(i) >= tmp_stdev:
						len_check += 1
					else:
						continue
				if len_check == tmp_len:
					std_met = True
				else:
					continue
	
	
		elif color_list == 'blues_list':	
			while std_met == False:
				for i in color_list:
					if i[0] < i[2] > i[1] and stdev < std(i) < tmp_stdev:
						i[0] += 1
						i[1] += 1	
					elif i[0] < i[2] <= i[1] and stdev < std(i) < tmp_stdev:
						i[0] += 1
						i[1] = i[2]	
					elif i[1] < i[2] <= i[0] and stdev < std(i) < tmp_stdev:
						i[0] = i[2]
						i[1] += 1
					else:
						continue
	
			
				tmp_len = len(color_list)
				len_check = 0
				for i in color_list:
					if std(i) >= tmp_stdev:
						len_check += 1
					else:
						continue
				if len_check == tmp_len:
					std_met = True
				else:
					continue
	
		
		return color_list
		
	def RGB_correct(self, wb_list):
		self.wb_list = wb_list

		tmp_val = rgb_tmp_val
		for i in wb_list:
			for j in tmp_val:
				if i == j:
					srt_val = sorted(i, reverse=True)
					clr_line = max(i) / 2
					if max(i) == i[0] and srt_val[1] <= clr_line and srt_val[2] == i[2]:
						i[1] = int(srt_val[1]*.6)
					elif max(i) == i[0] and srt_val[1] <= clr_line and srt_val[2] == i[1]:
						i[2] = int(srt_val[1]*.6)
					elif max(i) == i[1] and srt_val[1] <= clr_line and srt_val[2] == i[2]:
						i[0] = int(srt_val[1]*.6)
					elif max(i) == i[1] and srt_val[1] <= clr_line and srt_val[2] == i[0]:
						i[2] = int(srt_val[1]*.6)
					elif max(i) == i[2] and srt_val[1] <= clr_line and srt_val[2] == i[1]:
						i[0] = int(srt_val[2]*.6)
					elif max(i) == i[2] and srt_val[1] <= clr_line and srt_val[2] == i[0]:
						i[1] = int(srt_val[2]*.6)					
					else:
						continue
				else:
					continue
	
		return wb_list		
	
	def exposure_correct(self, corrected_list):
		self.corrected_list = corrected_list

		for i in corrected_list:
			if max(i) > 240 and min(i) >= 20:
				i[0] -= 20
				i[1] -= 20			
				i[2] -= 20
			elif std(i) <= 18 and min(i) > 240:
				i[0] -= 20
				i[1] -= 20			
				i[2] -= 20
			elif max(i) <= 20 and max(i) == i[0] and min(i) != i[1]:
				i[0] += 20
				i[1] += 20
			elif max(i) <= 20 and max(i) == i[0] and min(i) != i[2]:
				i[0] += 20
				i[2] += 20
			elif max(i) <= 20 and max(i) == i[1] and min(i) != i[0]:
				i[0] += 20
				i[1] += 20
			elif max(i) <= 20 and max(i) == i[1] and min(i) != i[2]:
				i[1] += 20
				i[2] += 20
			elif max(i) <= 20 and max(i) == i[2] and min(i) != i[0]:
				i[0] += 20
				i[2] += 20
			elif max(i) <= 20 and max(i) == i[2] and min(i) != i[1]:
				i[1] += 20
				i[2] += 20
			else:
				continue
	
		return corrected_list
		
	def curve_vals(self):				
	
		new_reds =  [
		     len(analyzer.Bands.red_1)/float(len(analyzer.Bands.src_red_1)+.001), 
		     len(analyzer.Bands.red_2)/float(len(analyzer.Bands.src_red_2)+.001), 
		     len(analyzer.Bands.red_3)/float(len(analyzer.Bands.src_red_3)+.001),
		     len(analyzer.Bands.red_4)/float(len(analyzer.Bands.src_red_4)+.001),
		     len(analyzer.Bands.red_5)/float(len(analyzer.Bands.src_red_5)+.001), 
		     len(analyzer.Bands.red_6)/float(len(analyzer.Bands.src_red_6)+.001),
		     len(analyzer.Bands.red_7)/float(len(analyzer.Bands.src_red_7)+.001), 
		     len(analyzer.Bands.red_8)/float(len(analyzer.Bands.src_red_8)+.001), 
		     len(analyzer.Bands.red_9)/float(len(analyzer.Bands.src_red_9)+.001), 
		     len(analyzer.Bands.red_10)/float(len(analyzer.Bands.src_red_10)+.001)
			]
		new_greens = [
		     len(analyzer.Bands.green_1)/float(len(analyzer.Bands.src_green_1)+.001), 
		     len(analyzer.Bands.green_2)/float(len(analyzer.Bands.src_green_2)+.001), 
		     len(analyzer.Bands.green_3)/float(len(analyzer.Bands.src_green_3)+.001),
		     len(analyzer.Bands.green_4)/float(len(analyzer.Bands.src_green_4)+.001),
		     len(analyzer.Bands.green_5)/float(len(analyzer.Bands.src_green_5)+.001),
		     len(analyzer.Bands.green_6)/float(len(analyzer.Bands.src_green_6)+.001),
		     len(analyzer.Bands.green_7)/float(len(analyzer.Bands.src_green_7)+.001),
		     len(analyzer.Bands.green_8)/float(len(analyzer.Bands.src_green_8)+.001),
		     len(analyzer.Bands.green_9)/float(len(analyzer.Bands.src_green_9)+.001),
		     len(analyzer.Bands.green_10)/float(len(analyzer.Bands.src_green_10)+.001),
			]
		new_blues = [
		     len(analyzer.Bands.blue_1)/float(len(analyzer.Bands.src_blue_1)+.001),
		     len(analyzer.Bands.blue_2)/float(len(analyzer.Bands.src_blue_2)+.001),
		     len(analyzer.Bands.blue_3)/float(len(analyzer.Bands.src_blue_3)+.001),
		     len(analyzer.Bands.blue_4)/float(len(analyzer.Bands.src_blue_4)+.001),
		     len(analyzer.Bands.blue_5)/float(len(analyzer.Bands.src_blue_5)+.001),
		     len(analyzer.Bands.blue_6)/float(len(analyzer.Bands.src_blue_6)+.001),
		     len(analyzer.Bands.blue_7)/float(len(analyzer.Bands.src_blue_7)+.001),
		     len(analyzer.Bands.blue_8)/float(len(analyzer.Bands.src_blue_8)+.001),
		     len(analyzer.Bands.blue_9)/float(len(analyzer.Bands.src_blue_9)+.001),
		     len(analyzer.Bands.blue_10)/float(len(analyzer.Bands.src_blue_10)+.001),
			]
		new_grays = [
		     len(analyzer.Bands.gray_1)/float(len(analyzer.Bands.src_gray_1)+.001),
		     len(analyzer.Bands.gray_10)/float(len(analyzer.Bands.src_gray_10)+.001)
			]

		curves_red = "r='0/" + str(.01*new_reds[0]/2) +  " .1/" + str(.1*new_reds[1]/2) + " .2/" + str(.2*new_reds[2]/2) +  \
		" .3/" + str(.3*new_reds[3]/2) + " .4/" + str(.4*new_reds[4]/2) + " .5/" + str(.5*new_reds[5]/2) + " .6/" + str(.6*new_reds[6]/2) \
		+ " .7/" + str(.7*new_reds[7]/2) + " .8/" + str(.8*new_reds[8]/2) + " 0.9/" + str(.9*new_reds[9]/2) + "':"  
	
		curves_green = "g='0/" + str(.01*new_greens[0]/2) +  " .1/" + str(.1*new_greens[1]/2) + " .2/" + str(.2*new_greens[2]/2) +  \
		" .3/" + str(.3*new_greens[3]/2) + " .4/" + str(.4*new_greens[4]/2) + " .5/" + str(.5*new_greens[5]/2) + " .6/" + str(.6*new_greens[6]/2) \
		+ " .7/" + str(.7*new_greens[7]/2) + " .8/" + str(.8*new_greens[8]/2) + " 0.9/" + str(.9*new_greens[9]/2) + "':" 
	
		curves_blue = "b='0/" + str(.01*new_blues[0]/2) +  " .1/" + str(.1*new_blues[1]/2) + " .2/" + str(.2*new_blues[2]/2) +  \
		" .3/" + str(.3*new_blues[3]/2) + " .4/" + str(.4*new_blues[4]/2) + " .5/" + str(.5*new_blues[5]/2) + " .6/" + str(.6*new_blues[6]/2) \
		+ " .7/" + str(.7*new_blues[7]/2) + " .8/" + str(.8*new_blues[8]/2) + " 0.9/" + str(.9*new_blues[9]/2) + "':"  

		curves_gray = "m='0/" + str(.1*new_grays[0]/2) + " .9/" + str(.9*new_grays[1]/2) + "'"

		curves = 'curves=' + curves_red + curves_green + curves_blue + curves_gray
		return curves


