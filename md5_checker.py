import hashlib

file_name = input("Enter file name: ")
md5_hash = input("Enter MD5 hash to check: ")

with open(file_name, "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)

if(md5_hash == file_hash.hexdigest()):
    print("Match found! Hash value: " + file_hash.hexdigest())
else:
    print("MD5 hash does not match. Hash value: " + file_hash.hexdigest())