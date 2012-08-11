# This was created by Ryan Jobson

import string
import random
import os
from urllib2 import urlopen
from sys import argv

path = "/Users/Family/Pictures/Imgur/"	# This is the folder where the images are stored
storeName = 'RandomImage' # The base name for all of the images

# Creates a list of all letters and numbers 0-9
choices = []
for letter in string.letters:
	choices.append(letter)
i=0
while i < 10:
	choices.append(str(i))
	i+=1



# Creates a random imgur url from "choices" 
def RandomUrl():
	s = []
	for i in range(0,5):
		s.append(random.choice(choices))
	s = ''.join(s)
	return "http://imgur.com/%s.jpg" % s

# Finds a storing name
def StoringName(name):
	filename = name +'.jpg'
	imageFile = path + filename
	if os.path.exists(imageFile):
		count = 0
		for files in os.listdir(path):
			if name in files:
				count+=1

		finalpath = path+name+str(count)+'.jpg' # Appends numbers to the end of the file to prevent overwrite
		return finalpath

	else:
		return imageFile # Returns the name if no conflicts found




def ImgurRandom(url):
	image = urlopen(url)
	print "Trying", url
	imagesize = image.info().getheaders("Content-Length")[0]
	if int(imagesize) != 503: # This is the size of the error image
		image = image.read()
		filepath = StoringName(storeName)
		name = open(filepath, 'wb')
		name.write(image)
		print "Wrote %s to %s\n" % (url, filepath)
		
	else:
		print 'Nope\n'
		ImgurRandom(RandomUrl())
	

def main():
	try:				# Number argument can be added to download more than one image at a time
		numtimes = argv[1]
		for i in range(0,int(numtimes)):
			ImgurRandom(RandomUrl())

	except IndexError:
		ImgurRandom(RandomUrl())

main()
