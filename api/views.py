from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tim_app.models import Good
from api.serializers import GoodSerializer


@api_view(['GET', 'POST'])
def good_list(request, format=None):
    if request.method == 'GET':
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def good_detail(request, name, format=None):
    try:
        good = Good.objects.get(goodName=name)
    except Good.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GoodSerializer(good)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GoodSerializer(good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
