file_name = 'words.txt'
# with open(file_name, 'w') as f:
#     f.write("Hello, World \n")
#     f.write("alksjdlaksjdlkasjdkl \n")
# with open(file_name, 'a') as f:
#     f.write("What's your favourite Language? \n")
#     f.write('My favourite language is python too..')
with open(file_name, 'r') as f:
    stringsss = f.read()

print(stringsss)