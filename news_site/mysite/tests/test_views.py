from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User, Group

from mysite.models import Topic, Article, Comment


class TopicViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'testuder@vk.ru', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')
        Topic.objects.create(topic='Topic1')
        Topic.objects.create(topic='Topic2')
        Group.objects.create(name='admins')
        Group.objects.create(name='editors')
        Group.objects.create(name='readers')

    def test_topic_list_view(self):
        test_response = self.client.get('/topics')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('topics' in test_response.context)
        self.assertTemplateUsed(test_response, 'mysite/actions/topics/topic_edit.html')
        self.assertEqual(test_response.context['topics'][0].topic, 'Topic1')
        self.assertEqual(test_response.context['topics'][0].id, 5)
        self.assertEqual(test_response.context['topics'][1].topic, 'Topic2')
        self.assertEqual(test_response.context['topics'][1].id, 6)

    def test_topic_create_view(self):
        test_response = self.client.get('/topic/create')
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, 'mysite/actions/topics/create.html')

    def test_topic_update_view(self):
        test_response = self.client.get('/topic/7/update')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('topic' in test_response.context)
        self.assertTemplateUsed(test_response, 'mysite/actions/topics/update.html')
        self.assertEqual(test_response.context['topic'].pk, 7)
        self.assertEqual(test_response.context['topic'].topic, 'Topic1')
        null_response = self.client.get('/topic/11/update')
        self.assertEqual(null_response.status_code, 404)

    def test_topic_delete_view(self):
        test_response = self.client.get('/topic/3/delete')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('topic' in test_response.context)
        self.assertTemplateUsed(test_response, 'mysite/actions/topics/delete.html')
        self.assertEqual(test_response.context['topic'].pk, 3)
        self.assertEqual(test_response.context['topic'].topic, 'Topic1')
        null_response = self.client.get('/topic/11/delete')
        self.assertEqual(null_response.status_code, 404)

# class ArticleViewTest(TestCase):
#     def setUp(self):
#         pass
#
#     def test_article_list_view(self):
#         # main view
#         pass
#
#     def test_article_view(self):
#         pass
#
#     def test_article_create_view(self):
#         pass
#
#     def test_article_update_view(self):
#         pass
#
#     def test_article_delete_view(self):
#         pass
#
#
# class CommentViewTest(TestCase):
#     def setUp(self):
#         pass
#
#     def test_comment_list_view(self):
#         # article view
#         pass
#
#     def test_comment_create_view(self):
#         # article view
#         pass
#
#     def test_comment_update_view(self):
#         pass
#
#     def test_comment_delete_view(self):
#         pass
