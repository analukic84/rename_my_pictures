import itertools

# filenames for open or save files
# start_number is the first item number to be written
file_open = 'case.txt'
file_save = 'case_rename.bat'
start_number = 677

# signs are suffixes for iterating, 7 pics (suffix) of 1 item
# i is index for following 7 pictures before increasing start_number of item
renamed_files_list = []
signs = itertools.cycle(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
i = 1

# open file_open, split into lines, creating image_files_list with only filenames.
with open(file_open, 'r') as file:
    file = [line.strip() for line in file.readlines()]
    image_files_list = [image.split(' ')[-1] for image in file]

# iterating over image_files_list, renaming every line in appropriate format.
# Keep changes in new list - renamed_files_list
# After every 7 filenames, increase start_number and start over again from "a"
for image_file in image_files_list:
    new_line = f'rename "{image_file}" "case{start_number}{next(signs)}.jpg"\n'
    renamed_files_list.append(new_line)

    if i % 7 == 0:
        start_number += 1
        i = 0

    i += 1

# save renamed_files_list into file_save
with open(file_save, 'w') as file:
    file.writelines(renamed_files_list)