"""
Cowsay but cat
"""

import sys

# params
BALLOON_BORDERS_SIZE = 4
MAX_WIDTH = 64

CAT = """ /\\_/\\
( o.o )
 > ^ <"""

say = " ".join(sys.argv[1:])
say_size = len(say)
cat_width = len(CAT.split("\n")[0])
max_text_width = MAX_WIDTH - BALLOON_BORDERS_SIZE
total_text_lines = int(say_size / max_text_width) + 1
lines_to_be_printed = [
    say[i * max_text_width : (i + 1) * max_text_width] for i in range(total_text_lines)
]

if len(lines_to_be_printed) > 0:
    first_line = lines_to_be_printed[0]
    last_line = lines_to_be_printed[-1]
    size_diff = len(first_line) - len(last_line)
    lines_to_be_printed[-1] = f"{last_line}{' ' * size_diff}"


print("-" * (BALLOON_BORDERS_SIZE + len(lines_to_be_printed[0])))
for line in lines_to_be_printed:
    print(f"| {line} |")
print("-" * (BALLOON_BORDERS_SIZE + len(lines_to_be_printed[0])))
print(" " * cat_width + "/")
print(CAT)
