userRepo = repoURL[19:]



config = aaaaaa

@app.route('/v1/filename')
def get_cong(filemame):
call pygit and fetch filename
if file name is .yml then 
	yml
	else
	json
	
	
	
	  '''repo11.index.diff()'''
	
	
for repo in g.get_user().get_repos():
	print repo.name
	

'''
print(g.get_user().repos_url)
print(repoURL)
'''
	
	
	
	
for repo in g.get_user().get_repos():
	if repo.name in repoURL:
		print repo.name
	print(repo.get_file_contents())



from github import Github
g1 = Github()
for repo in g1.get_user(userName).get_repos(repoName):
	if repo.name == repoName:
		print g1.get_user(userName).get_repos(repoName).filename







	

'''	repo.edit(has_wiki=False)
import git 
getLatest = git.cmd.Git("/home/neil/Neil_Work/MS_SJSU/EDS_273/Assignments_Labs/assignment1/part2/cmpe273-assignment1-config/")
getLatest.pull()

import git
repo11 = git.Repo()
mod_files = git.cmd.Git
print mod_files
'''


if __name__ == "__main__":
	app.run(debug=True)

if __name__ == "_main_":
    for arg in sys.argv: 1
	userRepo = arg.replace('https://github.com/','')

CMD ["app.py"]
from github import File
g3 = Github()

ff1 = g3.File.filename



import yaml
with open('dev-config.yml') as stream:
	output = yaml.load(stream)
	webPrint2 = output["welcome_message"] 
	
	
	
	
'''
accessToken = 'b9fa39dff4583d24249930733bbdcdd5a798bf23'
client = Github(accessToken, per_page=100)
repo = client.get_repo(userRepo);'''


