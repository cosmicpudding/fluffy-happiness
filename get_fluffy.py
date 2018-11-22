# Fluffy Happiness: Test code to grab pictures of cute animals from
# the Internet
# Usage: >> python get_fluffy.py [options] V.A. Moss
# (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$22-oct-2018 22:00:00$"
__version__ = "0.2"

# Imports
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
import ssl
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from argparse import ArgumentParser, RawTextHelpFormatter

parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument('-k', '--keywords',
		    default='cute fluffy animal',
		    type=str,
		    help='Specify which kind of search to do(default: %(default)s)')

# Parse the arguments above
args = parser.parse_args()

# Path format
path = 'https://imgur.com/search/score?q=%s' % ('+'.join(args.keywords.split()))

# Get data from website
request = urllib.request.Request(path)
response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
read_response = response.readlines()

# Possible cuteness
possible = []

for line in read_response:

	line = line.decode('utf-8')
	
	if '<img alt="" src="' in line:
		image_url = line.split('src="//')[1].split('"')[0]
		possible.append('http://'+image_url)

# Now select a random image to show
rand_int = randint(0,len(possible)-1)
print("I've selected image #%i: %s" % (rand_int,possible[rand_int]))

# Download the image and display it
# note: imgur adds a b to names for some reason.
img_name = (possible[rand_int].split('b.jpg')[0]+'.jpg').split('/')[-1]
image_path = 'https://i.imgur.com/'+img_name
urllib.request.urlretrieve('%s' % image_path,'%s' % img_name)

# Show the image in matplotlib
img=mpimg.imread('%s' % img_name)
imgplot = plt.imshow(img)
plt.show()

