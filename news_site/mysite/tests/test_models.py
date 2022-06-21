from unittest import TestCase
from mysite.models import Topic

class TopicModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
       Topic.objects.create(topic='Some Topic')

    def test_topic_label(self):
        topic = Topic.objects.get(topic='тема тест')
        field_label = topic._meta.get_field('topic').verbose_name
        self.assertEquals(field_label, 'topic')

    def test_topic_max_length(self):
        topic = Topic.objects.get(topic='тема тест')
        max_length = topic._meta.get_field('topic').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_topic(self):
        topic = Topic.objects.get(topic='тема тест')
        expected_object_name = '%s' % topic.topic
        self.assertEquals(expected_object_name, str(topic))
