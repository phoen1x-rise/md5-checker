import hashlib

md5_hash = hashlib.md5()

def md5_hash_gen(file_name):
    with open(file_name, 'rb') as f:
        while chunk := f.read(8192):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

file_name = input('Enter the file name: ')
md5_existing = input('Enter the existing MD5 hash: ')

md5_generated = md5_hash_gen(file_name)

#print(f'Generated MD5 hash: {md5_generated}')

print('Match found!') if md5_existing == md5_generated else print('No match found! File is corrupt')