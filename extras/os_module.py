import os

print("No. CPUs:", os.cpu_count())
print("Encoding:", os.device_encoding(0))
print("Terminal size:", os.get_terminal_size())
print("Dir tree:", os.walk('./'))

dir_tree = os.walk('./')

for tree in dir_tree:
    print(tree)