import doctest
import importlib
import pkgutil

from pathlib import Path


import pytest

import joke_machine


modules = [
    importlib.import_module(name)
    for _, name, _ in pkgutil.walk_packages(
        joke_machine.__path__, joke_machine.__name__ + "."
    )
]
doctest_globals = {}


@pytest.mark.parametrize("module", modules)
def test_doctest(module):
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner()
    tests = finder.find(module)

    failures = 0
    for test in tests:
        # Create a fresh copy of the globals for each test
        test_globals = dict(doctest_globals)
        test.globs.update(test_globals)

        # Run the test
        failures += runner.run(test).failed

    assert failures == 0, f"{failures} doctest(s) failed in module {module.__name__}"
