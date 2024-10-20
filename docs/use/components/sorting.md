
# Sorting

!!! note "Note"

    While using the multiprocessing option, the data are tested as given.

## Why do we need it?

Because sorted is better, we sort by default!

## How does it work?

!!! note "Note"

    Want to read the code ? It's here:
    :func:`~PyFunceble.cli.utils.sort.standard`
    and
    :func:`~PyFunceble.cli.utils.sort.hierarchical`!

### Alphabetically

This is the default one. The :func:`~PyFunceble.cli.utils.sort.standard`
function is used for that purpose.

### Hierarchically

The objective of this is to provide sorting by service/domains.

The :func:`~PyFunceble.cli.utils.sort.hierarchical`
function is used for that purpose.

!!! note "Note"
    This is a simplified version of what we do.

1. Let's say we have `aaa.bbb.ccc.tld`.
    !!! note "Note"
        The TLD part is determined. Indeed, we first look at the
        IANA Root Zone database, then at the Public Suffix List.

2. Let's split the points. We then get a list `[aaa, bbb, ccc, tld]`
3. Put the tld first. It will give us `[tld, aaa, bbb, ccc]`
4. Reverse everything after the tld. It will give us `[tld, ccc, bbb, aaa]`.
5. Get the string to use for sorting. It will give us `tld.ccc.bbb.aaa`.


### How to activate the hierarchical sorting?

Simply change

```yaml
  cli_testing:
    sorting_mode:
      # Activates the hierarchical sorting.
      hierarchical: False
```

to

```yaml
  cli_testing:
    sorting_mode:
      # Activates the hierarchical sorting.
      hierarchical: True
```

into your personal `.PyFunceble.overwrite,yaml` or use the `--hierarchical`
argument from the CLI to activate it.
