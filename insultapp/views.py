from django.http import HttpRequest, HttpResponse

from insultapp import insulter


def insult(request: HttpRequest) -> HttpResponse:
    insult_response: str = insulter.insult()
    return HttpResponse(insult_response, status=200)


def insult_name(request: HttpRequest, name: str) -> HttpResponse:
    insult_response: str = insulter.named_insult(name)
    return HttpResponse(insult_response, status=200)
