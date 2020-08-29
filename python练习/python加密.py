import hashlib

s = '1213520abcd'

print('md5', hashlib.md5(s.encode('utf-8')).hexdigest())
print('sha1', hashlib.sha1(s.encode('utf-8')).hexdigest())
print('sha224', hashlib.sha224(s.encode('utf-8')).hexdigest())
print('sha256', hashlib.sha256(s.encode('utf-8')).hexdigest())
print('sha384', hashlib.sha384(s.encode('utf-8')).hexdigest())
print('sha512', hashlib.sha512(s.encode('utf-8')).hexdigest())

print('md5', len(hashlib.md5(s.encode('utf-8')).hexdigest()))
print('sha1', len(hashlib.sha1(s.encode('utf-8')).hexdigest()))
print('sha224', len(hashlib.sha224(s.encode('utf-8')).hexdigest()))
print('sha256', len(hashlib.sha256(s.encode('utf-8')).hexdigest()))
print('sha384', len(hashlib.sha384(s.encode('utf-8')).hexdigest()))
print('sha512', len(hashlib.sha512(s.encode('utf-8')).hexdigest()))