import unittest
from flask_login import current_user
from app import db
from app.models import Comment,User,Pitch

class TestComment(unittest.TestCase):

    '''
    class facilitates the creation of test units to test comment class behavior
    '''
    def setUp(self):

        '''
        test runs before all other tests
        '''
        self.user_peaches = User(username="peaches",password="geranimo",email="peaches@ms.com")
        
        self.new_pitch = Pitch(id=1,pitch_title="Humanity's hope",pitch_content="The development of more stringent interaction measures in this globalized age offer the bests chance for human's survival",category="humanity",user=self.user_peaches)

        self.new_comment = Comment(id=1,comment='meh',user=self.user_James,pitch=self.new_pitch)

    def tearDown(self):

        '''
        test runs after each test and ensures the accuracy of subsequent test runs
        '''
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()

    def test_instance(self):

        '''
        test checks if objects are initialized properly
        '''
        self.assertTrue(isinstance(self.new_user,User))
        self.assertTrue(isinstance(self.new_pitch,Pitch))
        self.assertTrue(isinstance(self.new_comment,Comment))