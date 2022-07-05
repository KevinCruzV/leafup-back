from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentarySerializer, ImgUserSerializer, PlantsSerializer, PostSerializer, PostLikeSerializer, \
    RecordPostSerializer, SpeciesSerializer, UserSerializer, UserPlantsSerializer
from .models import Commentary, ImgUser, Plants, Post, PostLike, RecordPost, Species, User, UserPlants


# Create your views here.

class CommentaryView(viewsets.ModelViewSet):
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()


class ImgUserView(viewsets.ModelViewSet):
    serializer_class = ImgUserSerializer
    queryset = ImgUser.objects.all()


class PlantsView(viewsets.ModelViewSet):
    serializer_class = PlantsSerializer
    queryset = Plants.objects.all()


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostLikeView(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()


class RecordPostView(viewsets.ModelViewSet):
    serializer_class = RecordPostSerializer
    queryset = RecordPost.objects.all()


class SpeciesView(viewsets.ModelViewSet):
    serializer_class = SpeciesSerializer
    queryset = Species.objects.all()


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserPlantsView(viewsets.ModelViewSet):
    serializer_class = UserPlantsSerializer
    queryset = UserPlants.objects.all()
