# Outputted Files

!!! note "Note"

    This section does not cover the log files.

## Why do we need it?

We need a way to deliver our results.

## How does it work?

After testing a given subject, we generate its output file based on what's
needed.

### Host format

This is the default output file.

A line is formatted like `0.0.0.0 example.org`.

!!! note "Note"
    A custom IP can be set with the help of the `custom_ip` index or the
    `--hosts-ip` argument from the CLI.

Don't need it? Simply change

```yaml
  cli_testing:
    file_generation:
      # Activates the generation of the hosts file(s).
      hosts: False
```

to

```yaml
  cli_testing:
    file_generation:
      # Activates the generation of the hosts file(s).
      hosts: False
```

into your personal `.PyFunceble.yaml` or use the `--hosts` argument
from the CLI to deactivate it.


### Plain format

A line is formatted like `example.org`.

Need it? Simply change

```yaml
  cli_testing:
    file_generation:
      # Activates the generation of the plain (or raw) file(s).
      plain: False
```

to

```yaml
  cli_testing:
    file_generation:
      # Activates the generation of the plain (or raw) file(s).
      plain: True
```

into your personal `.PyFunceble.yaml` or use the `--plain` argument
from the CLI to activate it.
