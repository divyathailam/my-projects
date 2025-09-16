commands = [
    ("git init", "Initialize a new Git repository in the current directory."),
    ("git status", "Show the state of the working tree and staging area."),
    ("git add <path>", "Stage changes in <path> for the next commit."),
    ("git commit -m \"message\"", "Record staged changes with an inline commit message."),
    ("git branch", "List local branches and highlight the current branch."),
    ("git checkout <branch>", "Switch to an existing branch or restore files."),
    ("git merge <branch>", "Merge the specified branch into the current branch."),
    ("git log", "Show commit history for the current branch."),
    ("git remote -v", "List remote repositories and their URLs."),
    ("git clone <url>", "Copy a remote repository to a new local directory."),
    ("git pull", "Fetch from the remote and integrate into the current branch."),
    ("git push", "Upload local commits to the remote repository."),
    ("git stash", "Temporarily save local changes without committing them."),
    ("git fetch", "Download objects and refs from another repository."),
    ("git rebase <branch>", "Reapply commits on top of another base branch."),
    ("git reset --hard <ref>", "Reset current branch and working tree to the specified state."),
    ("git cherry-pick <commit>", "Apply the changes introduced by each commit to the current branch."),
    ("git revert <commit>", "Create a new commit that reverses the changes from the specified commit."),
    ("git tag <name>", "Create a tag to mark a specific commit."),
    ("git bisect", "Find the commit that introduced a bug via binary search."),
    ("git blame <file>", "Show commit info for each line in the given file."),
    ("git reflog", "Show local history of branch movements and HEAD changes."),
    ("git submodule", "Manage repositories embedded inside another repository."),
]

for command, explanation in commands:
    print(f"{command}\n  -> {explanation}\n")
