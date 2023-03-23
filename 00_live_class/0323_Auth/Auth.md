# Auth

- 인증 : 로그인 했는지 확인

- 권한 : 로그인 ok, 요청 권한이 있는지 확인
  
  - A로 로그인했으나 B가 쓴 글은 게시글을 삭제/수정할 수는 없어야한다.

- 인증을 하려면 유저 데이터가 필요함 -> User Model을 정의해야한다.
  
  - 장고의 기본 UserModel을 custom하여 사용 

---

# 순서

1. accounts 애플리케이션 생성 및 기본 설정

2. accounts의 models.py에서 UserModel 정의하기
- 원래 쓰는 models.Model말고 유저 모델만을 위한 모델 클래스인 AbstactUser 사용해서  User클래스 만들어줌.
3. settings.py에 AUTH_USER_MODEL 설정
- 기존에 user 모델이 있기 때문에 내가 커스텀한 모델로 대체 해주어야함.

- AUTH_USER_MODEL = 'accounts.User' : accounts의 User모델을 기본 유저모델로 설정해줘
4. admin.py에 User모델을 등록
- 원래다른 모델 만들때는 admin.site.register에 모델명만 넣었음

- User 모델은 UserAdmin도 인자로 같이 넣어줘야함.
5. migrations (____init____ 은 놔두고!!) 날리고, db delete하기

6. 다시 makemigrations, migrate 

-> auth_user 없어지고 accounts_user 생김 
