import re

target_file = "/Users/kay/homework/django-document/Authentication_Customizing-authentication-in-django.md"
# TARGET_DIR = input()
# match_md_file = re.match(r'.*md$')
# MD_FILES = os.path.join(TARGET_DIR, r'.*md$')
# print(MD_FILES)
# for target_file in MD_FILES:
#     with open(target_file, 'rt') as f:
#         for line in f:
#             target = re.sub(r'(?<=[#*])#', '? ', line)
#             print(target)

result = ''
with open(target_file, 'rt') as f:
    for line in f:
        find_target = re.findall('#', line)
        if len(find_target) > 0:
            target = re.sub('#+', r'\g<0> ', line)
            result += target
        else:
            result += line

result_file = target_file

with open(result_file, 'w') as r:
    r.write(result)










# with open(target_file, 'rt') as f:
#     # 파일에서 #  바로 뒤에 비 공백문자 /S 가 오는 #을 찾는다
#     # 코드블럭으로 싸여있는 # 제외
#
#     # readlines 함수를 이용하여 파일의 모든 라인을 읽는다
#     # readlines 함수는 각 라인을 요소로 갖는 리스트를 리턴한다
