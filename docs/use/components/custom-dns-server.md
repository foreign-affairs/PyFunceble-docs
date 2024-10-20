# Custom DNS Server

!!! versionadded:: 3.3.0

## Why do we need it?

Our testing tool may sometime use a DNS-server which isn't
suited for PyFunceble. This could by example be your own DNS-Firewall.

To avoid these situations, the program allows you to setup the DNS-Server that
we need to use.

## How does it work?

!!! note "note"

    Want to read the DNS query tool source code ?
    It's here :class:`~PyFunceble.query.dns.query_tool.DNSQueryTool`!

What we do is that we parse and use your given server.

## How to use it?

By default, PyFunceble will use the system-wide DNS settings. This can be
changed with the ability to configure which DNS-Servers you like PyFunceble to
use during the test.

You set this up with the CLI command `--dns` **or** insert it into your
`.PyFunceble.overwrite,yaml`

```yaml
  dns:
    server: null
```

to

```yaml
  dns:
    server:
    - 9.9.9.10
    - 149.112.112.10
```

!!! versionchanged:: 3.0.0

It is now possible to assign a specific port to use with the DNS-Server.

If you don't append a port number, the default DNS port (53) will be used.

```bash
pyfunceble --dns 9.9.9.10 149.112.112.10 -f $DOMAIN_FILE
```
