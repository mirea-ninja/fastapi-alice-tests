import setuptools


long_description = """
# fastapi-alice-tests

Class for autotests Yandex.Alice skill, that implemented as Fast API application
"""

setuptools.setup(
    name='fastapi_alice_tests',
    version='1.0',
    author='Mirea Ninja',
    author_email='contact@mirea.ninja',
    description='Class for autotests Yandex.Alice skill, that implemented as Fast API application',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ninja-Official/fastapi-alice-tests',
    packages=['fastapi_alice_tests'],
    download_url='https://github.com/Ninja-Official/fastapi-alice-tests/archive/v1.0.tar.gz',
    keywords=['python', 'Yandex.Alice', 'Fast API', 'unittest'],
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Fast API",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
