>>> toml = """
... [python]
... label = "Python"
...
... [python.version]
... number = "3.10"
... release.date = 2021-10-04
... release.manager = "@pyblogsal"
... """

>>> import tomli
>>> tomli.loads(toml)
{'python': {'label': 'Python', 'version': {
    'release': {'date': datetime.date(2021, 10, 4), 'manager': '@pyblogsal'},
    'number': '3.10'}}}
