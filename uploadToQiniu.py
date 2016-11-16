#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qiniu
import urllib
import os
import sys
import json

with open('config.json', 'r') as f:
	config = json.load(f)
# ----------------手动配置区---------------
accessKey = config['AK']#"4usYI7rJ2XDeatbEL1XRXZylP1XbalTEWTV2zUIc"
secretkey = config['SK']#"4e0Ia1Li9txMAt_P61WDmEpgLy1b4RMFIozGEbbs"
# 上传空间的域名，需要自己去后台获取
bucket_url =  {
	"fcc-blogs": "ogit74i74.bkt.clouddn.com",
}

bucket = config['bucket']#"fcc-blogs"  # 上传空间

# ----------------默认配置区-------------------------
img_suffix = ["jpg", "jpeg", "png", "bmp", "gif"]
os.chdir(sys.path[0])
result_file = "上传结果.txt"  # 保存上传结果

if os.path.exists(result_file):
	os.remove(result_file)


class Qiniu(object):

	"""七牛上传与下载的工具类

	需要七牛的Python SDK
	pip install qiniu
	SDK详细用法见　http://developer.qiniu.com/docs/v6/sdk/python-sdk.html
	"""
	SUCCESS_INFO = "上传成功！"

	def __init__(self, accessKey, secretkey):
		self.accessKey = accessKey
		self.secretkey = secretkey
		self._q = qiniu.Auth(self.accessKey, self.secretkey)

	def upload_file(self, bucket, up_filename, file_path):
		"""上传文件

		Args:
			bucket: 上传空间的名字
			up_filename: 上传后的文件名
			file_path:   本地文件的路径
		Returns:
			ret:     dict变量，保存了hash与key（上传后的文件名）
			info:    ResponseInfo对象，保存了上传信息
			url:     st, 上传后的网址
		"""
		token = self._q.upload_token(bucket)
		ret, info = qiniu.put_file(token, up_filename, file_path)
		url = self.get_file_url(bucket, up_filename)
		return ret, info, url

	def get_file_url(self, bucket, up_filename):
		if not bucket in bucket_url.keys():
			raise AttributeError("空间名不正确！")
		url_prefix = bucket_url[bucket]
		url = url_prefix + "/" + up_filename
		return url

def upload_from(file_path, custom_name):
	if not os.path.isfile(file_path):
		print "please specify a file path"
		return
	if custom_name == "":
		print "custom name must not be \"\""
		return

	q = Qiniu(accessKey, secretkey)
	ret, info, url = q.upload_file(bucket, custom_name, file_path)
	print("已上传： %s " % url)
	return url
	pass

def main():
	print("deodemdeo")
	if len(sys.argv) < 3:
		print "please input custom name and file path"
		sys.exit(0)

	customName = sys.argv[1]
	file = sys.argv[2]
	upload_from(file, customName)
	pass

if __name__ == '__main__':
	upload_from("1.jpg", "demo1.jpg")

