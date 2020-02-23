from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# class UserListView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users)
#         return Response(serializer.data)