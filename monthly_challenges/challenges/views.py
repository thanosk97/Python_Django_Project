from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january" : "Eat no meat for the entire month!",
    "february" : "Walk for 20 minutes every day!",
    "march" : "Learn django for 20 minutes per day",
    "april" : "Eat no meat for the entire month!",
    "may" : "Walk for 20 minutes every day!",
    "june" : "Learn django for 20 minutes per day",
    "july" : "Eat no meat for the entire month!",
    "august" : "Walk for 20 minutes every day!",
    "september" : "Learn django for 20 minutes per day",
    "october" : "Eat no meat for the entire month!",
    "november" : "Walk for 20 minutes every day!",
    "december" : "Learn django for 20 minutes per day"
}


# Create your views here.

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported yet!")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
