# `pytest-xfailer`: external xfail configuration

Pytest's `xfail` is really cool and can be used for all sorts of
purposes, however one of its limitations is out of the box it can only
be used by editing the code and `mark`-ing test nodes. There are cases
where this is less than ideal.

This plugin solves that issue: if there exists an `xfail.conf` file at
the project's rootdir (usually the location of `pytest.ini` or
`pyproject.toml`) then all the nodeids in this file (one per line)
will automatically be marked as xfailed if encountered. You may or may
not want to tune [`strict_xfail`] in your pytest configuration.

## Limitations

Currently, xfailer has no support for any [xfail parameter].

[`strict_xfail`]: https://docs.pytest.org/en/stable/reference/reference.html#confval-strict_xfail
[xfail parameter]: https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-xfail-ref
