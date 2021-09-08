import os
import readline
import re

only_one = []

for root, dirs, files in os.walk("."):
    for filename in files:
        file_path = "{}/{}".format(root, filename)
        count = len(open(file_path).readlines(  ))
        if count == 1:
            only_one.append(file_path)
for path in only_one:
    with open(path) as f:
        first_line = f.readline()
    if re.match(r"^(.+)\/([^\/]+)$", first_line):
        symlink_list = "".join(c for c in first_line if c.isprintable())
        os.remove(path)
        os.symlink(first_line, path)