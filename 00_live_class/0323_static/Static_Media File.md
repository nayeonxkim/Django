# Static & Media File

## Static File

- 내가 개발하면서 웹 페이지에 넣은 이미지 파일 같은 것

- 파일 자체가 고정되어 있다.

- 이미지 파일을 요청 받으면, 해당 이미지 파일을 url형식으로 응답해야한다.

---

### 장고에서 정적파일 구성 및 사용하기

1. settings.pt 에서 `STATIC_URL` 정의하기

2. 앱의 static 폴더에 정적 파일들 두기

3. 템플릿에서 `load static`태그와  `static` 태그를 사용하여 지정된 정로에 있는 정적 파일 url 생성하기

---

## Media File

- 유저가 웹에서 업로드하는 정적 파일

- Form을 사용한다. : 필드를 정의해주어야 데이터를 받을 수 있다.

- 폼에 이미지필드가 있음 !

---

### 장고에서 미디어 파일 사용하기

1. settings.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정하기

2. 선택사항) `upload_to` 속성을 정의하여 업로드된 파일에 사용할 `MEDIA_ROOT`의 하위 경로를 지정
