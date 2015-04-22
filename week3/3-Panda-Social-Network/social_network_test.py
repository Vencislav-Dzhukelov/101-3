from panda import Panda
from social_network import PandaSocialNetwork
from social_network import PandaAlreadyThere, PandasAlreadyFriends

import unittest


class TestSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.my_panda = Panda("Name", "panda@gmail.com", "male")
        self.your_panda = Panda("Name", "panda@gmail.com", "male")
        self.his_panda = Panda("Dancho", "dancho_panda@gmail.com", "male")

        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")

        self.sn = PandaSocialNetwork()

    def test_init(self):
        self.assertEqual(self.sn.get_social_network(), {})

    def test_add(self):
        self.sn.add(self.my_panda)
        with self.assertRaises(PandaAlreadyThere):
            self.sn.add(self.your_panda)
        self.assertEqual(self.sn.get_social_network(), {self.my_panda: []})

    def test_has_panda(self):
        self.sn.add(self.my_panda)
        self.assertTrue(self.sn.has_panda(self.my_panda))

    def test_already_frends(self):
        self.sn.add(self.my_panda)
        self.sn.add(self.his_panda)
        self.sn.make_friends(self.my_panda, self.his_panda)
        with self.assertRaises(PandasAlreadyFriends):
            self.sn.make_friends(self.my_panda, self.his_panda)
        with self.assertRaises(PandasAlreadyFriends):
            self.sn.make_friends(self.his_panda, self.my_panda)

    def test_are_friends(self):
        self.sn.add(self.my_panda)
        self.sn.make_friends(self.my_panda, self.his_panda)
        self.assertTrue(self.sn.are_friends(self.my_panda, self.his_panda))

    def test_friends_of(self):
        self.sn.add(self.my_panda)
        self.sn.make_friends(self.my_panda, self.his_panda)
        self.assertEqual(self.sn.friends_of(self.my_panda), [self.his_panda])

    def test_connection_level(self):
        for panda in [self.ivo, self.rado, self.tony]:
            self.sn.add(panda)

        self.sn.make_friends(self.ivo, self.rado)
        self.sn.make_friends(self.rado, self.tony)
        self.assertTrue(self.sn.connection_level(self.ivo, self.rado) == 1)
        self.assertTrue(self.sn.connection_level(self.ivo, self.tony) == 2)

    def test_are_connected(self):
        result = self.sn.are_connected(self.my_panda, self.his_panda)
        self.assertFalse(result)

    def test_how_many_gender(self):
        for panda in [self.ivo, self.rado, self.tony]:
            self.sn.add(panda)

        self.sn.make_friends(self.ivo, self.rado)
        self.sn.make_friends(self.rado, self.tony)
        self.assertEqual(self.sn.how_many_gender_in_network(1, self.rado, "female"), 1)


if __name__ == '__main__':
    unittest.main()
