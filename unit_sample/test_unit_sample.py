from unittest import TestCase

class SampleTestCase(TestCase):
    def test_always_pass(self):
        self.assertTrue(True)

    def test_always_fail(self):
        self.assertTrue(False)
