from git import Repo
import os

# github url
git_url = 'https://github.com/vivekanandpv/python-basics.git'

# First took the path except .git and the split with '/'
dir_name= os.path.splitext(git_url)[0].split('/')

# Creating a path joining current dir + git-repository + parent_folder + child_folder
repo_dir = os.path.join(os.getcwd() , 'git-repository', dir_name[-2], dir_name[-1])

# Incase child folder is present then we rename to folder by adding _1.
# if dir_name[-1] in os.listdir(os.path.join(os.getcwd(),'git-repository', dir_name[-2])):
#     repo_dir = repo_dir + '_1'

try:
    Repo.clone_from(git_url, repo_dir, branch='master')
except Exception as E:
    print(E)
else:
    print('Cloning Successfull!!')




