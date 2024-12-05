from main_utils import create_error_response, create_success_response
import functools

def authorize(permissions):
    def decorator_method(view_func):
      """
      Decorator method to authorize the user.
      It will check whether a user has given permissions or not
      """
      @functools.wraps(view_func)
      def wrapper(request, *args, **kwargs):
        for permission in permissions:
           if permission not in request.permissions:
              response = create_error_response("UNAUTHORIZED !")
              return response
        return view_func(request,*args, **kwargs)

      return wrapper
    return decorator_method