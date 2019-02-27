# -*- coding:utf-8 -*
import struct
import hashlib
import hmac
# 任意数据类型变成 bytes
bt = struct.pack('>I', 2018)
print('bytes:', bt)
st = struct.unpack('>I', bt)
print('str:', st)
# 哈希:md5 ==> SHA1 ==> SHA256
md5 = hashlib.md5()
md5.update('hello, hash md5'.encode('utf-8'))
print('digest:', md5.hexdigest())
# 防止彩虹表： hmac(加盐salt混入)
# h = hmac.new(b'salt', b'hello', digestmod='MD5')
# hc = h.hexdigest()
# print('hamc digest:', hc)