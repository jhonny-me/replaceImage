#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib2
import urllib

import uploadToQiniu

def downloadImgFrom(url, filename, toLocalPath):
	print "start download" + url
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
	headers = {'User-Agent': user_agent, "Connection": "Keep-Alive"}

	req = urllib2.Request(url=url,headers=headers)
	imageData = urllib2.urlopen(req).read()

	output = open(toLocalPath, 'wb')
	output.write(imageData)
	output.close()
	# if os.path.exists(filename):

	# 	pass
	pass

def generateWorkingDir(path = "images"):
	print "generate work dir"
	if not os.path.exists(path):
		os.mkdir(path)
		pass
	return os.path.normpath(os.path.join(os.getcwd(), path))
	pass

def generateImageName(url, custom_name=''):
	print "generate image name"
	originalName = url.rsplit('/', 1)[-1]
	extension = originalName.rsplit('.', 1)[-1]
	if custom_name == '':
		return originalName
	custom_name_parts = custom_name.rsplit('.', 1)	
	if len(custom_name_parts) == 1:
		return custom_name + '.' + extension
	return custom_name

def replaceToCNUrl(url, custom_name=''):
	imageName = generateImageName(url, custom_name)
	workingDir = generateWorkingDir()
	fullPath = os.path.join(workingDir, imageName)
	print fullPath
	downloadImgFrom(url, imageName, fullPath)
	uploadToQiniu.upload_from(fullPath, imageName)
	pass

def main():
	#this is only for testing
	if len(sys.argv) == 1:
		picurl="http://images.51cto.com/files/uploadimg/20100630/104906665.jpg"
		replaceToCNUrl(picurl)
	elif len(sys.argv) == 2:
		replaceToCNUrl(sys.argv[1])
	elif len(sys.argv) == 3:
		replaceToCNUrl(sys.argv[1], sys.argv[2])
	else:
		print 'too many arguments'

	pass

if __name__ == '__main__':
	main()