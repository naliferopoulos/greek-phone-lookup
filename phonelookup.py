#!/usr/bin/env python
#
# *****************************************************************
#              Reverse Phone Lookup (Greek Numbers)
# *****************************************************************
#
# Author: Nick Aliferopoulos
# aliferopoulos@icloud.com
#

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import urllib2
from BeautifulSoup import BeautifulSoup

class PhoneLookup(object):

    def __init__(self, num):
        self.num = num

    def lookup(self):
        print("Looking for %s" % (self.num))
	target = "http://www.11888.gr/list-names?_wpType=number&_wpPhone=" + self.num
	content = urllib2.urlopen(target).read()
	parsed_html = BeautifulSoup(content)
	details = parsed_html.body.find('div', attrs={'class':'details'})
	if details is not None:
		print "Name: " + details.find('span').text
		print "Address: " + details.find('div', attrs={'class':'address'}).text
	else:
		print "Not found."
def main():
    parser = ArgumentParser(description='Phone Lookup', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('number', help = 'Target phone number')
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0')
    args = parser.parse_args()

    pl = PhoneLookup(args.number)
    pl.lookup()

if __name__ == '__main__':
    main()
