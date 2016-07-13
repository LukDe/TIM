##
## Views.py
##
## This file defines the views for the application. Since they represent a REST Api,
## they only return Json objects, instead of Html files. At the moment all views are open
## for the user (which sould be later changed with authorization and authetication.)
##
## Each view receives a Request, and each request can be one of the following methods:
## - GET (gets a resource)
## - POST (partially updates or creates a resource)
## - DELETE (deletes a resource)
## - PUT (updates a resource), probably not going to be used on the app.
##
## For example:
##    GET localhost:8000/api/goods, should get a list of all Good models on the app.
##    POST localhost:8000/api/goods + json, should create a new Good models on the app.
##    DELETE localhost:8000/api/goods, should delete all Good models on the app.
##
## Note that the example above is just a convention, different approaches could be used.
##
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from tim_app.models import Good, Request, User
from tim_app.models import Supply as Offer
from api.serializers import GoodSerializer, RequestSerializer, OfferSerializer, UserSerializer, LoginFormSerializer, VerificationSerializer
from sms.utils import send_sms_message
from api.static import passGen
import api.expiration as exp
from api.static.match import find_match_for_request, find_match_for_supply


# This is a view definition, the same way as views on tim_app.
# The difference is that this views return Json Objects as responses,
# instead of Html files, the conversion model -> json is given by the respective
# Serializer defined in `serializers.py`.
# Inside the view it is checked the method of the request (request.method), that
# way we can create different functionalities for different methods.
@csrf_exempt
@api_view(['GET','POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, name, format=None):
    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['POST'])
def login(request, format=None):
    if request.method == 'POST':
        login_form_serializer = LoginFormSerializer(data = request.data)
        if login_form_serializer.is_valid():
            req_username = login_form_serializer.validated_data.get('username')
            req_password = login_form_serializer.validated_data.get('password')
            try:
                user = User.objects.get(username=req_username)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if user.password != req_password:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
@api_view(['GET', 'POST'])
def request_list(request, format=None):
    if request.method == 'GET':
        exp.check_if_expired()
        requests = Request.objects.all().filter(active = True)
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            req = serializer.create(validated_data=serializer.validated_data)
            print(req.id)
            find_match_for_request(req.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def request_detail(request, reqid, format=None):
    try:
        req = Request.objects.get(id=reqid)
    except Request.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RequestSerializer(req)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RequestSerializer(request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            find_match_for_request(reqid)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def offer_list(request, format=None):
    if request.method == 'GET':
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            off = serializer.create(validated_data=serializer.validated_data)
            print(off.id)
            find_match_for_supply(off.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print (serializer.data)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def offer_detail(request, offid, format=None):
    try:
        offer = Offer.objects.get(id=offid)
    except Offer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OfferSerializer(offer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OfferSerializer(request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            find_match_for_supply(offid)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
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


@csrf_exempt
@api_view(['POST'])
def verification(request, format=None):
    if request.method == 'POST':
        verify = passGen.generate()
        print("send Sms ")
        send_sms_message(
            request.data['phoneNr'],
            'Dein Bestätigungscode lautet: ' + verify)
        verificationSerializer = VerificationSerializer(data = {"verification":verify})
        if verificationSerializer.is_valid():
            print(verificationSerializer.data)
            return Response(verificationSerializer.data)
        else:
            print(verificationSerializer.errors)
            return Response(verificationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
