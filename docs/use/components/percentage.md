#Percentage

!!! info "Default status"

    This component is not activate by default.

!!! info "Information"
    The percentage doesn't show up - by design - while testing for single
    subjects.


## Why do we need it?

We need it in order to get information about the amount of data we just tested.

## How does it work?

!!! note ""
    Want to read the code ? It's here
    :class:`~PyFunceble.cli.filesystem.counter.FilesystemCounter`!

Regularly or at the very end of a test we get the number of subjects for
each status along with the number of tested subjects.
We then generate and print the percentage calculation on the screen
(`stdout`) and into
`output/${input_file_name}/logs/percentage/percentage.txt`

## How to use it?

It is activated by default, but if not please update

```yaml
  cli_testing:
    display_mode:
      # Activates the output of the percentage information.
      percentage: False
```

to

```yaml
  cli_testing:
    display_mode:
      # Activates the output of the percentage information.
      percentage: True
```

into your personal `.PyFunceble.yaml` or use the `--percentage`
argument from the CLI to reactivate it.
