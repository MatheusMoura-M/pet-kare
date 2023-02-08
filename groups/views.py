from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from .models import Group
from .serializers import GroupSerializer


class GroupView(APIView):
    def get(self, request: Request) -> Response:
        groups = Group.objects.all()

        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = GroupSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        group = Group.objects.create(**serializer.validated_data)

        serializer = GroupSerializer(group)

        return Response(serializer.data, status.HTTP_201_CREATED)
