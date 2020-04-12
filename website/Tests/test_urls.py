from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import home, loginRequest

#
# Author: Himika Dastidar
# Goal: trying to run test to see if the urls are working in website
# Date: 2020-04-12
# Source:https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2&frags=wn

class TestUrls(SimpleTestCase):
    def test_loginRequest_is_resolved(self):
        url = reverse('loginrequest')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, loginRequest)


    def test_home_is_resolved(self):
        url = reverse('home')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, home)

