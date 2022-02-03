# -*- coding: utf-8 -*-


def test_all_fixtures(testdir):
    """Make sure that pytest accepts our fixtures."""

    conventions_file = open('/workspaces/pytest-dbt-conventions/tests/example_conventions.py').read()

    # create a temporary pytest test module
    testdir.makepyfile(conventions_file)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v'
    )

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
