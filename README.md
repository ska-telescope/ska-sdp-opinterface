# SDP Operator Interface

This package contains the prototype operator interface to monitor and control the SKA SDP.

The current implementation is based on the Python Flask module and shows the basic capabilities of

- Displaying the current contents of the SDP Configuration library in a textual format

- Similar to the above but with a tree view - where nodes in the tree can be expanded and connected to additional display features.

- A simple example of creating new entries in the Configuration database

## Standard CI machinery

This repository is set up to use the
[Makefiles](https://gitlab.com/ska-telescope/sdi/ska-cicd-makefile) and [CI
jobs](https://gitlab.com/ska-telescope/templates-repository) maintained by the
System Team. For any questions, please look at the documentation in those
repositories or ask for support on Slack in the #team-system-support channel.

To keep the Makefiles up to date in this repository, follow the instructions
at: https://gitlab.com/ska-telescope/sdi/ska-cicd-makefile#keeping-up-to-date

## Contributing to this repository

[Black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/),
and various linting tools are used to keep the Python code in good shape.
Please check that your code follows the formatting rules before committing it
to the repository. You can apply Black and isort to the code with:

```bash
make python-format
```

and you can run the linting checks locally using:

```bash
make python-lint
```

The linting job in the CI pipeline does the same checks, and it will fail if
the code does not pass all of them.

## Creating a new release

When you are ready to make a new release:

  - Check out the master branch
  - Update the version number in `.release` with
    - `make bump-patch-release`,
    - `make bump-minor-release`, or
    - `make bump-major-release`
  - Set the Python package version number with `make python-set-release`
  - Manually update the version numbers in
    - `docs/src/conf.py`
  - Update the `CHANGELOG.md` and add the right version number
  - Use your working JIRA ticket when the ticket number is asked for
  - Create the git tag with `make git-create-tag`
  - Push the changes with `make git-push-tag`
