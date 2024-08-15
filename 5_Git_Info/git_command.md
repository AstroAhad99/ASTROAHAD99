#### Install GIT for windows 

#### Git Commands


1. clone - Brings the repository hosted on the web to the local machine.

2. add - Track the files and changes in Git.

3. commit - Save the changes to the Git.

<<<<<<< HEAD
4. push - Upload the Git changes to the remote repository from the local repository. Sometimes push does not work because you need to tell github to receive the updates from you local editor. For this purpose you need to add SSH key. Check this video at time 20:40 for more information.
```https://www.youtube.com/watch?v=RGOj5yH7evk``` 

5. pull (PR) - Download the changes from the remote repository to the local repository.

---

6. ``git status`` - To see in which files there are new updates

7. ``git add File_Name.md`` (We can skip this step also if we do only commit.)

8. ``git commit -m "Add Comments"``. If you want to do add and commit at the same time (In the existing files) the you can type ```git commit -am "Add Comments"```

9. ``git push origin master`` (origin means github link and master is the branch)

10. git branch (Shows the branches available in repository)

11. The purpose of the braches is to allow the software development easier like we can build 3 different platforms (branches) like dev, stage, and production so that each branch is independent of each other and makes the development safer and effecient. Once if everything works well in the dev environment then we can push it to the stage env and then to production environment.

``https://www.youtube.com/watch?v=RGOj5yH7evk``

---

12. ```git checkout -b new_branch_name``` To create a new branch

13. In this new branch you can create new files and commit the changes in the new files that are not seen from the master branch. 

14. ```git checkout master``` To move to the master branch again.

15. Once you are in the master branch then you can use diff command to see the difference between the current and the referred branch.
```git diff new_branch_name```

16. Now go to your new branch and push these changes to the github like ```git push -u origin new_branch_name```

17. Now open your git hub and there you can see that you have added maded changes in your new branch so after reviewing you can do merge the changes to your master repo.

18. Now to pull the new changes in your local repo, do the pull request like ```git pull origin master``` OR if the upstream is already configured then do ```git pull```,

19. Now we can delete the new_branch_name by ```git branch -d new_branch_name```

20. Sometimes there are multiple developers who are making their own branches and trying to push their changes to the main branch so there might be conflicts. Lets see this with an example.

21. Create a new branch with name new_branch

22. Open any file which exists in the main branch and edit ant line. Then make the commit to that new branch.

23. Then move to the master branch then make the same changes in the same file and the same line and then commit the changes.

24. Now move again to the new branch try to do merge like ```git merge master```.

25. When you execute this command then you will get an error that there is a conflict. To resolve this conflict you can do it easily from the editor.

26. At the end you can commit the changes again.

---

27. If you have already done the stage process (```git add```) then you can reset it by ```git reset``` command.

28. If you have commited the changes then you can do ```git reset HEAD~1```. It will go back to the last changes.

29. To unstaged using the hash key of the commit can be possible by looking at the hash first like ```git log```. Then copy the hash then type ```git reset hash-key```. This will unstage all the changes again.

30. If you want to completely remove the changes that you have made then type ```git reset --hard hash-key```

---

31. Fork means copy the whole repository from other source to our account and make us able to make the changes.  

32. Strings have another feature of "Something".join(another_list) or other properties.
=======
4. push - Upload the Git changes to the remote repository from the local repository.

5. pull - Download the changes from the remote repository to the local repository.

>>>>>>> e5dddf5dbf4a9fec31d4966471a30fdec27d13dd
