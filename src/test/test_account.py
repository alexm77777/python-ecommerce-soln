from unittest import TestCase
from ..account import get_accounts, login


class TestAccount(TestCase):
    def test_get_accounts(self):
        accounts = get_accounts('src/test/fixtures/accounts.csv')
        self.assertDictEqual(accounts, {
            'bob': 'b',
            'sally': 's',
            'frank': 'f'
        })

    def test_login(self):
        accounts = get_accounts('src/test/fixtures/accounts.csv')
        value = login('bob', 'b', accounts)
        self.assertTrue(value)
