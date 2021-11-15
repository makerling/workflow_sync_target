from dirsync import sync

sourcedir='/home/runner/work/workflow_sync_target/workflow_sync_target/workflow_sync_source/files'
targetdir='/home/runner/work/workflow_sync_target/workflow_sync_target/files'
action='sync'

sync(sourcedir, targetdir, action)