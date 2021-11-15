from dirsync import sync

sourcedir='workflow_sync_source/files'
targetdir='workflow_sync_target/files'
action='sync'

sync(sourcedir, targetdir, action)