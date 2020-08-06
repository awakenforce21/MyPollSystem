from django.db import models

class Question(models.Model):
    # 자동으로 생성되는 id는 PK, 1씩 자동증가(autoincrement)
    # id = models.IntegerField()
    question_text = models.CharField('투표질문제목', max_length = 200)
    pub_date = models.DateTimeField('투표생성날짜')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField('투표보기문구', max_length = 30)
    votes = models.IntegerField('투표수', default = 0)

    def __str__(self):
        return self.choice_text