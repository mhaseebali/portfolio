from django.shortcuts import render


# Create your views here.

# def req(request):
#     return render(request, 'home.html', {
#       "sometext": "challenge_text"
#     })

def req1(request):
    return render(request, 'myapp/base.html')

def req2(request):
    return render(request, 'myapp/designs.html')




      