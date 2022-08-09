from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import JsonResponse
from .forms import ContactModelForm

# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html')


class ContactView(generic.View):
    template_name = "index.html"
    context = {}
    data = {}
    
    def post(self, request, *args, **kwargs):
        form = ContactModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            self.data['response'] = "OK"
            return JsonResponse(self.data, status=200)
        else:
            self.data['response'] = "error"
            return JsonResponse(self.data, status=400)
