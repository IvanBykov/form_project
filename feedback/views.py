from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import FormView, CreateView, UpdateView

from django.views import View

class FeedBackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedBackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

#class FeedBackView(FormView):
#    form_class = FeedbackForm
#    template_name = 'feedback/feedback.html'
#    success_url = '/done'

#    def form_valid(self, form):
#        form.save()
#        return super(FeedBackView, self).form_valid(form)


#class FeedBackView(View):
#    def get(self, request):
#        form = FeedbackForm()
#        return render(request, 'feedback/feedback.html', context={'form': form})
#
#    def post(self, request):
#        form = FeedbackForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/done')
#        return render(request, 'feedback/feedback.html', context={'form': form})


class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        form = FeedbackForm(instance=Feedback.objects.get(id=id_feedback))
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        form = FeedbackForm(request.POST, instance=Feedback.objects.get(id=id_feedback))
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I.I.'
        context['date'] = '23.04.2022'
        return context

#class DetailFeedBack(TemplateView):
#    template_name = 'feedback/detail_feedback.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        feed = Feedback.objects.get(id=kwargs['id_feedback'])
#        context['feed'] = feed
#        return context

class DetailFeedBack(DeleteView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'feed'

# class ListFeedBack(TemplateView):
#    template_name = 'feedback/list_feedback.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        list_feed = Feedback.objects.all()
#        context['list_feed'] = list_feed
#        return context

class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        #queryset = super().get_queryset()
        #filter_qs = queryset.filter(rating__gt=3)
        #return super().get_queryset().filter(rating__gt=2)
        return super().get_queryset()


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'form': form})
