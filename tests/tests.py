import unittest
import os

from argparse import ArgumentParser


class CheckTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()
        self.subparser = self.parser.add_subparsers()
        self.email_parser = self.subparser.add_parser('email')
        self.email_parser.set_defaults(email=os.environ.get('EMAIL'))

    def test_email(self):
        args = self.parser.parse_args(['email'])
        self.assertEqual(args.email, os.environ.get('EMAIL'))


if __name__ == '__main__':
    unittest.main()
