tecnics@tecnics-Satellite-Pro-R50-B:~$ git init GitAbhi
Initialized empty Git repository in /home/tecnics/GitAbhi/.git/
tecnics@tecnics-Satellite-Pro-R50-B:~$ cd /home/tecnics/GitAbhi/
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi$ ls
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi$ git clone https://github.com/enchanter5525/FirstRepository.git
Cloning into 'FirstRepository'...
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 23 (delta 3), reused 15 (delta 1), pack-reused 0
Unpacking objects: 100% (23/23), done.
Checking connectivity... done.
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi$ ls
FirstRepository
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi$ cd FirstRepository
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ ls
MyFirstGitFile.c  README.md
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ subl README.md
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ git branch Abhi
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ git checkout Abhi
M	README.md
Switched to branch 'Abhi'
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ git add README.md
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ git commit -m "Check the Git codes"
[Abhi a4a8251] Check the Git codes
 1 file changed, 28 insertions(+), 4 deletions(-)
 rewrite README.md (96%)
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ git push --set-upstream origin Abhi
Username for 'https://github.com': enchanter5525
Password for 'https://enchanter5525@github.com': ##Korunga123
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/enchanter5525/FirstRepository.git/'
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ git push --set-upstream origin Abhi
Username for 'https://github.com': enchanter5525
Password for 'https://enchanter5525@github.com': 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 632 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'Abhi' on GitHub by visiting:
remote:      https://github.com/enchanter5525/FirstRepository/pull/new/Abhi
remote: 
To https://github.com/enchanter5525/FirstRepository.git
 * [new branch]      Abhi -> Abhi
Branch Abhi set up to track remote branch Abhi from origin.
tecnics@tecnics-Satellite-Pro-R50-B:~/GitAbhi/FirstRepository$ 
