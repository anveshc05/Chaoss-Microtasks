from elasticsearch5 import Elasticsearch
from elasticsearch_dsl import Search

es = Elasticsearch()

def delete_repo(to_delete):
	'''
	deletes the repository(github issues and git commits) from the dashboard by deleting the 
	elasticsearch data.
	:param to_delete : the url of the repository to be deleted
	'''
	print("Repository" , to_delete, "will be deleted")
	s = Search(using = es, index = "git_test", doc_type="items").\
		query("match", origin=to_delete + ".git")
		
	response = s.delete()

	s = Search(using = es, index = "git_test-raw", doc_type="items").\
		query("match", origin=to_delete + ".git")
		
	response = s.delete()
	
	s = Search(using = es, index = "github_test", doc_type="items").\
		query("match", origin=to_delete )
	response = s.delete()
	

	s = Search(using = es, index = "github_test-raw", doc_type="items").\
		query("match", origin=to_delete )
	response = s.delete()

def show_repositories():
	"""
	Shows the repositories present  in the current dashboard and asks for input from
	the user for the one to be deleted
	"""
	print("The list of repositories available is ->")
	s = Search(using = es, index = "github_test")
	s.aggs.bucket('repos','terms', field='origin')
	response = s.execute()
	list_rep = response['aggregations']['repos']['buckets']
	for i,res in enumerate(list_rep, start=1):
		print(i, res['key'])
	
	print("Type the index number of the repository to be deleted")
	num = int(input())
	return list_rep[num-1]['key']

def main():
	to_delete = show_repositories()
	delete_repo(to_delete)

if __name__ == '__main__':
	main()
