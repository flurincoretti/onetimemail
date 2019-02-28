# onetimemail

One-time email address generator.

## Installing

To install manually, download the repo and run

```
$ pip install .
```

## Usage

Generate a one-time email address:

```
$ otm
910f1cbc9caf3a13@example.com
```

Set your own domain:

```
$ otm --domain mydomain.com
817e1cd9112256c3@mydomain.com
```

Set the length of the randomly generated string:

```
$ otm --length 32
51c15d04e53e9d4b113041fdd2da39d7@mydomain.com
```