import os
import re

BASE_DIR = '/Users/kay/'
TARGET_DIR = os.path.join(BASE_DIR, input())

md_files = []
for file in os.listdir(TARGET_DIR):
    if file.endswith('.md'):
        md_files.append(os.path.join(TARGET_DIR, file))
print(md_files)

for target_file in md_files:
    result = ''
    with open(target_file, 'rt') as f:
        for line in f:
            result += re.sub('#+', r'\g<0> ', line)
            # if len(find_target) > 0:
            #     target = re.sub('#+', r'\g<0> ', line)
            #     result += target
            # else:
            #     result += line

    with open(target_file, 'w') as r:
        r.write(result)
