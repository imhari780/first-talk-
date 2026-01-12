from django.shortcuts import render


def mic_page(request):
    return render(request, "mic.html")
