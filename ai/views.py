from django.shortcuts import render
from .helpers import make_request, build_ai_context
# Create your views here.

MESSAGES = []

import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatSession, AIUserSettings
from .forms import AISettingsForm

@login_required
def ai_settings(request):
    user = request.user
    settings, create = AIUserSettings.objects.get_or_create(user=user)
    
    if request.method == "POST":
        form = AISettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect("ai:settings")
    else:
        form = AISettingsForm(instance=settings)

    return render(request, "ai/settings.html", {"form": form})


@login_required
def startchat(request):
    user = request.user

    # Create a new chat session each time or customize this logic
    usersession, created = ChatSession.objects.get_or_create(
        user=user
    )
    if created:
      usersession.session_id = str(uuid.uuid4())
      usersession.save()
    if request.GET.get('start', False):
      print(usersession)
      return redirect('ai:chatinterface', session_id=usersession.session_id)
    return render(request, 'ai/chat.html')

@login_required
def chatinterface(request, session_id):
    context = {}
    usersession = get_object_or_404(ChatSession, session_id=session_id, user=request.user)
    context['usersession'] = usersession
    messages_obj = usersession.messages.all().order_by('timestamp')
    messages = list(messages_obj.values('role', 'content'))
    
    if request.method == "POST":
      userInput = request.POST.get('userinput')
      messages.append({'role': 'user', 'content': userInput})
      ai_context = build_ai_context(request.user)
      response = make_request(userInput, messages, ai_context)
      messages.append(response)
      usersession.messages.create(role='user', content=userInput)
      usersession.messages.create(role='assistant', content=response['message']['content'])
      context['message'] = response['message']
      
      if request.htmx:
        return render(request, 'ai/_message.html', context)
       
    context['messages'] = messages_obj
    if request.htmx:
      return render(request, 'ai/_messages.html', context)
    
    return render(request, 'ai/chat.html', context)
def interface(request):
  context = {}
  # get user info and choose ai role
  if request.method == "POST":
    userInput = request.POST.get('userinput')
    MESSAGES.append({'role': 'user', 'content': userInput})
    response = make_request(userInput, MESSAGES)
    MESSAGES.append(response)
    context['response'] = response['content']
  return render(request, 'ai/chat.html', context)