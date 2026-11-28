import stemulous_genre

def test_package_imports_and_has_version():
    assert isinstance(stemulous_genre.__version__, str)
    assert stemulous_genre.__version__.count(".") >= 1
