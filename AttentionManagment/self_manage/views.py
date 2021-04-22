from django.shortcuts import render

from self_manage.scheduling import Scheduling


def index(request):
    scheduling = Scheduling()

    scheduling.make_schedule()
    return render(request,"index.html",context={"key":"value"})
# Create your views here.
