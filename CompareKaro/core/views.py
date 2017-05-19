from django.shortcuts import render

# Create your views here.
def home(request):
   context = {'request': request, 'user': request.user}
   return render(request, 'core/index.html',context)
