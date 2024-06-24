# Update

Updating PyFunceble is as easy as the installation.

## Overview: Update Method

| OS        | Technology                  | Tools        | Link                                 |
|-----------|-----------------------------|--------------|--------------------------------------|
| Any       | PyPi - Python Package Index | `pip3`       | [Link](#pypi---python-package-index) |
| Any       | Container Image Registry    | `docker`     | [Link](#container-image-registry)    |
| Any       | Git                         | `pip3`       | [Link](#git-repository)              |
| Any       | Zip File                    | `pip3`       | [Link](#from-source)                 |
| ArchLinux | AUR Helper                  | `aur-helper` | [Link](#arch-linux)                  |

## PyPi - Python Package Index

Updating a `pip` installed package is straight forward. Just append `--upgrade`
to you installation command and you are good to go.

Here is an overview of the packages and where they are hosted.

| Package        | PyPi Link                                                                       |
|----------------|---------------------------------------------------------------------------------|
| pyfunceble     | [https://pypi.org/project/PyFunceble](https://pypi.org/project/PyFunceble)      |
| pyfunceble-dev | [https://pypi.org/project/PyFunceblee-dev](https://pypi.org/project/PyFunceble) |

!!! danger "Beware!!"

    We recommend the usage of the `--user` flag as it installs the required
    dependencies at the user level. The main reason behind that is to avoid
    crashes or clashes between you OS package manager and `pip3`.

    However, if you:

    - are aware of the possible consequences
    - are running PyFunceble within a CI engine or in an automated environment

    you shouldn't use it.

### pyfunceble

You can update the **pyfunceble** through `pip3`:

```shell
pip3 install --user --upgrade pyfunceble
```

### pyfunceble-dev

You can update the  **pyfunceble-dev** package through `pip3`:

```shell
pip3 install --user --upgrade pyfunceble-dev
```

If you want to help and use the unstable pre-releases, you should update with
the `--pre` argument.

```shell
pip3 install --user --pre --upgrade pyfunceble-dev
```

## Container Image Registry

Updating from a Container Image Registry is easier. If you allowed your
container engine to automatically pull the `latest` tag, you have nothing
to do. The new layers are downloaded before you run PyFunceble.

Here is an overview of the packages and where they are hosted.

| Host       | Package        | Link                                                                                                     |
|------------|----------------|----------------------------------------------------------------------------------------------------------|
| Docker Hub | pyfunceble     | [https://hub.docker.com/r/pyfunceble/pyfunceble](https://hub.docker.com/r/pyfunceble/pyfunceble)         |
| Docker Hub | pyfunceble-dev | [https://hub.docker.com/r/pyfunceble/pyfunceble-dev](https://hub.docker.com/r/pyfunceble/pyfunceble-dev) |

## Arch Linux

Updating from the ArchLinux User Repository is straight forward.

Here is an overview of the packages and where they are hosted.

| Package        | AUR Link                                                                                               |
|----------------|--------------------------------------------------------------------------------------------------------|
| pyfunceble     | [https://aur.archlinux.org/packages/pyfunceble](https://aur.archlinux.org/packages/pyfunceble)         |
| pyfunceble-dev | [https://aur.archlinux.org/packages/pyfunceble-dev](https://aur.archlinux.org/packages/pyfunceble-dev) |

### pyfunceble

#### AUR Helper

You can update the **pyfunceble** package through your favorite AUR helper:

```shell
aur-helper -Syu pyfunceble
```

#### Manually

You can update the **pyfunceble** package manually through the following:

```shell
git clone https://aur.archlinux.org/pyfunceble.git pyfunceble
cd pyfunceble
makepkg -fsri
```

### pyfunceble-dev

#### AUR Helper

You can update the **pyfunceble-dev** package through your favorite AUR helper:

```shell
aur-helper -Syu pyfunceble-dev
```

#### Manually

You can update the **pyfunceble** package manually through the following:

```shell
git clone https://aur.archlinux.org/pyfunceble-dev.git pyfunceble-dev
cd pyfunceble-dev
makepkg -fsri
```

## Git Repository

Updating from the Git Repository with `pip3` is just like a normal update
of `pip` installed package. Just add `--upgrade` to your installation
command and you are good to go.

Here is an overview of the packages and where they are hosted.

| Host   | Package        | Repository                                                              |
|--------|----------------|-------------------------------------------------------------------------|
| GitHub | pyfunceble     | `git+https://github.com/funilrys/PyFunceble.git@master#egg=PyFunceble`  |
| GitHub | pyfunceble-dev | `git+https://github.com/funilrys/PyFunceble.git@dev#egg=PyFunceble-dev` |
| GitLab | pyfunceble     | `git+https://gitlab.com/funilrys/PyFunceble.git@master#egg=PyFunceble`  |
| GitLab | pyfunceble-dev | `git+https://gitlab.com/funilrys/PyFunceble.git@dev#egg=PyFunceble-dev` |

!!! danger "Beware!!"

    We recommend the usage of the `--user` flag as it installs the required
    dependencies at the user level. The main reason behind that is to avoid
    crashes or clashes between you OS package manager and `pip3`.

    However, if you:

    - are aware of the possible consequences
    - are running PyFunceble within a CI engine or in an automated environment

    you shouldn't use it.

### pyfunceble

#### GitHub

You can update the **pyfunceble** package from GitHub through `pip3`:

```shell
pip3 install --user --upgrade git+https://github.com/funilrys/PyFunceble.git@master#egg=PyFunceble
```

#### GitLab

You can update the **pyfunceble** package from GitLab through `pip3`:

```shell
pip3 install --user --upgrade git+https://gitlab.com/funilrys/PyFunceble.git@master#egg=PyFunceble
```

### pyfunceble-dev

#### GitHub

You can update the **pyfunceble-dev** package from GitHub through `pip3`:

```shell
pip3 install --user --upgrade git+https://github.com/funilrys/PyFunceble.git@dev#egg=PyFunceble-dev
```

#### GitLab

You can update the **pyfunceble-dev** package from GitLab through `pip3`:

```shell
pip3 install --user --upgrade git+https://gitlab.com/funilrys/PyFunceble.git@dev#egg=PyFunceble-dev
```

## From Source

Updating from the source with `pip3` is just like a normal update of `pip`
installed package. Just add `--upgrade` to your installation command and
you are good to go.

Here is an overview of the packages and where they are hosted.

| Host   | Package        | Branch   | Repository                                                                                               |
|--------|----------------|----------|----------------------------------------------------------------------------------------------------------|
| GitHub | pyfunceble     | `master` | [https://github.com/funilrys/PyFunceble/tree/master](https://github.com/funilrys/PyFunceble/tree/master) |
| GitHub | pyfunceble-dev | `dev`    | [https://github.com/funilrys/PyFunceble/tree/dev](https://github.com/funilrys/PyFunceble/tree/dev)       |
| GitLab | pyfunceble     | `master` | [https://gitlab.com/funilrys/PyFunceble/tree/master](https://gitlab.com/funilrys/PyFunceble/tree/master) |
| GitLab | pyfunceble-dev | `dev`    | [https://gitlab.com/funilrys/PyFunceble/tree/master](https://gitlab.com/funilrys/PyFunceble/tree/master) |

You can install the package from source through `pip3`:

```shell
# From Github
pip3 install --upgrade --user https://github.com/funilrys/PyFunceble/archive/{{branch}}.zip

# From GitLab
pip3 install --upgrade --user https://gitlab.com/funilrys/PyFunceble/-/archive/{{branch}}/PyFunceble-{{branch}}.zip
```
