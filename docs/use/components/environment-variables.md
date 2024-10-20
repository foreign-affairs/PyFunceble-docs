# Environment variables

## Dotenv files

Since PyFunceble `2.0.0` (equivalent of PyFunceble-dev `>=1.18.0`), we load
(thanks to [python-dotenv][python-dotenv]) the content of the following files
into the (local) list of environment variables.

1. `.env` (current directory)
2. `.pyfunceble-env` (current directory)
3. `.env` (configuration directory)
4. `.pyfunceble-env` (configuration directory)

To quote the [python-dotenv][python-dotenv] documentation, a `.env` should look
like the following:

```python
# a comment and that will be ignored.
REDIS_ADDRESS=localhost:6379
MEANING_OF_LIFE=42
MULTILINE_VAR="hello\nworld"
```


## What do we use and why ?

Here is the list of environment variables we use and how we use them if they
are set.

[//]: # (TODO: Add ref links in table to right docs)

| **Environment Variable**        | **How do we use it?**                                                                                       |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------- |
| `DEBUG_PYFUNCEBLE`              | Same as `PYFUNCEBLE_DEBUG` it's just present for retro-compatibility.                                       |
| `DEBUG_PYFUNCEBLE_ON_SCREEN`    | Same as `PYFUNCEBLE_DEBUG_ON_SCREEN` it's just present for retro-compatibility.                             |
| `PYFUNCEBLE_AUTO_CONFIGURATION` | Tell us if we have to install/update the configuration file automatically.                                  |
| `PYFUNCEBLE_DB_CHARSET`         | Tell us the database charset or encoding to use.                                                            |
| `PYFUNCEBLE_DB_HOST`            | Tell us the host or the Unix socket (absolute path) of the database.                                        |
| `PYFUNCEBLE_DB_NAME`            | Tell us the name of the database to use.                                                                    |
| `PYFUNCEBLE_DB_PASSWORD`        | Tell us the database user password to use.                                                                  |
| `PYFUNCEBLE_DB_PORT`            | Tell us the database connection port to use.                                                                |
| `PYFUNCEBLE_DB_USERNAME`        | Tell us the database user-name to use.                                                                      |
| `PYFUNCEBLE_DEBUG`              | Tell us to log everything into the `output/logs/*.log` files.                                               |
| `PYFUNCEBLE_DEBUG_LVL`          | Sets the logging level to use.                                                                              |
| `PYFUNCEBLE_LOGGING_LVL`        | Same as `PYFUNCEBLE_DEBUG_LVL`.                                                                             |
| `PYFUNCEBLE_DEBUG_ON_SCREEN`    | Tell us to log everything to `stdout`                                                                       |
| `PYFUNCEBLE_CONFIG_DIR`         | Tell us the location of the directory to use as the configuration directory.                                |
| `PYFUNCEBLE_OUTPUT_DIR`         | Same as `PYFUNCEBLE_CONFIG_DIR` it's just present for retro-compatibility.                                  |
| `PYFUNCEBLE_OUTPUT_LOCATION`    | Tell us where we should generate the `output/` directory.                                                   |
| `APPDATA`                       | Used under Windows to construct/get the configuration directory if `PYFUNCEBLE_CONFIG_DIR` is not found.    |
| `GH_TOKEN`                      | Tell us the GitHub token to set into the repository configuration when using PyFunceble under Travis CI.    |
| `GL_TOKEN`                      | Tell us the GitLab token to set into the repository configuration when using PyFunceble under GitLab CI/CD. |
| `GIT_EMAIL`                     | Tell us the `git.email` configuration to set when using PyFunceble under any supported CI environment.      |
| `GIT_NAME`                      | Tell us the `git.name` configuration to set when using PyFunceble under any supported CI environment.       |
| `TRAVIS_BUILD_DIR`              | Used to confirm that we are running under a Travis CI container.                                            |
| `GITLAB_CI`                     | Used to confirm that we are running under a GitLab CI/CD environment.                                       |
| `GITLAB_USER_ID`                | Used to confirm that we are running under a GitLab CI/CD environment.                                       |

[python-dotenv]: https://github.com/theskumar/python-dotenv
