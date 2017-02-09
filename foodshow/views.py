from django.shortcuts import render_to_response
from django.http import HttpResponse
from foodshow.models import Message
from django.template import RequestContext
from foodshow.forms import MessageForm
from django.utils import timezone
from django.shortcuts import render_to_response, redirect

# Create your views here.


def index(request):
  friends = ['about', 'news', 'food', 'location', 'contact']
  return render_to_response('index.html', {'friends':friends})

def about(request):
  return render_to_response('about.html')

def news(request):
        messages = Message.objects.all()
        response_string = "<a href='/about'>us</a>"
        response_string += "<a href='/post'>post</a><br/>"
        response_string += '<br/>'.join(["user: %s, subject: %s, time: %s" % (q.user, q.subject, q.publication_date) for q in messages])
        return HttpResponse(response_string)
      
#def news(request):
#  return render_to_response('news.html')

def post(request):
        if request.method == 'POST':
                form = MessageForm(request.POST)
                if form.is_valid():
                        message = Message(user=form.cleaned_data['user'],subject=form.cleaned_data['subject'], publication_date=timezone.now())
                        message.save()
                        return redirect('/news')
        else:
                form = MessageForm()
        return render_to_response('news.html',{'form': form}, context_instance=RequestContext(request))

      
      
def food(request):
  return render_to_response('food.html')


def location(request):
  return render_to_response('location.html')


def contact(request):
  return render_to_response('contact.html')


