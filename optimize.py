#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import subprocess

def optimizeFromPath(path):
	cmd = '/Applications/ImageOptim.app/Contents/MacOS/ImageOptim'
	subprocess.call([cmd, path])
	pass

def main():

	if len(sys.argv) == 1:
		path = './images/7cacb28dacb0c78fd3e414f11e2b9960_image_3.png'
		optimizeFromPath(path)
	elif len(sys.argv) == 2:
		optimizeFromPath(sys.argv[1])
	else:
		print 'too many arguments'
		pass

	pass


if __name__ == '__main__':
	main()