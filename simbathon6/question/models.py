from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    QUESTION_CATEGORY_CHOICES = [
        ('극예술연구회','극예술연구회'), 
        ('로터스','로터스'), 
        ('뭉게구름','뭉게구름'), 
        ('아리랑','아리랑'), 
        ('음샘','음샘'), 
        ('피어리스던','피어리스던'), 
        ('현여울','현여울'), 
        ('AJAX','AJAX'), 
        ('HOLA','HOLA'), 
        ('OCD','OCD'), 
        ('OPUS','OPUS'),

        ('길','길'), 
        ('손짓사랑회','손짓사랑회'), 
        ('젊은새이웃','젊은새이웃'), 
        ('페인터즈','페인터즈'), 
        ('푸름누리','푸름누리'), 
        ('한글학교하람','한글학교하람'), 
        ('ELF','ELF'), 
        ('RCY','RCY'),

        ('동국불교학생회','동국불교학생회'), 
        ('프론티어','프론티어'), 
        ('KUSA','KUSA'), 
        ('RICH','RICH'), 
        ('UNSA','UNSA'),

        ('두둠칫','두둠칫'), 
        ('멋쟁이사자처럼','멋쟁이사자처럼'), 
        ('인액터스','인액터스'), 
        ('잼잼','잼잼'), 
        ('FC엘레펜테','FC엘레펜테'), 
        ('QUD','QUD'),

        ('경영학연구회','경영학연구회'),
        ('경제학연구회','경제학연구회'),
        ('국제통상연구회','국제통상연구회'),
        ('정치학연구회','정치학연구회'),

        ('그리고그림','그리고그림'), 
        ('동국문학회','동국문학회'), 
        ('동국서도회','동국서도회'), 
        ('동그라미','동그라미'), 
        ('디딤돌','디딤돌'), 
        ('만화얼','만화얼'), 
        ('애드러쉬','애드러쉬'),

        ('기우회','기우회'), 
        ('명궁','명궁'), 
        ('선무부','선무부'), 
        ('터스커스','터스커스'), 
        ('COURTIST','COURTIST'), 
        ('DUTC','DUTC'), 
        ('FC_TOTO','FC_TOTO'), 
        ('LAE','LAE'),


        ('동국탐험연구회','동국탐험연구회'), 
        ('무법','무법'), 
        ('바람소리','바람소리'), 
        ('산악부','산악부'), 
        ('수중탐구연구회','수중탐구연구회'), 
        ('DUST','DUST'),


        ('맑스철학연구회','맑스철학연구회'), 
        ('CAFE_IN','CAFE_IN'), 
        ('DNA','DNA'), 
        ('DUSSA','DUSSA'), 
        ('KCC','KCC'), 
        ('MECS','MECS'), 
        ('NSA','NSA'),
    ]


    category = models.CharField(choices=QUESTION_CATEGORY_CHOICES, max_length=300)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    

    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:10] 

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
