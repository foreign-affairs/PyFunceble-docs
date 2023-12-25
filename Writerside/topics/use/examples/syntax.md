# Syntax Check

## Domains / IPs Syntax

PyFunceble can check the syntax of domains and IPs.

## Input Source

### Inline - CLI

You can check the syntax of a domain or IP, by running PyFunceble with the `-d` argument along with `--syntax` argument.

```Bash
pyfunceble -d example.net --syntax
```

The `-d` argument can also take multiple domains and IP addresses to test simultaneously.

```Bash
pyfunceble -d example.net example.org example.com 192.0.2.4 --syntax
```

<script async id="asciicast-OpqvsHdWBmD3jjLl0gVNVj7rK" src="https://asciinema.org/a/OpqvsHdWBmD3jjLl0gVNVj7rK.js"></script>

You can check the syntax of a URL through the `-u` argument of PyFunceble.

```Bash
pyfunceble -u https://github.com/pyfunceble
```

That `-u` argument can also take multiple URLs to test.

```Bash
pyfunceble -u https://github.com/pyfunceble https://gitlab.com/funilrys https://kb.mypdns.org/issues/MTX
```

<script async id="asciicast-s7Vvf821ax2aJ8QlPkMqKHd2v" src="https://asciinema.org/a/s7Vvf821ax2aJ8QlPkMqKHd2v.js"></script>


### File

You can check the syntax of the domains or IPs located inside a file, by giving the file path(s) to PyFunceble through the `-f` argument.

```Bash
pyfunceble -f ./source.list --syntax
pyfunceble -f https://example.org/my/awesome/file --syntax
```

When using the `-f` argument, the inputted source can be:

- any file-s on your filesystem accessible by the user running PyFunceble.
- an HTTP (raw) URLs of the file you want PyFunceble to download and check.

When testing for the syntax of domains or IPs, PyFunceble supports the
following file formats:

- hosts file
- plain text file
- AdBlock filter list (please use with the `--adblock` argument)
- RPZ (formatted) file (please use with the `--rpz` argument)

<script async id="asciicast-zoKLgHzy2Fpeud7KatlUQuGSf" src="https://asciinema.org/a/zoKLgHzy2Fpeud7KatlUQuGSf.js"></script>

## URLs Syntax

PyFunceble can check the syntax of URLs.

You can check the syntax of the URLs located inside a file, by
giving the file path-s to PyFunceble through the `-uf` argument.

```Bash
pyfunceble -uf ./source.url.list
pyfunceble -uf https://example.org/my/awesome/file
```

Just like the `-f` argument, when using the `-uf` argument, the inputted source can be:

- any file-s on your filesystem accessible by the user running PyFunceble.
- an HTTP(s) URL(s) of the  (raw) file you want PyFunceble to download and check.

When testing the syntax of URLs, PyFunceble following the following formats:

- plain text file

<script async id="asciicast-rOKnzpYgss7tKwd8s3t7tv22v" src="https://asciinema.org/a/rOKnzpYgss7tKwd8s3t7tv22v.js"></script>
