from rest_framework import viewsets , permissions , serializers
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import *
from API.permissions import *

class settingsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, isOwner, )
    queryset = settings.objects.all()
    serializer_class = settingsSerializer

class themeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = theme.objects.all()
    serializer_class = themeSerializer

class calendarViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, isOwner )
    serializer_class = calendarSerializer
    def get_queryset(self):
        return calendar.objects.filter(user =  self.request.user)

class notificationViewSet(viewsets.ModelViewSet):
    permission_classes = (isOwner, )
    serializer_class = notificationSerializer
    def get_queryset(self):
        return notification.objects.filter(user = self.request.user , read = False).order_by('-created')

class chatMessageViewSet(viewsets.ModelViewSet):
    permission_classes = (isOwner, )
    serializer_class = chatMessageSerializer
    def get_queryset(self):
        qs1 = chatMessage.objects.filter(user = self.request.user).order_by('-created')
        if 'mode' in self.request.GET:
            return qs1
        else:
            msgs = []
            usrs = []
            for msg in qs1:
                if msg.originator not in usrs or msg.read == False:
                    msgs.append(msg)
                    usrs.append(msg.originator)
            qs2 = chatMessage.objects.filter(originator = self.request.user).order_by('-created')
            usrs = []
            for msg in qs2:
                if msg.user not in usrs:
                    msgs.append(msg)
                    usrs.append(msg.user)
            return msgs[:300]

class chatMessageBetweenViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, readOnly)
    serializer_class = chatMessageSerializer
    def get_queryset(self):
        reciepient = User.objects.get(username = self.request.GET['other'])
        qs1 = chatMessage.objects.filter(originator = self.request.user , user= reciepient)
        qs2 = chatMessage.objects.filter(user = self.request.user , originator= reciepient)
        qs = qs1 | qs2
        for msg in qs:
            msg.read = True
            msg.save()
        return qs.order_by('created')[:150]

class blogViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = blogSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title' , 'state']
    def get_queryset(self):
        if 'state' not in self.request.GET and 'tags' not in self.request.GET and 'user' not in self.request.GET:
            return blogPost.objects.filter( users__in=[self.request.user,])
        if 'state' in self.request.GET:
            st = self.request.GET['state']
            if st != 'published':
                qs = blogPost.objects.filter( users__in=[self.request.user,])
            else:
                qs = blogPost.objects.filter(state= 'published')
        else:
            qs = blogPost.objects.filter(state='published')

        if 'tags' in self.request.GET:
            tags = []
            for t in self.request.GET['tags'].split(','):
                tags.append(blogCategory.objects.get(pk = int(t)))
            qs = qs.filter(tags__in=tags )

        if 'user' in self.request.GET: # filter for a perticular user
            qs = qs.filter(users__in=[User.objects.get(username=self.request.GET['user']),])

        return qs

class blogCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = blogCategorySerializer
    queryset = blogCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']


class blogCommentsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = blogCommentsSerializer
    queryset = blogComment.objects.all()
class blogLikesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = blogLikeSerializer
    queryset = blogLike.objects.all()
class blogCommentLikesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = blogCommentLikeSerializer
    queryset = blogCommentLike.objects.all()


class notebookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, isOwner,)
    serializer_class = notebookSerializer
    def get_queryset(self):
        return notebook.objects.filter(user = self.request.user ).order_by('-created')

class pageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, isOwner,)
    serializer_class = pageSerializer
    def get_queryset(self):
        return page.objects.filter(user = self.request.user ).order_by('-created')
