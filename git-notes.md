Git
-its about tracking versions of files
-takes snapshots using commit and these are all in memory and only stores
the differences which is why text format is useful so everything is about
lines
-using text and short lines make git effective
-everything is stored in the .git hidden directory
- allows for communitcation with people because all changes are pushed to 
github and pulled by other person
-each snapshot (commit) you add messages to label what the change was
-git checkout will change all files to the state of a previous commi even if
you change a file it is still accessible to via the snapshots. All previous
versions are accessible.
-git show brings up the last commit
-git log shows the title of the commit not the content of 
- --pretty=oneline option will put every commit on one line
-git commit -a will do both git add and git commit but only works on files 
that are being tracked will be added to git.
-changing base editor use  the command config --global core.editor
-when you change file names in git there can be issues so instead of using
just move use git move
-track things that change overtime like scripts text documentation(readme)
natebooks in text format
-do not track large files that can repoduced
-don't track datafiles because git is not the best way to do this
-binary files are not easily tracked by git
-pdf and figures are not good because the entire picture needs to be done
-same with word documents


## If you want to not track a file
-create a git ignore file
```touch gitignore
```
git then uses this file is added to git

##mistakes
If you accidentally overwrite a file you can use git status then git checkout 
to revert to the old version
