from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from .models import PetProfile
from .serializers import PetProfileSerializer

# Create your views here.

#for profile images 
class PetProfileViewSet(viewsets.ModelViewSet):
    queryset = PetProfile.objects.order_by('-pet_name')
    serializer_class = PetProfileSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profiles(request):
    profiles = PetProfile.objects.filter(user_id=request.user.id)
    serializer = PetProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request, pk):
    images = get_object_or_404(PetProfile, pk=pk)
    if request.method == 'GET':
        serializer = PetProfileSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pet_single(request, pk):
    one_profile = get_object_or_404(PetProfile, pk=pk)
    if request.method == 'GET':
        serializer = PetProfileSerializer(one_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)



    # path('<int:pk>/', views.pet_single),
    # path('createpet/', views.create_pet),
    # path('editpet/', views.edit_pet),
    # path('guest/', views.guest_views),