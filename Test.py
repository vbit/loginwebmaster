import hashlib

m = hashlib.md5('abc123')
#m.update("abc123")
print m.hexdigest()