# Chaoss-Microtasks

* **Requirements**
1. development environment, python3, pip3
2. Elasticsearch running on localhost:9200, Kibana running on localhost:5601
3. Grimoirelab packages like sortinghat, perceval  
4. Clone the repository using  
> git clone https://github.com/anveshc05/Chaoss-Microtasks.git

### Micro-task 1

Produce a Python script that produces configuration files for Mordred to analyze a complete GitHub organization, excluding repositories that are forks from other GitHub repositories. Test it with at least two GitHub organizations, producing screenshots of the resulting dashboard.

* **Solution file**  

The python code which generates the configuration files which generate the configuration files for mordred can be found in the [mtask1](mtask1/) directory by the name [mtask1.py](mtask1/mtask1.py).

I have produced dashboards for 2 organizations which are
* [haiku](https://github.com/haiku)
* [robocomp](https://github.com/robocomp)

* **Screenshots**  
All the screenshots have been placed in the [Screenshots](mtask1/Screenshots/) directory inside the [mtask1](mtask1/) directory.

_Some sample screenshots for reference_

![haiku git ](mtask1/Screenshots/Haiku/haiku_git_full.png )

![haiku pullrequests ](mtask1/Screenshots/Haiku/github_pull_requests.png)

* **How To Run**  
* Run command
> python mtask1.py orgname   
* This would lead to formation of 2 files orgname.cfg and orgname.json
* Start elasticearch and kibana.
* Change the name of sorting-hat user, sorting-hat password and [add your github api token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) to the github backend.
* Run the command 
> mordred -c orgname.cfg
* Run kibana to see dashboards.


### Micro-task 2

Produce a Python script that adds a new GitHub repository (git and GitHub issues / pull requests) to a given set of Mordred configuration files. Test it by adding at least two repositories (in two separate steps) to a GrimoireLab dashboard, producing screenshots of the results.

* **Solution file**  

The python code which generates the configuration files which generate the configuration files for mordred can be found in the [mtask2](mtask2/) directory by the name [mtask2.py](mtask2/mtask2.py).

I have shown the addition of two different repositories to the dashboard, one from the same project and one from another project for showing the working of implementation

* **Screenshots**  
All the screenshots have been placed in the [Screenshots](mtask2/Screenshots/) directory inside the [mtask1](mtask2/) directory.

_Some Sample Screenshots for reference_

![initial_dashboard_1_repo ](mtask1/Screenshots/initial-dashboard/git/grimoire_git_3.png)


![add_same_project_repo ](mtask1/Screenshots/add_same_project_repo/git/2_repo_git_3.png)


![add_different_project_repo ](mtask1/Screenshots/add_different_project_repo/git/diff_project_git_3.png)

* **How To Run**  
* Run command
> python mtask2.py project_name orgname reponame 
* This would lead to formation of 2 files projectname_reponame.cfg and projectname_reponame.json
* Start elasticearch and kibana.
* Change the name of sorting-hat user, sorting-hat password and [add your github api token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) to the github backend.
* Run the command 
> mordred -c projectname_reponame.cfg
* Run kibana to see dashboards.


