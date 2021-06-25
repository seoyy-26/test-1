from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from django.utils import timezone
# Create your views here.

def showquestion(requesst):
    questions = Question.objects.all()
    return render(requesst, 'question/question.html',{'questions':questions})

def question_detail(request,id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'question/question_detail.html',{'question':question})

def question_new(request):
    return render(request, 'question/question_new.html')

def question_create(request):
    new_question=Question()
    new_question.title = request.GET['title']
    new_question.category = request.GET['category']
    new_question.writer = request.user
    new_question.pub_date = timezone.now()
    new_question.body = request.GET['body']
    new_question.save()
    return redirect('question:question_detail', new_question.id)

def question_edit(request, id):
    edit_question = Question.objects.get(id=id)
    return render(request,'question/question_edit.html', {'question': edit_question})

def question_update(request, id):
    update_question=Question()
    update_question.title = request.POST['title']
    update_question.category = request.POST['category']
    update_question.writer = request.user
    update_question.pub_date = timezone.now()
    update_question.body = request.POST['body']
    update_question.save()
    return redirect('question:question_detail', update_question.id)

def question_delete(request, id):
    delete_question = Question.objects.get(id=id)
    delete_question.delete()
    return redirect('question:showquestion')


#동아리별 연결
def 극예술연구회(request):
    questions = Question.objects.filter(category='극예술연구회')
    return render(request, 'question/공연분과/극예술연구회.html',{'questions':questions})

def 로터스(request):
    questions = Question.objects.filter(category='로터스')
    return render(request, 'question/공연분과/로터스.html',{'questions':questions})

def 뭉게구름(request):
    questions = Question.objects.filter(category='뭉게구름')
    return render(request, 'question/공연분과/뭉게구름.html',{'questions':questions})

def 아리랑(request):
    questions = Question.objects.filter(category='아리랑')
    return render(request, 'question/공연분과/아리랑.html',{'questions':questions})

def 음샘(request):
    questions = Question.objects.filter(category='음샘')
    return render(request, 'question/공연분과/음샘.html',{'questions':questions})

def 피어리스던(request):
    questions = Question.objects.filter(category='피어리스던')
    return render(request, 'question/공연분과/피어리스던.html',{'questions':questions})

def 현여울(request):
    questions = Question.objects.filter(category='현여울')
    return render(request, 'question/공연분과/현여울.html',{'questions':questions})

def AJAX(request):
    questions = Question.objects.filter(category='AJAX')
    return render(request, 'question/공연분과/AJAX.html',{'questions':questions})

def HOLA(request):
    questions = Question.objects.filter(category='HOLA')
    return render(request, 'question/공연분과/HOLA.html',{'questions':questions})

def ODC(request):
    questions = Question.objects.filter(category='ODC')
    return render(request, 'question/공연분과/ODC.html',{'questions':questions})

def OPUS(request):
    questions = Question.objects.filter(category='OPUS')
    return render(request, 'question/공연분과/OPUS.html',{'questions':questions})

def 길(request):
    questions = Question.objects.filter(category='길')
    return render(request, 'question/봉사분과/길.html',{'questions':questions})

def 손짓사랑회(request):
    questions = Question.objects.filter(category='손짓사랑회')
    return render(request, 'question/봉사분과/손짓사랑회.html',{'questions':questions})

def 젊은새이웃(request):
    questions = Question.objects.filter(category='젊은새이웃')
    return render(request, 'question/봉사분과/젊은새이웃.html',{'questions':questions})

def 페인터즈(request):
    questions = Question.objects.filter(category='페인터즈')
    return render(request, 'question/봉사분과/페인터즈.html',{'questions':questions})

def 푸름누리(request):
    questions = Question.objects.filter(category='푸름누리')
    return render(request, 'question/봉사분과/푸름누리.html',{'questions':questions})

def 한글학교하람(request):
    questions = Question.objects.filter(category='한글학교하람')
    return render(request, 'question/봉사분과/한글학교하람.html',{'questions':questions})

def ELF(request):
    questions = Question.objects.filter(category='ELF')
    return render(request, 'question/봉사분과/E.L.F.html',{'questions':questions})

def RCY(request):
    questions = Question.objects.filter(category='RCY')
    return render(request, 'question/봉사분과/RCY.html',{'questions':questions})

def 동국불교학생회(request):
    questions = Question.objects.filter(category='동국불교학생회')
    return render(request, 'question/사회분과/동국불교학생회.html',{'questions':questions})

def 프론티어(request):
    questions = Question.objects.filter(category='프론티어')
    return render(request, 'question/사회분과/프론티어.html',{'questions':questions})

def KUSA(request):
    questions = Question.objects.filter(category='KUSA')
    return render(request, 'question/사회분과/KUSA.html',{'questions':questions})

def RICH(request):
    questions = Question.objects.filter(category='RICH')
    return render(request, 'question/사회분과/RICH.html',{'questions':questions})

def UNSA(request):
    questions = Question.objects.filter(category='UNSA')
    return render(request, 'question/사회분과/UNSA.html',{'questions':questions})

def 두둠칫(request):
    questions = Question.objects.filter(category='두둠칫')
    return render(request, 'question/신규분과/두둠칫.html',{'questions':questions})

def 멋쟁이사자처럼(request):
    questions = Question.objects.filter(category='멋쟁이사자처럼')
    return render(request, 'question/신규분과/멋쟁이사자처럼.html',{'questions':questions})

def 인액터스(request):
    questions = Question.objects.filter(category='인액터스')
    return render(request, 'question/신규분과/인액터스.html',{'questions':questions})

def 잼잼(request):
    questions = Question.objects.filter(category='잼잼')
    return render(request, 'question/신규분과/잼잼.html',{'questions':questions})

def FC엘레펜테(request):
    questions = Question.objects.filter(category='FC엘레펜테')
    return render(request, 'question/신규분과/FC엘레펜테.html',{'questions':questions})

def QUD(request):
    questions = Question.objects.filter(category='QUD')
    return render(request, 'question/신규분과/QUD.html',{'questions':questions})

def 경영학연구회(request):
    questions = Question.objects.filter(category='경영학연구회')
    return render(request, 'question/연구분과/경영학연구회.html',{'questions':questions})

def 경제학연구회(request):
    questions = Question.objects.filter(category='경제학연구회')
    return render(request, 'question/연구분과/경제학연구회.html',{'questions':questions})

def 국제통상연구회(request):
    questions = Question.objects.filter(category='국제통상연구회')
    return render(request, 'question/연구분과/국제통상연구회.html',{'questions':questions})

def 정치학연구회(request):
    questions = Question.objects.filter(category='정치학연구회')
    return render(request, 'question/연구분과/정치학연구회.html',{'questions':questions})

def 그리고그림(request):
    questions = Question.objects.filter(category='그리고그림')
    return render(request, 'question/예창분과/그리고그림.html',{'questions':questions})

def 동국문학회(request):
    questions = Question.objects.filter(category='동국문학회')
    return render(request, 'question/예창분과/동국문학회.html',{'questions':questions})

def 동국서도회(request):
    questions = Question.objects.filter(category='동국서도회')
    return render(request, 'question/예창분과/동국서도회.html',{'reviews':questions})

def 동그라미(request):
    questions = Question.objects.filter(category='동그라미')
    return render(request, 'question/예창분과/동그라미.html',{'reviews':questions})

def 디딤돌(request):
    questions = Question.objects.filter(category='디딤돌')
    return render(request, 'question/예창분과/디딤돌.html',{'reviews':questions})

def 만화얼(request):
    questions = Question.objects.filter(category='만화얼')
    return render(request, 'question/예창분과/만화얼.html',{'reviews':questions})

def 애드러쉬(request):
    questions = Question.objects.filter(category='애드러쉬')
    return render(request, 'question/예창분과/애드러쉬.html',{'reviews':questions})

def 기우회(request):
    questions = Question.objects.filter(category='기우회')
    return render(request, 'question/체육제1분과/기우회.html',{'reviews':questions})

def 명궁(request):
    questions = Question.objects.filter(category='명궁')
    return render(request, 'question/체육제1분과/명궁.html',{'reviews':questions})

def 선무부(request):
    questions = Question.objects.filter(category='선무부')
    return render(request, 'question/체육제1분과/선무부.html',{'reviews':questions})

def 터스커스(request):
    questions = Question.objects.filter(category='터스커스')
    return render(request, 'question/체육제1분과/터스커스.html',{'reviews':questions})

def COURTIST(request):
    questions = Question.objects.filter(category='COURTIST')
    return render(request, 'question/체육제1분과/COURTIST.html',{'reviews':questions})

def DUTC(request):
    questions = Question.objects.filter(category='DUTC')
    return render(request, 'question/체육제1분과/DUTC.html',{'reviews':questions})

def FC_TOTO(request):
    questions = Question.objects.filter(category='FC_TOTO')
    return render(request, 'question/체육제1분과/FC_TOTO.html',{'reviews':questions})

def LAE(request):
    questions = Question.objects.filter(category='LAE')
    return render(request, 'question/체육제1분과/L.A.E.html',{'reviews':questions})

def 동국탐험연구회(request):
    questions = Question.objects.filter(category='동국탐험연구회')
    return render(request, 'question/체육제2분과/동국탐험연구회.html',{'reviews':questions})

def 무법(request):
    questions = Question.objects.filter(category='무법')
    return render(request, 'question/체육제2분과/무법.html',{'reviews':questions})

def 바람소리(request):
    questions = Question.objects.filter(category='바람소리')
    return render(request, 'question/체육제2분과/바람소리.html',{'reviews':questions})

def 산악부(request):
    questions = Question.objects.filter(category='산악부')
    return render(request, 'question/체육제2분과/산악부.html',{'reviews':questions})

def 수중탐구연구회(request):
    questions = Question.objects.filter(category='수중탐구연구회')
    return render(request, 'question/체육제2분과/수중탐구연구회.html',{'reviews':questions})

def DUST(request):
    questions = Question.objects.filter(category='DUST')
    return render(request, 'question/체육제2분과/DUST.html',{'reviews':questions})         

def 맑스철학연구회(request):
    questions = Question.objects.filter(category='맑스철학연구회')
    return render(request, 'question/학술분과/맑스철학연구회.html',{'reviews':questions})

def CAFE_IN(request):
    questions = Question.objects.filter(category='CAFE_IN')
    return render(request, 'question/학술분과/CAFE_IN.html',{'reviews':questions})

def DNA(request):
    questions = Question.objects.filter(category='DNA')
    return render(request, 'question/학술분과/DNA.html',{'reviews':questions})

def DUSSA(request):
    questions = Question.objects.filter(category='DUSSA')
    return render(request, 'question/학술분과/DUSSA.html',{'questions':questions})

def KCC(request):
    questions = Question.objects.filter(category='KCC')
    return render(request, 'question/학술분과/KCC.html',{'questions':questions})

def MECS(request):
    questions = Question.objects.filter(category='MECS')
    return render(request, 'question/학술분과/MECS.html',{'questions':questions})

def NSA(request):
    questions = Question.objects.filter(category='NSA')
    return render(request, 'question/학술분과/NSA.html',{'questions':questions})
