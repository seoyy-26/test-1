from django.http import request
from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def index(request):
    return render(request, 'main/index.html')

def left_sidebar(request):
    return render(request, 'main/left_sidebar.html')

def no_sidebar(request):
    return render(request, 'main/no_sidebar.html')

def right_sidebar(request):
    return render(request, 'main/right_sidebar.html')

def 극예술연구회(request):
    return render(request, 'main/공연분과/극예술연구회.html')

def 로터스(request):
    return render(request, 'main/공연분과/로터스.html')

def 뭉게구름(request):
    return render(request, 'main/공연분과/뭉게구름.html')

def 아리랑(request):
    return render(request, 'main/공연분과/아리랑.html')

def 음샘(request):
    return render(request, 'main/공연분과/음샘.html')

def 피어리스던(request):
    return render(request, 'main/공연분과/피어리스던.html')

def 현여울(request):
    return render(request, 'main/공연분과/현여울.html')

def AJAX(request):
    return render(request, 'main/공연분과/AJAX.html')

def HOLA(request):
    return render(request, 'main/공연분과/HOLA.html')

def ODC(request):
    return render(request, 'main/공연분과/ODC.html')

def OPUS(request):
    return render(request, 'main/공연분과/OPUS.html')

def 길(request):
    return render(request, 'main/봉사분과/길.html')

def 손짓사랑회(request):
    return render(request, 'main/봉사분과/손짓사랑회.html')

def 젊은새이웃(request):
    return render(request, 'main/봉사분과/젊은새이웃.html')

def 페인터즈(request):
    return render(request, 'main/봉사분과/페인터즈.html')

def 푸름누리(request):
    return render(request, 'main/봉사분과/푸름누리.html')

def 한글학교하람(request):
    return render(request, 'main/봉사분과/한글학교하람.html')

def ELF(request):
    return render(request, 'main/봉사분과/E.L.F.html')

def RCY(request):
    return render(request, 'main/봉사분과/RCY.html')

def 동국불교학생회(request):
    return render(request, 'main/사회분과/동국불교학생회.html')

def 프론티어(request):
    return render(request, 'main/사회분과/프론티어.html')

def KUSA(request):
    return render(request, 'main/사회분과/KUSA.html')

def RICH(request):
    return render(request, 'main/사회분과/RICH.html')

def UNSA(request):
    return render(request, 'main/사회분과/UNSA.html')

def 두둠칫(request):
    return render(request, 'main/신규분과/두둠칫.html')

def 멋쟁이사자처럼(request):
    return render(request, 'main/신규분과/멋쟁이사자처럼.html')

def 인액터스(request):
    return render(request, 'main/신규분과/인액터스.html')

def 잼잼(request):
    return render(request, 'main/신규분과/잼잼.html')

def FC엘레펜테(request):
    return render(request, 'main/신규분과/FC엘레펜테.html')

def QUD(request):
    return render(request, 'main/신규분과/QUD.html')

def 경영학연구회(request):
    return render(request, 'main/연구분과/경영학연구회.html')

def 경제학연구회(request):
    return render(request, 'main/연구분과/경제학연구회.html')

def 국제통상연구회(request):
    return render(request, 'main/연구분과/국제통상연구회.html')

def 정치학연구회(request):
    return render(request, 'main/연구분과/정치학연구회.html')

def 그리고그림(request):
    return render(request, 'main/예창분과/그리고그림.html')

def 동국문학회(request):
    return render(request, 'main/예창분과/동국문학회.html')

def 동국서도회(request):
    return render(request, 'main/예창분과/동국서도회.html')

def 동그라미(request):
    return render(request, 'main/예창분과/동그라미.html')

def 디딤돌(request):
    return render(request, 'main/예창분과/디딤돌.html')

def 만화얼(request):
    return render(request, 'main/예창분과/만화얼.html')

def 애드러쉬(request):
    return render(request, 'main/예창분과/애드러쉬.html')

def 기우회(request):
    return render(request, 'main/체육제1분과/기우회.html')

def 명궁(request):
    return render(request, 'main/체육제1분과/명궁.html')

def 선무부(request):
    return render(request, 'main/체육제1분과/선무부.html')

def 터스커스(request):
    return render(request, 'main/체육제1분과/터스커스.html')

def COURTIST(request):
    return render(request, 'main/체육제1분과/COURTIST.html')

def DUTC(request):
    return render(request, 'main/체육제1분과/DUTC.html')

def FC_TOTO(request):
    return render(request, 'main/체육제1분과/FC_TOTO.html')

def LAE(request):
    return render(request, 'main/체육제1분과/L.A.E.html')

def 동국탐험연구회(request):
    return render(request, 'main/체육제2분과/동국탐험연구회.html')

def 무법(request):
    return render(request, 'main/체육제2분과/무법.html')

def 바람소리(request):
    return render(request, 'main/체육제2분과/바람소리.html')

def 산악부(request):
    return render(request, 'main/체육제2분과/산악부.html')

def 수중탐구연구회(request):
    return render(request, 'main/체육제2분과/수중탐구연구회.html')

def DUST(request):
    return render(request, 'main/체육제2분과/DUST.html')         

def 맑스철학연구회(request):
    return render(request, 'main/학술분과/맑스철학연구회.html')

def CAFE_IN(request):
    return render(request, 'main/학술분과/CAFE_IN.html')

def DNA(request):
    return render(request, 'main/학술분과/DNA.html')

def DUSSA(request):
    return render(request, 'main/학술분과/DUSSA.html')

def KCC(request):
    return render(request, 'main/학술분과/KCC.html')

def MECS(request):
    return render(request, 'main/학술분과/MECS.html')

def NSA(request):
    return render(request, 'main/학술분과/NSA.html')                 
