from random import choice
import time
import pytest


@pytest.fixture
def dummy():
    raise Exception('oops')


def test_passed():
    time.sleep(choice(range(0, 31)))


def test_failed():
    pytest.fail('Failed test')


def test_skipped():
    pytest.skip('Skipped test')


def test_error(dummy):
    assert dummy == 2


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_expected_failure():

    i = 1 / 0
    print i


@pytest.mark.xfail()
def test_unexpected_pass():
    pass
