import unittest
from flask_login import current_user
from app import db
from app.models import User,Pitch

class TestPitch(unittest.TestCase):

    '''
    class facilitates the creation of test units to test Pitch class behavior
    '''

    def setUp(self):

        '''
        function runs before every test case
        '''
        self.user_peaches = User(username="Peaches",password="geranimo",email="peaches@ms.com")
        self.new_pitch = Pitch(pitch_title="Humanity's hope",pitch_content="The development of more stringent interaction measures in this globalized age offer the bests chance for human's survival",category='humanity',user=user_peaches)
    
    def test_instance(self):

        '''
        function checks if objects are initialized properly
        '''
        self.assertTrue(isinstance(self.new_pitch,Pitch))
    
    def test_instance_variables(self):

        '''
        function checks if individual pitch properties are initialized properly
        '''
        self.assertEqual(self.new_pitch.id,1)
        self.assertEqual(self.new_pitch.pitch_title,"Humanity's hope")
        self.assertEqual(self.new_pitch.pitch_content,"The development of more stringent interaction measures in this globalized age offer the bests chance for human's survival")
        self.assertEqual(self.new_pitch.user,self.user_peaches)

    def test_save_pitch(self):

        '''
        function checks if pitches are saved to the database
        '''
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
    
    def test_get_pitches(self):

        '''
        function checks if it is possible to get pitch using pitch's id
        '''
        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches('humanity')
        self.assertTrue(len(got_pitches) == 'humanity')