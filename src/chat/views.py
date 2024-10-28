from django.shortcuts import render

# Create your views here.

def chat(request):
    return render(request, "chat/chat_main_view.html")