# from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def test():
    return HttpResponseRedirect(reverse('home'))
