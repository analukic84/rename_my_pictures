## Script to rename given filename into specific one.

Each item has 7 different pictures in 7 jpg files.
One item will have one particular item number, for example number 677 - case677
Every different picture of the item will have suffix of "a", "b", "c", etc...
Conclusion: this are filenames of one item:
  case677a - case677g (7 suffix letters:'a','b','c','d','e','f','g')

Imported .txt looks like this:
"
08/15/2021  18:15           699,294 2021-08-15-13-02-03.jpg
08/15/2021  18:15           625,702 2021-08-15-13-02-18.jpg
08/15/2021  18:15           966,594 2021-08-15-13-02-27.jpg
"
it obtained by command dir/s > file_open.txt - with deleted header and footer. No blank lines.

Exported .bat looks like this:
"
rename "2021-08-15-13-02-03.jpg" "case677a.jpg"
rename "2021-08-15-13-02-18.jpg" "case677b.jpg"
rename "2021-08-15-13-02-27.jpg" "case677c.jpg"
"
When we run exported .bat file, it will change all photos in current folder.

What script does?
open a file_open.txt
creates list (image_files_list) of picture filenames separated from text.
iterate over this list, it writes new lines into new list (renamed_files_list):
  up to 7 times it writes as one item with appropriate suffix,
  after 7 times, it increase item start number and continue in the same style

at the end, it saves changes in file_save


# Installation

Requires Python 3.7.

1. Clone the repository (going to a terminal and run `git clone git@github.com:analukic84/rename_pictures.git`.
2. Create a virtual environment for the repository (run `virtualenv --python=python3.7 venv`)
