import jwt
from main_utils import create_success_response, create_error_response
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.conf import settings
from user.models import User


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_json_response(self, response: Response):
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()

        return response

    def send_unauthorized_response(self, message="UNAUTHORIZED"):
        response = create_error_response(message)
        response = self.get_json_response(response)
        return response


    def __call__(self, request):
        user_auth_only = False
        is_except = False
        department_exception = False
        try:

            exception_endpoints = ['/user/login', '/admin/',
                                   ]

            if request.path == '/':
                response = self.get_response(request)
                return response

            for endpoint in exception_endpoints:
                if request.path.startswith(endpoint):
                    is_except = True
                    break
        except Exception:
            return self.send_unauthorized_response()

        if not is_except:
            request.auth_user = {}
            auth = request.headers.get('Authorization')
            try:
                auth = auth[7:]
                user = jwt.decode(auth, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
                user = user.get('user')
                user_obj = User.objects.filter(email=user["email"]).first()
                if not user_obj:
                    return self.send_unauthorized_response()
                request.auth_user = user_obj
                role = user_obj.role
                if not role:
                    return self.send_unauthorized_response("ROLE is missing for this user")
                request.role = role
                is_admin = False
                if role.name == "ADMIN":
                    is_admin = True
                request.is_admin = is_admin
                permissions_list = list(role.permissions.all().values("name"))
                permissions_list = [i['name'] for i in permissions_list]
                request.permissions = permissions_list

            except Exception as e:
                return self.send_unauthorized_response(f"{e}")

        response = self.get_response(request)
        return response

