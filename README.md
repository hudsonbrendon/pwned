# Pwned

[![Build Status](https://travis-ci.org/hudsonbrendon/pwned.svg?branch=master)](https://travis-ci.org/hudsonbrendon/pwned)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/pwned.svg?style=flat)](https://github.com/hudsonbrendon/pwned/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![logo](logo.jpg)

Check if you have an account that has been compromised in a data breach

This tool is based on [https://haveibeenpwned.com/](https://haveibeenpwned.com/)

# Quick start

```bash
$ pip install ppwned
```
or

```bash
$ python setup.py install
```

# Usage

You can import the library and use it in your project that way:

```python
>>> from pwned import check

>>> check(<email>)
```
Or just use it on the command line like this:

```bash
$ pwned <email>
```

# Dependencies

- [Python 3.5](https://www.python.org/downloads/release/python-350/)
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [requests](http://docs.python-requests.org/en/latest/)

# License

[MIT](http://en.wikipedia.org/wiki/MIT_License)
