from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer


class BlogList(APIView):
    serializer_class = BlogSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(
            blogs, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        """
            Deserialize the requested data, 
            if the data is valid, save it with the current user (owner)
            if data valid return the post with 201 status
            if data is not valid return 400 error code
        """
        serializer = BlogSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)