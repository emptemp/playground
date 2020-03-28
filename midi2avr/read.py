import midi
import re

c3   = 130.8	#60
cis3 = 138.6	#61
d3   = 146.8 	#62
dis3 = 155.6	#63
e3   = 164.8	#64
f3   = 174.6	#65
fis3 = 185	#66
g3   = 196.0	#67	
gis3 = 207.7	#68
a3   = 220	#69
ais3 = 233.1	#70
h3   = 246.9	#71

c4   = 261.6	#72
cis4 = 277.2	#73
d4   = 293.7 	#74
dis4 = 311.1	#75
e4   = 329.6	#76
f4   = 349.2	#77
fis4 = 370	#78
g4   = 392	#79	
gis4 = 415.3	#80
a4   = 440	#81
ais4 = 466.2	#82
h4   = 493.9	#83

c5   = 523.3	#84

presc = 1/(312500*1.0)
print presc	

notes = {"60" : c3,
	 "61" : cis3,
	 "62" : d3,
	 "63" : dis3,
	 "64" : e3,
	 "65" : f3,
	 "66" : fis3,
	 "67" : g3,
	 "68" : gis3,
	 "69" : a3,
	 "70" : ais3,
	 "71" : h3,
	 "72" : c4,
	 "73" : cis4,
	 "74" : d4,
	 "75" : dis4,
	 "76" : e4,
	 "77" : f4,
	 "78" : fis4,
	 "79" : g4,
	 "80" : gis4,
	 "81" : a4,
	 "82" : ais4,
	 "83" : h4,
	 "84" : c5  }


print "{"

pattern = midi.read_midifile("mario_mono_maxv_dead.mid")
for note in pattern[0]:
	string = str(note)
	note = re.findall(r"\[(\d*), (\d*)\]", string)
	if (len(note) > 0):
		if (int(note[0][0]) > 59 and int(note[0][1]) != 0):
			ocr = int((notes[note[0][0]])),
		        ocr_float = 1/(ocr[0]*16.0)			
			comp = int(ocr_float/presc)
			#print ocr_float			
			print comp,
			
			#print int(notes[note[0][0]]*8),
		
			#print (1/(ocr_float*4)/presc),			
			#if ( ocr[0] >= 255):
		#		print "!!!!!!!!!!!!",
			print ",",
		elif (int(note[0][0]) == 48 and int(note[0][1]) != 0 and int(note[0][1]) != 64):
			print "0",
			print ",",

print "}"
#			print "\t", 
#			print note[0][1]
#		print note[0][0],
#		print " , ",
#		print note[0][1],
#		print "\n"
