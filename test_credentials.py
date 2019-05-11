import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    """
    Define a TestCredentials subclass that inherits properties and behaviours from
    unittest.TestCase superclass above.
    Below, define a setUp() method that instantiates new_credentials
    instance of class Credentials before any tests can be run
    """

    def setUp(self):
        self.creadentials_test = Credentials("lwairore", "Yahoo", "4280")

    def tearDown(self):
        """
        tearDown() method will empty credentials class variable after every 
        test.
        """
        Credentials.credentials = []

    def test_save_individual_credential(self):
        """
        This method will take take in an instance that 
        it will later on use that instance to call save_credential() method
        that will also pass in that instance as self.Finally, these method
        will use assertEqual to assertain if the length of credentials class variable is
        equal to one(1)        
        """
        self.creadentials_test.save_credential()
        self.assertEqual(len(Credentials.credentials), 1)

    def test_save_multiple_credentials(self):
        """
        This method test to assertain if a save_credential() method can
        save append multiple instances to Credential's class variable by comparing it's actual
        length to assertain if it's equal to three(3)
        This method takes in an instance.
        """
        self.creadentials_test.save_credential()
        test_lucas_credential = Credentials("Lucas Abraham", "Bingo", "0712")
        test_lucas_credential.save_credential()
        test_sharon_credential = Credentials("Sharoon", "Gmail", "8901")
        test_sharon_credential.save_credential()
        self.assertEqual(len(Credentials.credentials), 3)


if __name__ == "__main__":
    """
    Checks if this file is being run as the main file
    or has been imported.
    """
    unittest.main()
