from panda import Panda
import unittest


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.my_panda = Panda("Name", "panda@gmail.com", "male")
        self.your_panda = Panda("Name", "panda@gmail.com", "male")

    def test_init(self):
        self.assertTrue(isinstance(self.my_panda, Panda))
        self.assertEqual(self.my_panda.name, "Name")
        self.assertEqual(self.my_panda.email, "panda@gmail.com")
        self.assertEqual(self.my_panda.gender, "male")

    def test_str(self):
        needed_result = "name: Name email: panda@gmail.com gender: male"
        self.assertEqual(str(self.my_panda), needed_result)

    def test_eq(self):
        self.assertTrue(self.my_panda == self.your_panda)

    def test_can_hash_panda(self):
        self.assertIsNotNone(hash(self.my_panda))

    def test_set_mail(self):
        self.assertTrue(self.my_panda)
        with self.assertRaises(ValueError):
            Panda("Name", "pandagmail.com", "male")
        with self.assertRaises(ValueError):
            Panda("Name", "pandag@mailcom", "male")


if __name__ == '__main__':
    unittest.main()
