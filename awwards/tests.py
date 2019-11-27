from django.test import TestCase
from .models import Profile,Project,Rate
from django.contrib.auth.models import User



# Create your tests here.
#testcases for project
class TestProject(TestCase):
    # Set up method
    def setUp(self):
        self.news_highlights= Project(id=1,image = '/static/images/pic.jpg',
        title ='news_highlights',description = 'news coverage',link = 'https://peninah-news-hub.herokuapp.com/')
        self.ninah = User(username='ninah')
        # self.ninah.save_username()
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.news_highlights,Project))

     # Testing Save Method
    def test_save_method(self):
        self.news_highlights.save_image()
        image = Project.objects.all()
        self.assertTrue(len(image) == 1)   

    def test_update(self):
        self.news_highlights.save_image()
        image = Project.objects.filter(title = "news_highlights").first()
        update = Project.objects.filter (id=image.id).update(title = "Searching_Github")
        updated = Project.objects.filter(title = "Searching_Github").first()
        self.assertTrue(Project.title,updated.title) 

    def test_delete(self):
        self.news_highlights.save_image()
        image = Project.objects.filter(title="News_Highlights").first()
        delete = Project.objects.filter(id=image.id).delete()
        image = Project.objects.all()
        self.assertTrue(len(image) ==0 )       

