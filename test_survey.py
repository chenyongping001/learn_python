from unittest import TestCase
from survey import AnonymousSurvey


class TestAnonymousSurvey(TestCase):
    """针对AnonymousSurver类的测试"""

    def setUp(self):
        self.question = "What language did you fisrt learn to speak?"
        self.my_surver = AnonymousSurvey(self.question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        "测试每个答案都被妥善地存储"
        self.my_surver.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_surver.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_surver.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_surver.responses)
