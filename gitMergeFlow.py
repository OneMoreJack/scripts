#!usr/bin/env python

import argparse

from git import Repo
from termcolor import cprint


def mergeFlow(branches, currentBranchName):
    print('\n' + '=' * 40 + '\n')
    print('START MERGE GIT BRANCHES...' + '\n')

    for idx, branch in enumerate(branches):
        git.checkout(branch)
        git.pull()
        if idx == 0:
            git.push()
            continue
        git.merge('-')
        git.push()
        print(' ✅ {} -> {}'.format(branches[idx - 1], branch))

    git.checkout(currentBranchName)
    print()
    cprint('🎉 COMPLETED: {}'.format(' -> '.join(branches)), 'green')


def checkWorkingTree(repo):
    # check if working tree is clean
    isDirty = repo.is_dirty(untracked_files=True)
    if (isDirty):
        cprint('Unclean working tree. Commit or stash changes first', 'red')
        exit(1)


def validateBranches(repo, targetBranches):
    # check if all branches exist
    branches = repo.branches
    branchNames = list(map(lambda x: x.name, branches))
    invalidBranches = list(
        filter(lambda x: x not in branchNames, targetBranches))
    if len(invalidBranches) > 0:
        cprint('Branch does not exist: {}'.format(invalidBranches), 'red')
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge git branches")
    parser.add_argument(
        'targetBranches', help="branches to be merged", nargs='+')
    args = parser.parse_args()
    targetBranches = args.targetBranches

    repo = Repo()
    git = repo.git
    # cache current branch
    currentBranchName = repo.head.ref.name

    # check if working tree is clean
    checkWorkingTree(repo)
    validateBranches(repo, targetBranches)
    mergeFlow(targetBranches, currentBranchName)
