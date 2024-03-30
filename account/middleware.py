from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages


class AccountCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user  # Who is the current user ?
        
        if not user.is_authenticated:
            if request.path == reverse('accounts') or modulename == 'django.contrib.auth.views':
                pass
            elif modulename == 'apm_app.views' or modulename == 'administration.views':
                messages.error(
                    request, "You need to be logged in to perform this operation")
                return redirect(reverse('accounts'))
            
        
        