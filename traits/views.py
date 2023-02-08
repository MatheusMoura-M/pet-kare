from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from .models import Trait
from .serializers import TraitSerializer


class TraitView(APIView):
    def get(self, request: Request) -> Response:
        traits = Trait.objects.all()

        serializer = TraitSerializer(traits, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = TraitSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        trait = Trait.objects.create(**serializer.validated_data)

        serializer = TraitSerializer(trait)

        return Response(serializer.data, status.HTTP_201_CREATED)
