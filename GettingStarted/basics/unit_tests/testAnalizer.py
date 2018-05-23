import unittest

class TestAnalizer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_func_not_runs(self):
        analize()

    def test_func_runs(self):
        analize_run()
        self.assertEqual(True)

def analize_run():
    pass

if __name__ == '__main__':
    unittest.main()