from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Group
from .serializer import GroupSerializer


class GroupView(APIView):
    def get(self, request):
        return Response({"msg": "Rota GET de Groups!"})

    def post(self, request):
        serializer = GroupSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        group = Group.objects.create(**serializer.validated_data)

        serializer = GroupSerializer(group)

        return Response(serializer.data, status.HTTP_201_CREATED)
