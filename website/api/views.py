from .serializers import UserSerializer, CategorySerializer
from home.models import User, Category, Post
from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import generics


# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @api_view(['GET', 'POST'])



    def user_list(request):
        """
        List all code snippets, or create a new snippet.
        """

        if request.method == 'GET':
            all_users = User.objects.all()
            serializer = UserSerializer(all_users, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



        elif request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            
            if User.objects.filter(username=self.cleaned_data['uname']).exists():
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
    
            else:
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def custom_exception_handler(exc, context):
            response = exception_handler(exc, context)
            if response is not None:
                response.data['status_code'] = response.status_code


class DeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CategoryView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    '''
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
    '''

    @api_view(['GET', 'POST'])



    def user_list(request):
        """
        List all code snippets, or create a new snippet.
        """

        if request.method == 'GET':
            all_users = Category.objects.all()
            serializer = CategorySerializer(all_users, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



        elif request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def custom_exception_handler(exc, context):
            response = exception_handler(exc, context)
            if response is not None:
                response.data['status_code'] = response.status_code



class DeleteCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
