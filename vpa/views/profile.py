
from django.contrib.auth.models import User
from rest_framework import generics as views
from rest_framework.response import Response

from vpa.serializers.profile_serializers import ProfileModelSerializer


class RegisterProfile(views.CreateAPIView):
    serializer_class = ProfileModelSerializer

    def post(self, request, *args, **kwargs):
        uname = request.data['username']
        email = request.data['email']
        password = request.data['password']
        fname = request.data['first_name']
        lname = request.data['last_name']

        if not password:
            raise Exception('Password was not provided!')

        user = User.objects.create_user(username=uname,
                                        email=email,
                                        password=password,
                                        first_name=fname,
                                        last_name=lname
                                        )
        if user:
            response = Response(data=f'User {user.username} is successfully created.', status=201)
            return response




