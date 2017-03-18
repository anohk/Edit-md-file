# md file을 자동으로 수정하는 기능을 만들고 있습니다.

### editheader.py

헤더를 작성할 때, `#`뒤에 공백없이 타이틀을 작성해왔는데 이제 이렇게 작성하는 것이 허용되지 않아 md파일의 헤더가 모두 깨졌습니다. 따라서 `#`뒤에 공백을 하나 넣어주는 기능을 python 코드로 구현했습니다.

현재 진행상황:
파일을 실행시키고 md파일이 있는 directory path를 모두 작성해야함.

```
>>> python editheader.py
>>> homework/django-document/
	# /Users/kay/homework/django-document/ 안에 md 파일들이 있는 경우
```
