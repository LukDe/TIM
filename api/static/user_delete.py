from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render

#test method can be deleted in the future
def hello():
    print('test')

def delete_user():
