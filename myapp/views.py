from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class BaseView(View):
    template_name = None

    def get(self, request):
        return render(request, self.template_name, {})

class IndexView(BaseView):
    template_name = 'myapp/index.html'

class AboutView(BaseView):
    template_name = 'myapp/about.html'

class ContactView(BaseView):
    template_name = 'myapp/contact.html'

class FeaturesView(LoginRequiredMixin, BaseView):
    template_name = 'myapp/features.html'
