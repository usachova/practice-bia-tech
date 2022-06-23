from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User, Group

from mysite.models import Topic


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
        self.assertEqual(test_response.context['topics'][1].topic, 'Topic2')

    def test_topic_create_view(self):
        pass

    def test_topic_update_view(self):
        pass

    def test_topic_delete_view(self):
        pass


################################

# class MainViewTest(TestCase):
#     pass
#
# class ArticlesCreateViewTest(TestCase):
#     pass
#
# class ArticleViewTest(TestCase):
#     pass
#
# class ArticlesUpdateViewTest(TestCase):
#     pass
#
# class ArticlesDeleteViewTest(TestCase):
#     pass
#
#
#
# class LoginUserViewTest(TestCase):
#     pass
#
# class RedistrUserViewTest(TestCase):
#     pass
#
# class LogoutUserViewTest(TestCase):
#     pass
#
#
#
# class CommentUpdateView(TestCase):
#     pass
#
# class CommentDeleteView(TestCase):
#     pass
