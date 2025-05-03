from {{ cookiecutter.package_slug }}.core 

import hello 

def test_hello():
    assert hello() == "hello world"
