import hashlib

with open('python-3.12.4-amd64.exe', 'rb') as f:
    md5_hash = hashlib.file_digest(f, 'md5')

print(md5_hash.hexdigest())