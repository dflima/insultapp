"""
Provides the controller logic for the insultapp.
"""

from django.http import HttpRequest, HttpResponse  # pylint: disable=import-error

from insultapp import insulter


def insult(_request: HttpRequest) -> HttpResponse:
    """
    Controller for the /insult endpoint.

    Parameters:
    request (HttpRequest): The HTTP Request

    Returns:
    HttpResponse: The HTTP Response with the insult
    """
    insult_response: str = insulter.insult()
    return HttpResponse(insult_response, status=200)


def insult_name(_request: HttpRequest, name: str) -> HttpResponse:
    """
    Controller for the /insult/<name> endpoint.

    Parameters:
    request (HttpRequest): The HTTP Request

    Returns:
    HttpResponse: The HTTP Response with the named insult
    """
    insult_response: str = insulter.named_insult(name)
    return HttpResponse(insult_response, status=200)
