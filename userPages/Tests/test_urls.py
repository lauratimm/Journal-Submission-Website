from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userPages.views import author_profile, author_view_journals, create_profile, ProposalDetailView, reviewer_view_proposals


class TestUserPagesUrl(SimpleTestCase):

    def proposal_view_is_resolved(self):
        url = reverse('Proposal View')
        self.assertEquals(resolve(url).func, reviewer_view_proposals)


    def proposal_detail_is_resolved(self):
        url = reverse('proposal-detail')
        self.assertEquals(resolve(url).func, ProposalDetailView.as_view())

    def create_profile_is_resolved(self):
        url = reverse('create-profile')
        self.assertEquals(resolve(url).func, create_profile)


    def author_view_journals_is_resolved(self):
        url = reverse('Journal View')
        self.assertEquals(resolve(url).func, author_view_journals)


    def author_profile_is_resolved(self):
        url = reverse('Author Profile')
        self.assertEquals(resolve(url).func, author_profile)