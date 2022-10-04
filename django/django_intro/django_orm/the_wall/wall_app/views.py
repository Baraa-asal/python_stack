from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from log_reg_app.models import User
from wall_app.models import Message, Comment


def root(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'messages': Message.objects.all().order_by('-created_at'),
    }
    return render(request, 'wall.html', context)


def create_message(request):
    message = request.POST['message']
    message = Message.objects.create(
        message=message, user=User.objects.get(id=request.session['id']))
    return redirect('/wall')


def create_comment(request):
    comment = request.POST['comment']
    Comment.objects.create(comment=comment,
                           message=Message.objects.get(
                               id=request.POST['message_id']),
                           user=User.objects.get(id=request.session['id']))
    return redirect('/wall')


def delete_message(request):
    Message.objects.get(id=request.POST['message_id']).delete()
    return redirect('/wall')
