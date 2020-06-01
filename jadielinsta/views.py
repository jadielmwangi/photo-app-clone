from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Post
from .forms import PostForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.



# @login_required(login_url='/accounts/register/')
def new_post(request):
    date = dt.date.today()
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data['caption']
            image = form.cleaned_data['Upload image']
            recipient = PostRecipients(caption = caption,image=image)
            recipient.save()
            send_welcome_email(caption,image)
            HttpResponseRedirect('newpost')
            print('valid')
    else:
        form = PostForm()
    return render(request, 'all-insta/post.html', {"date": date,'posts': posts,"postForm":form})




