from django.test import TestCase
from .models import Item

# Create your tests here
class Testmodels(testCase):
    item=Item.objects.create(name='Test Todo Item')
    self.assertFalse(item.done)
    

