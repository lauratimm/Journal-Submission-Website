# from django.test import TestCase
# import unittest
# from home.models import User
# from .models import Proposal
# from profile_maker.models import *
# import datetime
#
# # Create your tests here.
# '''
# Author: Himika Dastidar
# Date: 2020-04-05
#
# Source: https://docs.djangoproject.com/en/3.0/topics/testing/overview/
# '''
#
#
# class ProposalTestCase(TestCase):
#     '''
#     This in theory should create a proposal with predetermined values
#     Then the goal is to test different field using the getter methods
#     and assertEquals or assertNotEquals value
#
#
#     Note: this still doesnt run tests properly
#     '''
#
#
#
#     def setUp(self):
#         test = Proposal(author = User(author = 'Himika', reviewer = 'null', editor = 'null'),
#                         reviewer_1 =  User( author = 'null', reviewer = 'Jeremy', editor = 'null'),
#                         reviewer_2 =User(author='null', reviewer='Anna', editor='null'),
#                         reviewer_3 =User(author='null', reviewer='Laura', editor='null'),
#                         status = "SUBMITTED",
#                         version = 1)
#
#
#     def test1_proposal(self, test):
#         assertEqual(test.get_author(), 'Author is: Himika')
#
#     def test2_proposal(self):
#         assert self.reviewer_1 == 'Jeremy'
#
#     def test3_proposal(self):
#         assert self.reviewer_2 == 'Anna'
#
#     def test4_proposal(self):
#         assert self.reviewer_3 == 'Laura'
#
#     def test5_proposal(self):
#         assert self.version == 1
#
#
#     def teardown(self):
#         del self



