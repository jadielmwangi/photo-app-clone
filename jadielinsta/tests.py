from django.test import TestCase

# Create your tests here.

class PostTestClass(TestCase):
    def setUp(self):
        self.sirmwas=Profile(title='sirmwas',Bio='testing')
        self.sirmwas.save_editor()

        self.new_post=Post(title='jadiel',post='testing',profile = self.sirmwas)
        self.new_post.save()

    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()

    def test_get_new_posts(self):
        new_posts = Post.new_posts()
        self.assertTrue(len(new_posts)>0)