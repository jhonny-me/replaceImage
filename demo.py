
print 'hello,world'

import sys
import md5

# for x in range(len(sys.argv)):
# 	print sys.argv[x]
# 	pass

# generate UUID for file name
def generateUUID(name):
	return md5.new(name).digest()
	pass

print generateUUID(sys.argv[1])