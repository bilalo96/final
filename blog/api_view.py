from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404 , get_list_or_404


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_posts = get_list_or_404(Post , active=True)
    data = PostSerializer(all_posts , many = True, context={"request":request}).data
    return Response({'data':data})



@api_view(['GET'])
def post_detail_api(request, id):
    post = get_object_or_404(Post , id=id)
    data = PostSerializer(post).data
    return Response({'data':data})



@api_view(['GET'])
def post_search_api(requset, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) |
         Q(description__icontains=query)
    )
    data = PostSerializer(posts, many=True).data
    return Response({'data':data})
