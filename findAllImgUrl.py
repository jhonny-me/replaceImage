#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re

def find(file_name):
	with open(file_name) as f:
		content = f.read()
	s = re.findall(r'https?\:\/\/.+\.(?:jpe?g|gif|png)', content)
	print s
	return s

def write_url_back(file_name, original_urls,replaced_urls):
	with open(file_name, 'r+') as f:
		content = f.read()
		for x in range(len(original_urls)):
			content = content.replace(original_urls[x], replaced_urls[x])
			pass
		f.seek(0)
		f.write(content)
		f.truncate()
	pass

def main():
	find(sys.argv[1])
	pass

if __name__ == '__main__':
	main()