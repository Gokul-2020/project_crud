# from django.core.cache import cache
from django.conf import settings
# from django.contrib.auth.models import User
# from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.decorators import login_required
import re
import time
from django.shortcuts import redirect
from django.utils import timezone


class RequireLoginMiddleware(object):

    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response

        self.required = tuple(re.compile(url)
                              for url in settings.LOGIN_REQUIRED_URLS)
        self.exceptions = tuple(re.compile(url)
                                for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS)

    def __call__(self, request):

        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        # An exception match should immediately return None
        for url in self.exceptions:
            if url.match(request.path):
                return None

        # Requests matching a restricted URL pattern are returned
        # wrapped with the login_required decorator
        for url in self.required:
            if url.match(request.path):
                return login_required(view_func)(request, *view_args, **view_kwargs)

        # Explicitly return None for all non-matching requests
        return None
