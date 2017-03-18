import os
import re

target_file = "/Users/kay/homework/django-document/Authentication_Customizing-authentication-in-django.md"
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
            find_target = re.findall('#', line)
            if len(find_target) > 0:
                target = re.sub('#+', r'\g<0> ', line)
                result += target
            else:
                result += line

    with open(target_file, 'w') as r:
        r.write(result)










# with open(target_file, 'rt') as f:
#     # 파일에서 #  바로 뒤에 비 공백문자 /S 가 오는 #을 찾는다
#     # 코드블럭으로 싸여있는 # 제외
#
#     # readlines 함수를 이용하여 파일의 모든 라인을 읽는다
#     # readlines 함수는 각 라인을 요소로 갖는 리스트를 리턴한다
