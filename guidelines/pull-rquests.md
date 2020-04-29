# How to Create a Pull Request on RERO github projects

1. Create the PR in Draft mode
1. Fill in the PR comment, according to the template.
    1. Why you're opening the PR.
    1. Does it depend on a PR on other projects?
    1. How to test the PR (for developers and Product Owner).
1. Make sure your branch is up-to-date with the desired branch (parent branch you come from)
1. Make sure you do not have extra commits to squash
1. Make you own review on github
1. Update the commit message after the review to be sure that all what you have done is described
1. Check that the travis tests are successfull
1. Test your PR from scratch localy: bootstrap, setup and test the part of the interface touched by your work
1. Check the list in your PR
    1. Commit message template compliance.
    1. Commit message without typos.
    1. File names.
    1. Functions names.
    1. Functions docstrings (https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html).
    1. Unnecessary commited files?
    1. Extracted translations?
1. Remove the draft mode
1. Call the first reviewer
1. After the first acceptance, call one or two other reviewers
1. **If you've added strings to be translated**, ask someone of the PO group or the SM to review these strings.