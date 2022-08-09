from django.shortcuts import render, redirect
from . forms import SubscribersForm
from django.contrib import messages
from .forms import SubscribersForm
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import JsonResponse


# Create your views here.

@csrf_exempt
def bases(request):
  if request.method == 'POST':
    print("Request post")
    form = SubscribersForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Souscription réussi!')
      return redirect('/')
  else:
    form = SubscribersForm()
  context = {'form':form}
  template = "index.html"
  return render(request, template, context)


class NewslettersView(generic.View):
    data = {}
    def get(self, request, *args, **kwargs):        
        return JsonResponse(self.data)

    def post(self, request, *args, **kwargs):
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            self.data['response'] = "OK"
            return JsonResponse(self.data, status=200)
        else:
            self.data['response'] = "error"
            return JsonResponse(self.data, status=400)

