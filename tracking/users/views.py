from django.contrib.auth.models import User
from rest_framework import viewsets
from users.serializers import UserSerializer
from django.http import HttpResponse
from django.utils.timezone import datetime



def index(request):
    request.session.set_test_cookie()
    visits = int( request.COOKIES.get('visits', '0') )
    response =  HttpResponse(template.render(context))
    if request.COOKIES.has_key('last_visit' ):
            last_visit = request.COOKIES['last_visit']
            # the cookie is a string - convert back to a datetime type
            last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
            curr_time = datetime.now()
            if (curr_time-last_visit_time).days > 0:
                    # if at least one day has gone by then inc the visit count.
                    response.set_cookie('visits', visits + 1 )
                    response.set_cookie('last_visit', datetime.now())
    else:
            response.set_cookie('last_visit', datetime.now())
    return response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



def about(request):

        ...

        if request.session.test_cookie_worked():
                print("The test cookie worked!!!")
                request.session.delete_test_cookie()