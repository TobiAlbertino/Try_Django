from django.views.generic.base import TemplateView


# Inheritance dari Template response Mixin
# Context Mixin
# View
class indexView(TemplateView):
    pass

class ParameterView(TemplateView):
    template_name = 'parameter.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = kwargs
        context['judul'] = 'Home Parameter'
        context['penulis'] = 'ujang'
        return context

class ContextView(TemplateView):
    template_name = 'context.html'

    def get_context_data(self):
        context = {
            'judul' : 'Home Content',
            'penulis' : 'TobiAlbertino',
        }
        return context