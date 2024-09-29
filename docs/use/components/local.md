# Test in/for local hostnames, IPs, components

!!! info "Default status"

    This component is not activate by default.

## Why do we need it?

As we may need to test for local hostnames, IPs, components in a local network,
this component allows a less aggressive way of syntax validation.

## How does it work?

We simply use a less aggressive syntax validation so that everything you give
us is being tested.

## How to use it?

Simply change

```yaml
   cli_testing:
      # Acknowleadges that we may test for local network component.
      # NOTE: Activating this, will remove the syntax checker completely.
      local_network: False
```

to

```yaml
   cli_testing:
      # Acknowleadges that we may test for local network component.
      # NOTE: Activating this, will remove the syntax checker completely.
      local_network: True
```

into your personal `.PyFunceble.overwrite,yaml` or use the :code:`--local` argument
from the CLI to activate it.
