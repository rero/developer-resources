# Git

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## Configuration

Set user name and email for signed message:

```bash
git config --global user.name "John Doe"               # set username for all git projects
git config --global user.email johndoe@example.com     # set email for all git projects
```

## Main Commands

Basic commands:

```bash
git clone <repository>   # get a local copy of a git project
git commit -s -a         # commit all changes with a signature
git pull                 # get all changes from a remote repository
git push                 # push all change to a remote repository
git log                  # show commit logs
```

## Git Commit Guidelines

We have very precise rules over how our git commit messages can be formatted. This leads to **more
readable messages** that are easy to follow when looking through the **project history**.

The commit message formatting can be added using a typical git workflow.

### Commit Message Format

See [Contributing guide > Commit message style](https://github.com/rero/rero-ils/blob/staging/CONTRIBUTING.rst#commit-message-style)

## References

1) [main site](https://git-scm.com)
2) [Invenio contribution guide](https://invenio.readthedocs.io/en/latest/community/contributing/contribution-guide.html)
3) [How to write a commit message](https://cbea.ms/git-commit/)
