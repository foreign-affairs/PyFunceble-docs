# Custom User-Agent

## Why do we need it?

As we need to be one in a middle of a connection to a webserver, the custom
user agent is there for that!

## How does it work?

We set the user-agent every time we request something with the `http`
and `https` protocols.

If a custom user agent is given, it will be used.

Otherwise, every 24 hours, we update our [user-agents.json][UA] file
which will be fetched by your local version to determine the user-agent to use.

## How to use it?

Simply choose your browser and platform or provide us your custom one!

```yaml
  user_agent:
    browser: chrome
    platform: linux
    custom: null
```

into your personal `.PyFunceble.yaml` or use the `--user-agent`
(custom UA) argument from the CLI.

### Available Browser

Here is a list of available and accepted browsers at this time.

* `chrome`
* `edge`
* `firefox`
* `ie`
* `opera`
* `safari`

### Available Platform

Here is a list of available and accepted platform at this time.

* `linux`
* `macosx`
* `win10`

## What if we don't give a custom User-Agent?

If you don't set a custom User-Agent, we will try to get the latest one for the chosen
browser and platform.


[UA]: https://raw.githubusercontent.com/PyFunceble/user_agents/master/user_agents.json
