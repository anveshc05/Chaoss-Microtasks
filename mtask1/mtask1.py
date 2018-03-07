import requests
import sys
import json
import configparser

def create_config(org):
	config = configparser.ConfigParser()
	config.add_section('general')
	config['general']['short_name'] = 'GrimoireLab'
	config['general']['update'] = 'false'
	config['general']['sleep'] = '0'
	config['general']['debug'] = 'true'
	config['general']['min_update_delay'] = '10'
	config['general']['logs_dir'] = '/tmp/logs'
	config['general']['kibana'] = '"5"'

	config.add_section('projects')
	config['projects']['projects_file'] = org + '.json'

	config.add_section('es_collection')
	config['es_collection']['url'] = 'http://localhost:9200'
	config['es_collection']['user'] = ''
	config['es_collection']['password'] = ''

	config.add_section('es_enrichment')
	config['es_enrichment']['url'] = 'http://127.0.0.1:9200'
	config['es_enrichment']['user'] = ''
	config['es_enrichment']['password'] = ''
	config['es_enrichment']['autorefresh'] = 'false'	
	config['es_enrichment']['studies'] = 'true'

	config.add_section('sortinghat')
	config['sortinghat']['host'] = 'localhost'
	config['sortinghat']['user'] = 'user'
	config['sortinghat']['password'] = 'XXX'
	config['sortinghat']['database'] = 'shatdb'
	config['sortinghat']['load_orgs'] = 'false'
	config['sortinghat']['unify_method'] = ''
	config['sortinghat']['unaffiliated_group'] = 'Unknown'
	config['sortinghat']['affiliate'] = 'True'
	config['sortinghat']['autoprofile'] = '[customer,git,github]'
	config['sortinghat']['matching'] = '[email]'
	config['sortinghat']['sleep_for'] = '0'
	config['sortinghat']['bots_names'] = '[Beloved Bot]'

	config.add_section('panels')
	config['panels']['kibiter_time_from'] = '"now-90d"'

	config.add_section('phases')
	config['phases']['collection'] = 'true'
	config['phases']['identities'] = 'true'
	config['phases']['enrichment'] = 'true'
	config['phases']['panels'] = 'true'

	config.add_section('git')
	config['git']['raw_index'] = 'git_test-raw'
	config['git']['enriched_index'] = 'git-test'

	config.add_section('github')
	config['github']['api-token'] = 'XXX'
	config['github']['raw_index'] = 'github_test-raw'
	config['github']['enriched_index'] = 'github-test'

	return config


def get_repo_url(org):
	git = []
	github = []
	names = []
	url = "https://api.github.com/users/" + org + "/repos"
	page =0
	last_page=0
	r = requests.get(url + "?page=0")

	while ('next' in r.links or not r.links):
		for repo in r.json():
			if not repo['fork']:
				git.append(repo['clone_url'])
				github.append(repo['html_url'])
		if not r.links:
			break
		r = requests.get(r.links['next']['url'])
	return git, github
def main():
	if len(sys.argv) != 2:
		print("Format :: python mtask1.py <orgname to explore>")
		sys.exit(1)
	org = sys.argv[1]
	repos, repo_github = get_repo_url(org)
	config_file = create_config(org)
	json_obj = {}
	json_obj[org] = {}
	json_obj[org]['git'] = repos 
	json_obj[org]['github'] = repo_github 
	with open(org + ".json", "w") as outfile:
		json.dump(json_obj, outfile)

	with open(org + ".cfg", "w") as conf:
		config_file.write(conf)

	# print (repos)
	# print(repo_github)

if __name__ == '__main__':
	main()
