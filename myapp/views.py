from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class BaseView(View):
    template_name = None

    def get(self, request):
        return render(request, self.template_name, {})

class IndexView(LoginRequiredMixin, BaseView):
    template_name = 'myapp/index.html'

class AboutView(BaseView):
    template_name = 'myapp/about.html'

class ContactView(BaseView):
    template_name = 'myapp/contact.html'

class FeaturesView(BaseView):
    template_name = 'myapp/features.html'

class CreateRoomView(LoginRequiredMixin, BaseView):
    template_name = 'myapp/video_call.html'
    def get(self, request):
        return render(request, self.template_name, {'name': request.user.first_name + " " + request.user.last_name})

class JoinRoomView(LoginRequiredMixin, BaseView):
    template_name = 'myapp/joinroom.html'
    def get(self, request):
        if request.method == "POST":
            roomID = request.POST['roomID']
            return HttpResponseRedirect("/meeting?roomID="+roomID,)
        return render(request, self.template_name, {'name': request.user.first_name + " " + request.user.last_name})