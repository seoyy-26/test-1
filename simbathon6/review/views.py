from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.utils import timezone
# Create your views here.

def showreview(requesst):
    reviews = Review.objects.all()
    return render(requesst, 'review/review.html',{'reviews':reviews})

def review_detail(request,id):
    review = get_object_or_404(Review, pk=id)
    return render(request, 'review/review_detail.html',{'review':review})

def review_new(request):
    return render(request, 'review/review_new.html')

def review_create(request):
    new_review=Review()
    new_review.title = request.POST['title']
    new_review.category = request.POST['category']
    new_review.writer = request.user
    new_review.pub_date = timezone.now()
    new_review.body = request.POST['body']
    new_review.활동시기 = request.POST['활동시기']
    new_review.추천의사 = request.POST['추천의사']
    new_review.save()
    return redirect('review:review_detail', new_review.id)

def review_edit(request, id):
    edit_review = Review.objects.get(id=id)
    return render(request,'review/review_edit.html', {'review': edit_review})

def review_update(request, id):
    update_review=Review()
    update_review.title = request.POST['title']
    update_review.category = request.POST['category']
    update_review.writer = request.user
    update_review.pub_date = timezone.now()
    update_review.body = request.POST['body']
    update_review.활동시기 = request.POST['활동시기']
    update_review.추천의사 = request.POST['추천의사']
    update_review.save()
    return redirect('review:review_detail', update_review.id)

def review_delete(request, id):
    delete_review = Review.objects.get(id=id)
    delete_review.delete()
    return redirect('review:showreview')


#동아리별 연결
def 극예술연구회(request):
    reviews = Review.objects.filter(category='극예술연구회')
    return render(request, 'review/공연분과/극예술연구회.html',{'reviews':reviews})

def 로터스(request):
    reviews = Review.objects.filter(category='로터스')
    return render(request, 'review/공연분과/로터스.html',{'reviews':reviews})

def 뭉게구름(request):
    reviews = Review.objects.filter(category='뭉게구름')
    return render(request, 'review/공연분과/뭉게구름.html',{'reviews':reviews})

def 아리랑(request):
    reviews = Review.objects.filter(category='아리랑')
    return render(request, 'review/공연분과/아리랑.html',{'reviews':reviews})

def 음샘(request):
    reviews = Review.objects.filter(category='음샘')
    return render(request, 'review/공연분과/음샘.html',{'reviews':reviews})

def 피어리스던(request):
    reviews = Review.objects.filter(category='피어리스던')
    return render(request, 'review/공연분과/피어리스던.html',{'reviews':reviews})

def 현여울(request):
    reviews = Review.objects.filter(category='현여울')
    return render(request, 'review/공연분과/현여울.html',{'reviews':reviews})

def AJAX(request):
    reviews = Review.objects.filter(category='AJAX')
    return render(request, 'review/공연분과/AJAX.html',{'reviews':reviews})

def HOLA(request):
    reviews = Review.objects.filter(category='HOLA')
    return render(request, 'review/공연분과/HOLA.html',{'reviews':reviews})

def ODC(request):
    reviews = Review.objects.filter(category='ODC')
    return render(request, 'review/공연분과/ODC.html',{'reviews':reviews})

def OPUS(request):
    reviews = Review.objects.filter(category='OPUS')
    return render(request, 'review/공연분과/OPUS.html',{'reviews':reviews})

def 길(request):
    reviews = Review.objects.filter(category='길')
    return render(request, 'review/봉사분과/길.html',{'reviews':reviews})

def 손짓사랑회(request):
    reviews = Review.objects.filter(category='손짓사랑회')
    return render(request, 'review/봉사분과/손짓사랑회.html',{'reviews':reviews})

def 젊은새이웃(request):
    reviews = Review.objects.filter(category='젊은새이웃')
    return render(request, 'review/봉사분과/젊은새이웃.html',{'reviews':reviews})

def 페인터즈(request):
    reviews = Review.objects.filter(category='페인터즈')
    return render(request, 'review/봉사분과/페인터즈.html',{'reviews':reviews})

def 푸름누리(request):
    reviews = Review.objects.filter(category='푸름누리')
    return render(request, 'review/봉사분과/푸름누리.html',{'reviews':reviews})

def 한글학교하람(request):
    reviews = Review.objects.filter(category='한글학교하람')
    return render(request, 'review/봉사분과/한글학교하람.html',{'reviews':reviews})

def ELF(request):
    reviews = Review.objects.filter(category='ELF')
    return render(request, 'review/봉사분과/E.L.F.html',{'reviews':reviews})

def RCY(request):
    reviews = Review.objects.filter(category='RCY')
    return render(request, 'review/봉사분과/RCY.html',{'reviews':reviews})

def 동국불교학생회(request):
    reviews = Review.objects.filter(category='동국불교학생회')
    return render(request, 'review/사회분과/동국불교학생회.html',{'reviews':reviews})

def 프론티어(request):
    reviews = Review.objects.filter(category='프론티어')
    return render(request, 'review/사회분과/프론티어.html',{'reviews':reviews})

def KUSA(request):
    reviews = Review.objects.filter(category='KUSA')
    return render(request, 'review/사회분과/KUSA.html',{'reviews':reviews})

def RICH(request):
    reviews = Review.objects.filter(category='RICH')
    return render(request, 'review/사회분과/RICH.html',{'reviews':reviews})

def UNSA(request):
    reviews = Review.objects.filter(category='UNSA')
    return render(request, 'review/사회분과/UNSA.html',{'reviews':reviews})

def 두둠칫(request):
    reviews = Review.objects.filter(category='두둠칫')
    return render(request, 'review/신규분과/두둠칫.html',{'reviews':reviews})

def 멋쟁이사자처럼(request):
    reviews = Review.objects.filter(category='멋쟁이사자처럼')
    return render(request, 'review/신규분과/멋쟁이사자처럼.html',{'reviews':reviews})

def 인액터스(request):
    reviews = Review.objects.filter(category='인액터스')
    return render(request, 'review/신규분과/인액터스.html',{'reviews':reviews})

def 잼잼(request):
    reviews = Review.objects.filter(category='잼잼')
    return render(request, 'review/신규분과/잼잼.html',{'reviews':reviews})

def FC엘레펜테(request):
    reviews = Review.objects.filter(category='FC엘레펜테')
    return render(request, 'review/신규분과/FC엘레펜테.html',{'reviews':reviews})

def QUD(request):
    reviews = Review.objects.filter(category='QUD')
    return render(request, 'review/신규분과/QUD.html',{'reviews':reviews})

def 경영학연구회(request):
    reviews = Review.objects.filter(category='경영학연구회')
    return render(request, 'review/연구분과/경영학연구회.html',{'reviews':reviews})

def 경제학연구회(request):
    reviews = Review.objects.filter(category='경제학연구회')
    return render(request, 'review/연구분과/경제학연구회.html',{'reviews':reviews})

def 국제통상연구회(request):
    reviews = Review.objects.filter(category='국제통상연구회')
    return render(request, 'review/연구분과/국제통상연구회.html',{'reviews':reviews})

def 정치학연구회(request):
    reviews = Review.objects.filter(category='정치학연구회')
    return render(request, 'review/연구분과/정치학연구회.html',{'reviews':reviews})

def 그리고그림(request):
    reviews = Review.objects.filter(category='그리고그림')
    return render(request, 'review/예창분과/그리고그림.html',{'reviews':reviews})

def 동국문학회(request):
    reviews = Review.objects.filter(category='동국문학회')
    return render(request, 'review/예창분과/동국문학회.html',{'reviews':reviews})

def 동국서도회(request):
    reviews = Review.objects.filter(category='동국서도회')
    return render(request, 'review/예창분과/동국서도회.html',{'reviews':reviews})

def 동그라미(request):
    reviews = Review.objects.filter(category='동그라미')
    return render(request, 'review/예창분과/동그라미.html',{'reviews':reviews})

def 디딤돌(request):
    reviews = Review.objects.filter(category='디딤돌')
    return render(request, 'review/예창분과/디딤돌.html',{'reviews':reviews})

def 만화얼(request):
    reviews = Review.objects.filter(category='만화얼')
    return render(request, 'review/예창분과/만화얼.html',{'reviews':reviews})

def 애드러쉬(request):
    reviews = Review.objects.filter(category='애드러쉬')
    return render(request, 'review/예창분과/애드러쉬.html',{'reviews':reviews})

def 기우회(request):
    reviews = Review.objects.filter(category='기우회')
    return render(request, 'review/체육제1분과/기우회.html',{'reviews':reviews})

def 명궁(request):
    reviews = Review.objects.filter(category='명궁')
    return render(request, 'review/체육제1분과/명궁.html',{'reviews':reviews})

def 선무부(request):
    reviews = Review.objects.filter(category='선무부')
    return render(request, 'review/체육제1분과/선무부.html',{'reviews':reviews})

def 터스커스(request):
    reviews = Review.objects.filter(category='터스커스')
    return render(request, 'review/체육제1분과/터스커스.html',{'reviews':reviews})

def COURTIST(request):
    reviews = Review.objects.filter(category='COURTIST')
    return render(request, 'review/체육제1분과/COURTIST.html',{'reviews':reviews})

def DUTC(request):
    reviews = Review.objects.filter(category='DUTC')
    return render(request, 'review/체육제1분과/DUTC.html',{'reviews':reviews})

def FC_TOTO(request):
    reviews = Review.objects.filter(category='FC_TOTO')
    return render(request, 'review/체육제1분과/FC_TOTO.html',{'reviews':reviews})

def LAE(request):
    reviews = Review.objects.filter(category='LAE')
    return render(request, 'review/체육제1분과/L.A.E.html',{'reviews':reviews})

def 동국탐험연구회(request):
    reviews = Review.objects.filter(category='동국탐험연구회')
    return render(request, 'review/체육제2분과/동국탐험연구회.html',{'reviews':reviews})

def 무법(request):
    reviews = Review.objects.filter(category='무법')
    return render(request, 'review/체육제2분과/무법.html',{'reviews':reviews})

def 바람소리(request):
    reviews = Review.objects.filter(category='바람소리')
    return render(request, 'review/체육제2분과/바람소리.html',{'reviews':reviews})

def 산악부(request):
    reviews = Review.objects.filter(category='산악부')
    return render(request, 'review/체육제2분과/산악부.html',{'reviews':reviews})

def 수중탐구연구회(request):
    reviews = Review.objects.filter(category='수중탐구연구회')
    return render(request, 'review/체육제2분과/수중탐구연구회.html',{'reviews':reviews})

def DUST(request):
    reviews = Review.objects.filter(category='DUST')
    return render(request, 'review/체육제2분과/DUST.html',{'reviews':reviews})         

def 맑스철학연구회(request):
    reviews = Review.objects.filter(category='맑스철학연구회')
    return render(request, 'review/학술분과/맑스철학연구회.html',{'reviews':reviews})

def CAFE_IN(request):
    reviews = Review.objects.filter(category='CAFE_IN')
    return render(request, 'review/학술분과/CAFE_IN.html',{'reviews':reviews})

def DNA(request):
    reviews = Review.objects.filter(category='DNA')
    return render(request, 'review/학술분과/DNA.html',{'reviews':reviews})

def DUSSA(request):
    reviews = Review.objects.filter(category='DUSSA')
    return render(request, 'review/학술분과/DUSSA.html',{'reviews':reviews})

def KCC(request):
    reviews = Review.objects.filter(category='KCC')
    return render(request, 'review/학술분과/KCC.html',{'reviews':reviews})

def MECS(request):
    reviews = Review.objects.filter(category='MECS')
    return render(request, 'review/학술분과/MECS.html',{'reviews':reviews})

def NSA(request):
    reviews = Review.objects.filter(category='NSA')
    return render(request, 'review/학술분과/NSA.html',{'reviews':reviews})
