#!/usr/bin/python

from Modules import analyzer
from Modules import correct
from numpy import std
from subprocess import Popen, PIPE



pic = analyzer.Bands()
clr_pre_wb = []	
reds_list = []
greens_list = []
blues_list = []
clr_pre_clr = []
clr_pre_exp = []

Corekt = correct.Corrector()
Dev = correct.Standard_Dev()
pic.bands(analyzer.Processor.pixels)



pic.src_bands()

for i in pic.wb_reds:
	reds_list += [j for j in i]

for i in pic.wb_greens:
	greens_list += [j for j in i]

for i in pic.wb_blues:
	blues_list += [j for j in i]

clr_pre_wb += [i for i in reds_list]
clr_pre_wb += [i for i in greens_list]
clr_pre_wb += [i for i in blues_list]

wb_stdev = Dev.wb_stdv(clr_pre_wb)
rgb_stdev = Dev.rgb_stdv(clr_pre_wb)

wb_r_list = Corekt.WB_correct(reds_list, wb_stdev)
wb_g_list = Corekt.WB_correct(greens_list, wb_stdev)
wb_b_list = Corekt.WB_correct(blues_list, wb_stdev)


clr_pre_clr += [i for i in wb_r_list]
clr_pre_clr += [i for i in wb_g_list]
clr_pre_clr += [i for i in wb_b_list]


clr_pre_expo = Corekt.RGB_correct(clr_pre_clr)

clr_pre_curv = Corekt.exposure_correct(clr_pre_expo)

pic.bands(clr_pre_curv)

curv = Corekt.curve_vals()
output_spec = [
	'ffmpeg',
	'-y',
	'-i', pic.infile,
	'-vf', curv,
	'output.png'
	]


output = Popen(output_spec, stdout=PIPE)
output.wait()
	
	

<<<<<<< HEAD

=======
>>>>>>> 2219b0987d0220a5491aca09be850db050198558
