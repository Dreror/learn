from django.shortcuts import render, redirect
from .models import Info
from .forms import InfoForm
from django.views.generic import DetailView, UpdateView, DeleteView


def new_2_home(request):
    news = Info.objects.order_by("-date")
    return render(request, "new_2/new_2_home.html", {"news": news})


class NewsDetailNews(DetailView):
    model = Info
    template_name = "new_2/detail_view.html"
    context_object_name = "article"


class NewsUpdateView(UpdateView):
    model = Info
    template_name = "new_2/create.html"

    form_class = InfoForm


class NewsDeleteView(DeleteView):
    model = Info
    success_url = "/new_2"
    template_name = "new_2/news-delete-views.html"


def create(request):
    error = ""
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Form is incorrect"

    form = InfoForm()

    data = {
        "form": form,
        "error": error
    }

    return render(request, "new_2/create.html", data)
