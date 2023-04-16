from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import ContestQuestion
from django.views.decorators.csrf import csrf_exempt

def courses(request):
    questions = ContestQuestion.objects.all()
    if request.GET:
        difficulty=request.GET.get('difficulty')
        topic=request.GET.get('topic')
    else:
        difficulty=topic='all'
    return render(request,'courses/courses.html',{ 'questions':questions,'difficulty': difficulty, 'topic': topic })

@csrf_exempt
def question_status_update(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        is_done = request.POST.get('is_done')
        item = ContestQuestion.objects.get(pk=pk)
        item.is_done= is_done
        item.save()
        return JsonResponse({'success': True, 'is_done': item.is_done}, status=200)
    else:
        return JsonResponse({'success': False, 'errors': []}, status=400)
    
