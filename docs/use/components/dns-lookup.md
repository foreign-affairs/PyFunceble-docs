# DNS Lookup

## Why do we need it?

As our main purpose is to check the availability of the given subjects, we make
a DNS lookup to determine its availability.

## How does it work?

### For domains

In order:

1. Request the `NS` record.
2. If not found, request the `A` record.
3. If not found, request the `AAAA` record.
4. If not found, request the `CNAME` record.
5. If not found, request the `DNAME` record.

!!! note "Note"

    If none is found, we call the UNIX/C equivalent of `getaddrinfo()`.

### For IP

We request the `PTR` record for the IP.

!!! note "Note"

    If none is found, we call the UNIX/C equivalent of `gethostbyaddr()`
    or `getaddrinfo()`.


## How to use it?

It is activate by default. If it is not the case, please simply set
this value in your `.PyFunceble.overwrite,yaml`

```yaml
    lookup:
        # Activates the usage of the DNS lookup.
        dns: False
```

to

```yaml
    lookup:
        # Activates the usage of the DNS lookup.
        dns: True
```

into your personal `.PyFunceble.yaml` or use the `--no-whois`
argument from the CLI to reactivate it.
