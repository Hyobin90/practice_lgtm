# a script testing `core.py`
import unittest
#import debugpy


class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm('./python.jpeg', 'LGTM'))

# def initialize_debugger():
#     if not debugpy.is_client_connected():
#         debugpy.listen(("localhost", 5679))
#         print("Waiting for debugger to attach...")
#         debugpy.wait_for_client()


if __name__ == '__main__':
    #initialize_debugger()
    unittest.main()