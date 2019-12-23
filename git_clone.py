from git import Repo
import os


git_url = 'https://github.com/vivekanandpv/py-book-store-project.git'

dir_name = os.path.basename(os.path.splitext(git_url)[0])

repo_dir = os.path.join(os.getcwd() , dir_name)

if dir_name in os.listdir(os.getcwd()):
    repo_dir = repo_dir + '_1'

try:
    Repo.clone_from(git_url, repo_dir, branch='master')
except Exception as E:
    print(E)
else:
    print('Cloning Successfull!!')




