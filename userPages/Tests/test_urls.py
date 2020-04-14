# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from userPages.views import author_profile, author_view_journals, create_profile, ProposalDetailView, reviewer_view_proposals
#
# # Author: Himika Dastidar
# # Date: 2020-04-12
# # Tutorial: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
# # NOTE: EACH TEST CASE MUST BEGIN WITH TEST_*
# class TestUserPagesUrl(SimpleTestCase):
#
#     def test_proposal_view_is_resolved(self):
#         url = reverse('Proposal View')
#         self.assertEquals(resolve(url).func, reviewer_view_proposals)
#
#     """
#     Currently failing test
#     """
#     def test_proposal_detail_is_resolved(self):
#         url = reverse('proposal-detail')
#         self.assertEquals(resolve(url).func, ProposalDetailView.as_view())
#
#     """
#     Currently failing test
#     """
#     def test_create_profile_is_resolved(self):
#         url = reverse('create-profile')
#         self.assertEquals(resolve(url).func, create_profile)
#
#
#     def test_author_view_journals_is_resolved(self):
#         url = reverse('Journal View')
#         self.assertEquals(resolve(url).func, author_view_journals)
#
#
#     def test_author_profile_is_resolved(self):
#         url = reverse('Author Profile')
#         self.assertEquals(resolve(url).func, author_profile)