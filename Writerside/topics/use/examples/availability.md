# Availability Check

PyFunceble can check the availability of domains and IPs.

For IP testing several formats are supported as well as both IPv4 and IPv6.

## Input methode

### Inline - CLI

#### Domain testing {id="domain-testing_cli"}
You can check the availability of a domain or IP, by running PyFunceble with the `-d` argument.

```Bash
pyfunceble -d example.net
```

The `-d` argument can also take multiple domains to test.

```Bash
pyfunceble -d example.net example.org example.com 192.0.2.4
```

<script async id="asciicast-DeyvkADk8zCm51Sxo7iinNOk3" src="https://asciinema.org/a/DeyvkADk8zCm51Sxo7iinNOk3.js"></script>

#### URI testing {id="uri-testing_cli"}

You can check the availability of a URL through the `-u` argument of PyFunceble.

```Bash
pyfunceble -u https://github.com/pyfunceble
```

That `-u` argument can also take multiple URLs to test.

```Bash
pyfunceble -u https://github.com/pyfunceble https://gitlab.com/funilrys https://gitea.com
```

<script async id="asciicast-HyVGobPUHiPq2PPh5Krr0ilhh" src="https://asciinema.org/a/HyVGobPUHiPq2PPh5Krr0ilhh.js"></script>


### File

#### Domain testing {id="domain-testing_file"}

You can check the availability of the domains or IPs located inside a file, by giving the file path(s) to PyFunceble through the `-f` argument.

```Bash
pyfunceble -f ./source.list
pyfunceble -f https://example.org/my/awesome/file
```

When using the `-f` argument, the inputted source can be:

- any file-s on your filesystem accessible by the user running PyFunceble.
- an HTTP (raw) URLs of the file you want PyFunceble to download and check.

When testing for the availability of domains or IPs, PyFunceble supports the following file formats:

- hosts file
- plain text file
- AdBlock filter list (please use with the `--adblock` argument)
- RPZ (formatted) file (please use with the `--rpz` argument)

<script async id="asciicast-JIPgxiZgueGiD2wI1FvuRQJyx" src="https://asciinema.org/a/JIPgxiZgueGiD2wI1FvuRQJyx.js"></script>

## URLs Availability

PyFunceble can check the availability of URLs.

#### URI testing {id="uri-testing_file"}

You can check the availability of the URLs located inside a file, by giving the file path(s) to PyFunceble through the `-uf` argument.

```Bash
pyfunceble -uf ./source.url.list
pyfunceble -uf https://example.org/my/awesome/file
```

Just like the `-f` argument, when using the `-uf` argument, the inputted source can be:

- any file-s on your filesystem accessible by the user running PyFunceble.
- an HTTP (raw) URL-s of the file you want PyFunceble to download and check.

When testing the availability of URLs, PyFunceble following the following formats:

- plain text file

<script async id="asciicast-6EQeyFdgeA4CHZlbsWMZqkKeS" src="https://asciinema.org/a/6EQeyFdgeA4CHZlbsWMZqkKeS.js"></script>


Todo
    Complete rewrite of this file for reordering and sorting by URI / DOMAIN rather than input source 