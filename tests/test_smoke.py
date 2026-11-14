import platitude_genre

def test_package_imports_and_has_version():
    assert isinstance(platitude_genre.__version__, str)
    assert platitude_genre.__version__.count(".") >= 1
