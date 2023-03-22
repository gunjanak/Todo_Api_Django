from django.test import TestCase

from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="First todo",
            body = "Do not do this",
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title,"First todo")
        self.assertEqual(self.todo.body,"Do not do this")
        self.assertEqual(str(self.todo),"First todo")