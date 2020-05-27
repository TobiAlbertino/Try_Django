from django.shortcuts import render
from django.views import View

def index(request):
    context = {
        'heading' : 'Selamat Datang'
    }

    if request.method == 'POST':
        context['heading'] = 'Post Function based view'

    return render(request, 'index.html', context)

class IndexClassView(View):

    template_name = ''
    context = {
    }
    # override method get dari parrent class view
    def get(self, request):
        self.context['heading'] = 'Get Class based view'
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.context['heading'] = 'Post Class based view'
        return render(request, self.template_name, self.context)