#!/bin/dash -e
#A script to streamline commit and push of changes to git.
# read -p "Commit description: " desc
# echo "Executing pull, add -A, commit -m $desc, push"
git pull
git add -A
# git commit -m "$desc"
git commit -m "$1"
git push