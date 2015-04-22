from bank_account import BankAccount
import unittest


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount("Myname", 130, "$")

    def test_init(self):
        self.assertTrue(isinstance(self.my_account, BankAccount))
        with self.assertRaises(ValueError):
            BankAccount("Myname", -10, "$")

    def test_deposit(self):
        self.my_account.deposit(50)
        self.assertTrue(self.my_account.balance == 180)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-50)
        self.assertTrue(self.my_account.balance == 180)

    def test_withdraw(self):
        self.assertEqual(self.my_account.withdraw(180), False)
        self.my_account.withdraw(50)
        self.assertEqual(self.my_account.balance, 80)

        with self.assertRaises(ValueError):
            self.my_account.deposit(-50)
        self.assertEqual(self.my_account.balance, 80)

    def test_str(self):
        needed_result = "Bank account for Myname with balance of 130$"
        self.assertEqual(str(self.my_account), needed_result)

    def test_transfer_to_different_currency(self):
        your_account = BankAccount("Rado", 10, "BGN")

        with self.assertRaises(ValueError):
            self.my_account.transfer_to(your_account, 20)
        self.assertEqual(self.my_account.balance, 130)
        self.assertEqual(your_account.balance, 10)

    def test_transfer_to_more_money_that_we_have(self):
        your_account = BankAccount("Rado", 10, "$")

        self.assertFalse(your_account.transfer_to(self.my_account, 30))
        self.assertEqual(self.my_account.balance, 130)
        self.assertEqual(your_account.balance, 10)

    def test_transfer_to(self):
        your_account = BankAccount("Rado", 10, "$")
        self.assertTrue(self.my_account.transfer_to(your_account, 20))
        self.assertEqual(self.my_account.balance, 110)
        self.assertEqual(your_account.balance, 30)

    def test_history(self):
        self.assertIn('Account was created', self.my_account.account_history())

        self.my_account.get_balance()
        self.assertIn('Balance check -> ' + str(self.my_account.get_balance()),
                      self.my_account.account_history())

        int(self.my_account)
        self.assertIn('__int__ check -> ' + str(self.my_account.get_balance()),
                      self.my_account.account_history())

        self.my_account.deposit(50)
        self.assertIn('Deposited 50' + self.my_account.currency,
                        self.my_account.account_history())


if __name__ == '__main__':
    unittest.main()
