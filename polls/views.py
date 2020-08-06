from django.shortcuts import render, get_object_or_404
from polls.models import Question

# view의 function이 하는 일은 request를 받아서 결과 template html
# 을 이용해서 결과파일을 만들어 내는 일.
def index(request):
    # database에서 투표질문의 목록을 가져올 거예요!
    # 원래는 문자열로 표현되야 하는데 .. ORM을 사용하다 보니 .. 각 레코드가
    # Question 클래스의 객체로 표현.
    my_list = Question.objects.all().order_by('-pub_date')
    context = {'question_list':my_list}
    return render(request, 'index.html', context)

def detail(request, aaa):
    tmp = get_object_or_404(Question, pk=aaa)
    context = {"question":tmp}
    return render(request, 'detail.html', context)

def vote(request, bbb):
    # URL로 넘어온 데이터(bbb)는 Question 객체의 id가 넘어왔어요!
    question = get_object_or_404(Question, pk=bbb)
    # request header 안에 form에서 선택한 데이터가 포함되서 전달되고
    # 이것을 추출하기 위해서 request.POST["choice"]를 사용

    selected_choice = question.choice_set.get(pk=request.POST["choice"])

    selected_choice.votes += 1
    selected_choice.save()

    # result.html에서 현재 투표항목에 대한 각 항목들의 투표현황을 출력!!
    context = {'question':question}
    return render(request, 'result.html', context)