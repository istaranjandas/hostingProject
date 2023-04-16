from django.shortcuts import render
from .models import LeaderBoard

def stat(request):
    return render(request,'coding_profile/stat.html')

def leaderboard(request):
    if request.POST:
        institute=request.POST.get('institute-name')
        print(institute)
    else:
        institute='all'
    leaderboard = LeaderBoard.objects.all()
    return render(request, 'coding_profile/leaderboard.html',{'leaderboard':leaderboard, 'institute':institute})
