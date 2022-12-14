#!usr/bin/env python

import sys

from git import Repo
from termcolor import cprint

args = sys.argv[1:]

repo = Repo()
git = repo.git
# cache current branch
currentBranchName = repo.head.ref.name

# check if working tree is clean
isDirty = repo.is_dirty(untracked_files=True)
if (isDirty):
    cprint('Unclean working tree. Commit or stash changes first', 'red')
    exit(1)


if len(args) == 0:
    cprint('No branch name provided', 'red')
    print(' - Usage: python3 <path_to_this_file> <branch1_name> <branch2_name> ...')
    exit(1)

# check if all branches exist
branchNames = [x.name for x in repo.branches]
invalidBranches = [x for x in args if x not in branchNames]
if len(invalidBranches) > 0:
    cprint('Branch does not exist: {}'.format(invalidBranches), 'red')
    exit(1)


def mergeFlow(branches):
    print('\nSTART MERGE FLOW...')

    for idx, branch in enumerate(branches):
        git.checkout(branch)
        git.pull()
        if idx == 0:
            continue
        git.merge('-')
        git.push()
        print('  ✅ {} -> {}'.format(branches[idx - 1], branch))

    git.checkout(currentBranchName)
    print()
    cprint('🎉 COMPLETED: {}'.format(' -> '.join(branches)), 'green')


mergeFlow(args)
