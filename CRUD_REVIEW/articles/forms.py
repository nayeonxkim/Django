# create.html의 form 안쪽을 채워주는 역할
# 원래는 label, input하나하나 만들어줬는데 forms를 사용하면 form안에 적어야할 내용을 쉽게 채울 수 있다.

# 특히 ModelForms는, 모델의 정보를 토대로 form을 생성해준다.
# 즉, (모델을 기반으로 만들어지는)DB에 넣을거 어차피 입력받을거니깐 모델에 있는 정보를 입력받을 수 있게 하는 것이다.


from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:

        # 내가 models.py에 정의한 특정 클래스(모델)를 기반으로 한다.
        # models.py에 있는 여러 모델 중, 이 폼은 Article모델을 기준으로 생성된다.
        model = Article

        # Article에 있는 field 중 어떤 필드를 입력받을지 정한다.
        # 일단은 모든 필드를 전부 폼에 넣을 것이니 all로 지정한다.
        fields = '__all__'

        