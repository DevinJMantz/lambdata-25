import pytest
from lambdata.wallet import Wallet 

@pytest.fixture
def empty_wallet():
    """Return empty wallet"""
    return Wallet()

@pytest.fixture
def wallet():
    """returns wallet with 20"""
    return Wallet(20)


def test_defaults(empty_wallet):
    assert empty_wallet.balance == 0

def test_set_init_amount(wallet):
    assert wallet.balance == 20

def test_walet_add_cash(wallet):
    wallet.add_cash(100)
    assert wallet.balance == 120

def test_walle_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

