# Databases

## Why do we use "databases"?

We use databases to store data while we run the tests. When globally talking
about databases, we are indirectly talking about the following subsystems.

* Autocontinue
* InactiveDB
* WhoisDB

## How do we manage them?

They consist of simple CSV files which are read and updated on the fly.

## Warnings around Database (self) management

!!! warning "Warning"

    If you plan to delete everything and still manage to use PyFunceble in the
    future, please use the `clean-pyfunceble` CLI.

    Indeed, it will delete everything that we generated,
    except the things like the WHOIS database file/table which saves (almost)
    static data which should be reused in the future.

    Deleting, for example, the WHOIS database file/table will just make
    your test run for a much longer time if you retest subject that used to be
    indexed into the whois database file/table.

## Databases types

Since PyFunceble `2.0.0` (equivalent of `>=1.18.0.dev`),
we offer multiple database types which are (as per configuration) `csv`
(default since `4.0.0`), `mariadb`, `mysql` and `postgresql`.

### Why different database types?

With the introduction of the multiprocessing logic, it became natural to
introduce other database formats.

### How to use the `mysql` or `mariadb` format?

1. Create a new user, password and database (optional) for PyFunceble to work
   with.

2. Create a `.pyfunceble-env` file at the root of your configuration
   directory.

3. Complete it with the following content (example)

    ```ini
    PYFUNCEBLE_DB_CHARSET=utf8mb4
    PYFUNCEBLE_DB_HOST=localhost
    PYFUNCEBLE_DB_NAME=PyFunceble
    PYFUNCEBLE_DB_PASSWORD=Hello,World!
    PYFUNCEBLE_DB_PORT=3306
    PYFUNCEBLE_DB_USERNAME=pyfunceble
    ```

    Since version `2.4.3.dev` it is possible to use the UNIX socket
    for the `PYFUNCEBLE_DB_HOST` environment variable.

    The typical location for `mysqld.sock` is
    `/var/run/mysqld/mysqld.sock`.

    This have been done to make

    1. It easier to use the `socket` in conjunction with a supported CI
    environment/platform.

    2. Leaving more space on the IP-stack on local DB installations.

    3. The `UNIX:SOCKET` is usually faster than the IP connection on
    local runs.

    ```ini
    PYFUNCEBLE_DB_CHARSET=utf8mb4
    PYFUNCEBLE_DB_HOST=/var/run/mysqld/mysqld.sock
    PYFUNCEBLE_DB_NAME=PyFunceble
    PYFUNCEBLE_DB_PASSWORD=Hello,World!
    PYFUNCEBLE_DB_PORT=3306
    PYFUNCEBLE_DB_USERNAME=pyfunceble
    ```

4. Switch the `db_type` index of your configuration file to `mysql` or `mariadb`.

5. Play with PyFunceble!

!!! note "Note"

    If the environment variables are not found, you will be asked to prompt the
    information.


### How to use the `postgresql` format?

1. Create a new user, password and database (optional) for PyFunceble to work
   in.

2. Create a `.pyfunceble-env` file at the root of your configuration
   directory.

3. Complete it with the following content (example)

    ```ini
    PYFUNCEBLE_DB_CHARSET=utf8
    PYFUNCEBLE_DB_HOST=localhost
    PYFUNCEBLE_DB_NAME=PyFunceble
    PYFUNCEBLE_DB_PASSWORD=Hello,World!
    PYFUNCEBLE_DB_PORT=5432
    PYFUNCEBLE_DB_USERNAME=pyfunceble
    ```

    Since version `2.4.3.dev` it is possible to use the UNIX socket
    for the `PYFUNCEBLE_DB_HOST` environment variable.

    The typical location for `s.PGSQL.5432` is `/var/run/postgresql`.

    This have been done to make

    1. It easier to use the `socket` in conjunction with a supported CI
       environment/platform.

    2. Leaving more space on the IP-stack on local DB installations.

    3. The `UNIX:SOCKET` which usually is faster than the IP connection on
       local runs.

    ```ini
    PYFUNCEBLE_DB_CHARSET=utf8
    PYFUNCEBLE_DB_HOST=/var/run/postgresql
    PYFUNCEBLE_DB_NAME=PyFunceble
    PYFUNCEBLE_DB_PASSWORD=Hello,World!
    PYFUNCEBLE_DB_PORT=5432
    PYFUNCEBLE_DB_USERNAME=pyfunceble
    ```

4. Switch the `db_type` index of your configuration file to `postgresql`.

5. Play with PyFunceble!

!!! note "Note"

    If the environment variables are not found, you will be asked to prompt the
    information.
