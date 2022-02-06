# -*- coding: utf-8 -*-
import os
import pytest


@pytest.fixture()
def pwd():
    return os.path.dirname(os.path.abspath(__file__))


def test_all_fixtures(pwd, testdir):
    """Make sure that pytest accepts our fixtures."""

    print(pwd)

    conventions_file = open(os.path.join(pwd, 'example_conventions.py')).read()

    # create a temporary pytest test module
    testdir.makepyfile(conventions_file)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v'
    )

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
