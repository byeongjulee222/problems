from django.shortcuts import render

# Create your views here.
def push(request):
    return render(request, 'pages/push.html')


def pull(request):
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'pages/pull.html', context)