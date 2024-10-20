# Execution time

!!! info "Default status"

    This component is not activate by default.

## Why do we need it?

As it is always nice to see how long we worked, we added this logic!

## How does it work?

!!! note "Note"

    Want to read the code ? It's here
    :class:`PyFunceble.cli.execution_time.ExecutionTime`!

It shows the execution time on screen (`stdout`).

## How to use it?

You can simply change

```yaml
  display_mode:
    # Activates the printing of the execution time.
    execution_time: False
```

to

```yaml
  display_mode:
    # Activates the printing of the execution time.
    execution_time: True
```

into your personal `.PyFunceble.yaml` or use the `--execution`
argument from the CLI to activate it.
