# AdBlock/Filter list decoding


!!! info "Default status"

    This component is not activate by default.

## Why do we need it?


As some people may want to test the content of their AdBlock/Filter list, we
offer a way to decode them!

We keep it simple by trying to comply with the Adblock Plus filters explained
documentation. For us, the relevant parts are the one which defines/explains
which domains are being blocked from a given rule.

## How does it work?

!!! info "Info"

    Want to read the code ? It's here:
    :class:`~PyFunceble.converter.adblock_input_line2subject.AdblockInputLine2Subject`!

We keep it simple by trying to comply with the
[Adblock Plus filters explained][AP] documentation.
For us, the relevant parts are the one which defines/explains which domains
are being blocked from a given rule.

!!! note "note"

    A more aggressive extraction might be planned in the future.


## How to use it?

You can simply change

```yaml
cli_decoding:
    adblock: False

    # Activate this only if you want to get as much as possible.
    aggressive: False
```

to

```yaml
cli_decoding:
    adblock: True

    # Activate this only if you want to get as much as possible.
    aggressive: False
```

into your personal `.PyFunceble.yaml` or use the `--adblock` argument from
the CLI to activate it.


[AP]: https://adblockplus.org/filter-cheatsheet "Adblock Plus filters explained"
