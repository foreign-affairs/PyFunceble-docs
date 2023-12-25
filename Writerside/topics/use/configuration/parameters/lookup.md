# lookup

To lookup or not lookup, that is the question!

## Overview

```yaml
lookup:
  # Provides everything related to the lookup.

  # Enable/Disable the usage of DNS records to look up the status.
  #
  # CLI Argument: --dns-lookup
  # Exclusive CLI Argument: --dns-lookup-only
  dns: yes

  # Enable/Disable the usage of HTTP status codes to look up the status.
  #
  # CLI Argument: --http | --http-status-code-lookup
  # Exclusive CLI Argument: --http-only | --http-status-code-lookup
  http_status_code: yes

  # Enable/Disable the usage of network (information) socket to look up the status.
  #
  # CLI Argument: --netinfo-lookup
  # Exclusive CLI Argument: --netinfo-lookup-only
  netinfo: yes

  # Enable/Disable the usage of special rules to look up or switch the status.
  #
  # CLI Argument: --special-lookup
  # Exclusive CLI Argument: --special-lookup-only
  special: yes

  # Enable/Disable the usage of WHOIS records to look up the status.
  #
  # CLI Argument: --whois-lookup
  # Exclusive CLI Argument: --whois-lookup-only
  whois: yes

  # Enable/Disable the usage of the reputation data to look up the status.
  #
  # NOTE:
  #     The reputation lookup is actualy a lookup against the AlienVault IPv4
  #     reputation file.s
  #
  # CLI Argument: --reputation-lookup
  # Exclusive CLI Argument: --reputation-lookup
  reputation: no

  # Enable/Disable the usage of the collection (API) to look up the status.
  #
  # CLI Argument: --collection-lookup
  # Exclusive CLI Argument: --collection-lookup-only
  collection: no

  # Set the timeout to apply to each of our lookup methods - when possible.
  #
  # WARNING:
  #     This should be a value >= 0.
  #
  # CLI Argument: -t | --timeout
  timeout: 5
```
{collapsible="true" default-state="collapsed" collapsed-title="Provides everything related to the lookup." validate="false"}

### html style code
<code-block lang="yaml" collapsible="true" default-state="collapsed"
    collapsed-title="Provides everything related to the lookup." id="lookup2" validate="false">
<![CDATA[
lookup:
  # Provides everything related to the lookup.

  # Enable/Disable the usage of DNS records to look up the status.
  #
  # CLI Argument: --dns-lookup
  # Exclusive CLI Argument: --dns-lookup-only
  dns: yes

  # Enable/Disable the usage of HTTP status codes to look up the status.
  #
  # CLI Argument: --http | --http-status-code-lookup
  # Exclusive CLI Argument: --http-only | --http-status-code-lookup
  http_status_code: yes

  # Enable/Disable the usage of network (information) socket to look up the status.
  #
  # CLI Argument: --netinfo-lookup
  # Exclusive CLI Argument: --netinfo-lookup-only
  netinfo: yes

  # Enable/Disable the usage of special rules to look up or switch the status.
  #
  # CLI Argument: --special-lookup
  # Exclusive CLI Argument: --special-lookup-only
  special: yes

  # Enable/Disable the usage of WHOIS records to look up the status.
  #
  # CLI Argument: --whois-lookup
  # Exclusive CLI Argument: --whois-lookup-only
  whois: yes

  # Enable/Disable the usage of the reputation data to look up the status.
  #
  # NOTE:
  #     The reputation lookup is actualy a lookup against the AlienVault IPv4
  #     reputation file.s
  #
  # CLI Argument: --reputation-lookup
  # Exclusive CLI Argument: --reputation-lookup
  reputation: no

  # Enable/Disable the usage of the collection (API) to look up the status.
  #
  # CLI Argument: --collection-lookup
  # Exclusive CLI Argument: --collection-lookup-only
  collection: no

  # Set the timeout to apply to each of our lookup methods - when possible.
  #
  # WARNING:
  #     This should be a value >= 0.
  #
  # CLI Argument: -t | --timeout
  timeout: 5
]]>
</code-block>

### html import snippet line 1-7

<code-block lang="yaml" src="PyFunceble.overwrite.yaml" include-lines="1-7" id="lookup3">

</code-block>

## dns

Enable or disable the usage of DNS records to look up the status.

| Type:                   | boolean             |
|-------------------------|---------------------|
| Default Value:          | `no`                |
| Available Values:       | `yes`, `no`         |
| CLI Argument:           | `--dns-lookup`      |
| Exclusive CLI Argument: | `--dns-lookup-only` |


## http_status_code

Enable or disable the usage of HTTP status codes to look up the status.

| Type:                   | boolean                                         |
|-------------------------|-------------------------------------------------|
| Default Value:          | `no`                                            |
| Available Values:       | `yes`, `no`                                     |
| CLI Argument:           | `--http-only`, `--http-status-code-lookup`      |
| Exclusive CLI Argument: | `--http-only`, `--http-status-code-lookup-only` |


## netinfo

Enable or disable the usage of network (information) socket to look up the status.

| Type:                   | boolean                 |
|-------------------------|-------------------------|
| Default Value:          | `no`                    |
| Available Values:       | `yes`, `no`             |
| CLI Argument:           | `--netinfo-lookup`      |
| Exclusive CLI Argument: | `--netinfo-lookup-only` |


## special

Enable or disable the usage of special rules to look up or switch the status.

| Type:                   | boolean                 |
|-------------------------|-------------------------|
| Default Value:          | `no`                    |
| Available Values:       | `yes`, `no`             |
| CLI Argument:           | `--special-lookup`      |
| Exclusive CLI Argument: | `--special-lookup-only` |


## whois

Enable or disable the usage of <tooltip term="WHOIS">WHOIS</tooltip> records to look up the status.

| Type:                   | boolean               |
|-------------------------|-----------------------|
| Default Value:          | `no`                  |
| Available Values:       | `yes`, `no`           |
| CLI Argument:           | `--whois-lookup`      |
| Exclusive CLI Argument: | `--whois-lookup-only` |


## reputation {id=reputation}

Enable or disable the usage of reputation data to look up the status.

| Type:                   | boolean                    |
|-------------------------|----------------------------|
| Default Value:          | `no`                       |
| Available Values:       | `yes`, `no`                |
| CLI Argument:           | `--reputation-lookup`      |
| Exclusive CLI Argument: | `--reputation-lookup-only` |


## collection {id=collection}

Enable or disable the usage of the collection (API) to look up the status.

| Type:                   | boolean                    |
|-------------------------|----------------------------|
| Default Value:          | `no`                       |
| Available Values:       | `yes`, `no`                |
| CLI Argument:           | `--collection-lookup`      |
| Exclusive CLI Argument: | `--collection-lookup-only` |


## timeout {id=timeput}

Set the timeout to apply to each of our lookup methods - when possible.

<table style="header-column">
    <tr>
        <td width="30%">Type:</td>
        <td>integer</td>
    </tr>
    <tr>
        <td>Default Value:</td>
        <td><code>`5`</code></td>
    </tr>
    <tr>
        <td>Available Values:</td>
        <td>Any value greater <code>&gt;</code> that <code>0</code></td>
    </tr>
    <tr>
        <td>CLI Argument:</td>
        <td><code>`-t`</code>, <code>`--timeout`</code></td>
    </tr>
</table>



<deflist type="wide" default-state="collapsed" title="DNS test timeout">
    <def title="Type">
            integer
    </def>
    <def title="Default Value">
            `5`
    </def>
    <def title="Available Values">
            Any value greater `>` that `0`
    </def>
    <def title="CLI Argument">
            `-t`, `--timeout`
    </def>
</deflist>
