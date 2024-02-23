import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

"""
release checklist:
1. update version on `setup.py`
2. make release on PyPI. Run the following commands:
    2.1 `python3 setup.py sdist bdist_wheel`
    2.2 (optional) `python3 -m pip install --user --upgrade twine`
    2.3 `python3 -m twine upload dist/*`
"""

setuptools.setup(
    name="papyrus",
    version="0.0.0",
    author="Mayukh Deb",
    author_email="mayukhmainak2000@gmail.com",
    description="Simple markdown to webpage builder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mayukhdeb/papyrus",
    packages=setuptools.find_packages(),
    install_requires=None,
    include_package_data=True,
    keywords=[],
    classifiers=[
        "Intended Audience :: Education",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)