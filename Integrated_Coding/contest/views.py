from django.shortcuts import render,HttpResponse
from .models import Contest
from .tasks import scrape_website


def home(request):
    contest = Contest.objects.all()
    return render(request,'contest/contest.html',{'contest':contest})

def test(request):
    scrape_website.delay()
    return HttpResponse("done")
