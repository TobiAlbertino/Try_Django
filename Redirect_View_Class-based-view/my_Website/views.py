from django.views.generic.base import RedirectView, TemplateView

class HomeView(RedirectView):
    # url = '/'
    pattern_name = 'index'

class HomeUserView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        print(kwargs)
        if self.request.GET.__contains__('tipe'):
            kwargs['tipe'] = self.request.GET['tipe']

        print (kwargs)
        return super().get_context_data(**kwargs)

# inheritance hanya dari nase view
class HomeRedirectView(RedirectView):
    pattern_name='user'
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        if kwargs['user'] == 'pukis':
            print('merubah data')
            kwargs['user'] = 'tobi'
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)