from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Trait
from .serializer import TraitSerializer


class TraitView(APIView):
    def get(self, request):
        return Response({"msg": "Rota GET de Traits!"})

    def post(self, request):
        serializer = TraitSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        trait = Trait.objects.create(**serializer.validated_data)

        serializer = TraitSerializer(trait)

        return Response(serializer.data, status.HTTP_201_CREATED)
