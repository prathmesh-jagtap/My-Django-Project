from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.
openai_api_key = "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"
openai.api_key = openai_api_key


def ask_openai(message):
    reponse = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7
    )
    answer = reponse.choices[0].text.strip()


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)
        return JsonResponse({"message": message, "response": response})
    return render(request, "chatbot.html")
