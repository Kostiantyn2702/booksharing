from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from accounts.models import User


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    model = User
    success_url = reverse_lazy("index")
    fields = ("first_name", "last_name")

    def get_object(self, queryset=None):
        return self.request.user
