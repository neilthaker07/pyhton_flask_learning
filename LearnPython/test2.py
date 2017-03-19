
import urllib
print(urllib.urlretrieve(repo, "dev-config.yml"))
import requests
print (requests.get(repo).content)


repo = user.get_repo("RepoName")

print(repo)

file = repo.get_file_contents("/App/forms.py")
decoded_content = "# Test " + "\r\n" + file.decoded_content
repo.update_file("/"RepoName"/forms.py", "Commit Comments",decoded_content,
  file.sha)


from github import Github
g = Github()
print(g.get_repo(repoURL))

