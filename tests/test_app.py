import unittest

from bridge_app import hello

class TestBridgeApp(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello(), "Hello World!\n")

if __name__ == '__main__':
  unittest.main()