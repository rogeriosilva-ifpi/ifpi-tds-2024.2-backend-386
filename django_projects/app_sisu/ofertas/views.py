from rest_framework.views import APIView
from rest_framework.response import Response
from ofertas.models import Universidade
from ofertas.serializers import UniversidadeSerializer


class UniversidadeListAPIView(APIView):
    
    def get(self, request):
        universidades = Universidade.objects.all()
        serializer = UniversidadeSerializer(universidades, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UniversidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

 