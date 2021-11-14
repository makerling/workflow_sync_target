from dirsync import sync

sourcedir='./workflow-sync-source/files'
targetdir='./workflow-sync-target/files'
action='sync'

sync(sourcedir, targetdir, action)