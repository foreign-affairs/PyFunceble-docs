# Complements Generation

!!! info "Default status"

    This component is not activate by default.

## Why do we need it?

Let's say we have `example.org` while `www.example.org`
(or vice-versa) are not into your list.<br>
This component (if activated) will test both `example.org` and
`www.example.org`, even if it's not into the input list.

## How does it work?

!!! note "Note"
    Want to read the code ? It's here
    :class:`~PyFunceble.converter.subject2complements.Subject2Complements`!

At the end of the normal test process, we generate the list of complements and
test them.

## How to use it?

You can simply change

```yaml
  cli_testing:
    # Activates the generation of complements.
    complements: False
```

to

```yaml
  cli_testing:
    # Activates the generation of complements.
    complements: True
```

into your personal `.PyFunceble.yaml` or use the `--complements`
argument from the CLI to activate it.
