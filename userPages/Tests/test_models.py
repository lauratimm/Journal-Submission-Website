from django.test import TestCase
from userPages.models import Institution, Paper, Journal, Proposal, Comment
from django.contrib.auth.models import User
import datetime


"""
Author: Himika Dastidar
source: https://www.youtube.com/watch?v=IKnp2ckuhzg

"""
class TestModels(TestCase):

    def setUp(self):

        '''
        Create a institution object ins 1
        '''

        self.ins1 = Institution.objects.create(name = 'University A',
                                            address = '123 Main St SW')

        self.ins2 = Institution.objects.create(name = 'University of Calgary',
                                            address = '2500 University Dr. NW')

        '''
        Create user objects and assign them as author, reviewer and editor
        '''
        self.author = User.objects.create_user(username = 'Theodore Dostoevsky')                    #Source https://docs.djangoproject.com/en/3.0/topics/auth/default/

        self.reviewer1 = User.objects.create_user(username = 'Jeremy Stuart')

        self.reviewer2 = User.objects.create_user(username = 'Laura Timm')

        self.reviewer3 = User.objects.create_user(username = 'Anna Chaykovska')

        self.editor1 = User.objects.create_user(username = 'Alex Tenney')

        '''
        Create a paper object
        '''
        self.testPaper = Paper.objects.create(author = self.author,
                                              version = 1,
                                              upload_date = datetime.datetime(2020, 1, 1))


        '''
        Create a journal object
        
        '''
        self.journal1 = Journal.objects.create(name = 'Nature',
                                               institution = 'University of Alberta',
                                               editor = self.editor1)

        '''
        Create a proposal object
        '''
        self.proposal1 = Proposal.objects.create(author = self.author,
                                                 reviewer_1 = self.reviewer1,
                                                 reviewer_2 = self.reviewer2,
                                                 reviewer_3 = self.reviewer3,
                                                 title = 'War and Peace',
                                                 abstract = 'Long long time ago, there was a man who sold the world.',
                                                 status = 'submitted',
                                                 due_date = datetime.datetime(2020, 1, 1),
                                                 upload_date = datetime.datetime(2020, 1, 1),
                                                 version = 1,
                                                )


    '''
    test if institution returns the name properly
    '''
    def test_institution_1(self):
        self.assertEquals(self.ins1.get_Name(), 'University A')

     '''
     test if institution name returns properly
     '''
    def test_institution_2(self):
        self.assertEquals(self.ins2.get_Name(), 'University of Calgary')


    def test_paper(self):
        self.assertEquals(self.testPaper.get_author(), 'Theodore Dostoevsky')
        self.assertEquals(self.testPaper.get_version(), 1)
        self.assertEquals(self.testPaper.get_uploadDate(), datetime.datetime(2020, 1, 1))

        #no file tested as I have not figured out how to get it to work yet

    def test_journal(self):
        self.assertEquals(self.journal1.get_journalName(), 'Nature')
        self.assertEquals(self.journal1.get_institution(), 'University of Alberta')
        self.assertEquals(self.journal1.get_editor(), 'Alex Tenney')



    def test_proposal1(self):
        self.assertEquals(self.proposal1.get_author(), 'Author is: Theodore Dostoevsky')
        self.assertEquals(self.proposal1.get_reviewers(), 'Reviewers are : Jeremy Stuart, Laura Timm, Anna Chaykovska')
        self.assertEquals(self.proposal1.get_status(), 'submitted')
        self.assertEquals(self.proposal1.get_dueDate(), datetime.datetime(2020, 1,1))
        self.assertEquals(self.proposal1.get_uploadDate(), datetime.datetime(2020, 1, 1))






