from django.core.urlresolvers import reverse
from django.test import TestCase


class CheeseTest(TestCase):
    def test_home(self):
        url = reverse('cheese_list')
        response = self.client.get(url)
        self.assertContains(response, 'Cheese')
