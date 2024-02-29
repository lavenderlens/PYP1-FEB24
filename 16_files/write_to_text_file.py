file = open('data.txt', mode='a')
# 1. mode w overwrites
# 2. mode x creates, raises error if exists: FileExistsError: [Errno 17] File exists: 'data.txt'
# 3. mode a appends

# methods
# 1. write
# 2. writelines

# 1.write
text = '\nThis is additional text to write to file'
file.write(text)

#2. writelines
lines = ["\nextra line 1","\nextra line 2","\nextra line 3"]
file.writelines(lines)

file.close()