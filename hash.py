from filehash import FileHash
file = "lib.dll"
md5hasher = FileHash('md5')
print("md5: ",md5hasher.hash_file(file))
sha1hasher = FileHash('sha1')
print("sha1: ",sha1hasher.hash_file(file))