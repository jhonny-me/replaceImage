#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import hashlib
import os
import findAllImgUrl
import replaceToCNUrl

# for x in range(len(sys.argv)):
# 	print sys.argv[x]
# 	pass

# generate UUID for file name
def generateUUID(name):
	return hashlib.md5(name).hexdigest()#md5.new(name).digest()
	pass


def custom_image_name(file_name,urls):
	custom_names = []
	base_name = generateUUID(file_name)
	for x in range(len(urls)):
		name = base_name + '_image_' + str(x)
		custom_names.append(name)
		pass
	return custom_names
	pass

def processWith(file_or_dir):
	if os.path.isfile(file_or_dir):
		urls = findAllImgUrl.find(file_or_dir)
		names = custom_image_name(file_or_dir, urls)
		replaced_urls = []
		for x in range(len(urls)):
			url = replaceToCNUrl.replaceToCNUrl(urls[x],names[x])
			replaced_urls.append(url)
			pass
		print replaced_urls
		findAllImgUrl.write_url_back(file_or_dir,urls,replaced_urls)
		print 'all done'
		pass
	pass

def main():
	if not len(sys.argv) == 2:
		print 'please check document for correct param input'
	processWith(sys.argv[1])

if __name__ == '__main__':
	main()