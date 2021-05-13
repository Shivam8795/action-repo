from git import Repo

PATH_OF_GIT_REPO = r'https://github.com/Shivam8795/action-repo/edit/main/actionrepo.py\.git'  
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(https://github.com/Shivam8795/action-repo/edit/main/actionrepo.py)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()


import json
import os
import sys

import requests


def neutral_exit():
    sys.exit(0)


def get_session(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):
    sess = requests.Session()
    sess.headers = {
        "Accept": "; ".join([
            "application/vnd.github.v3+json",
            "application/vnd.github.antiope-preview+json",
        ]),
        "Authorization": f"token {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}",
        "User-Agent": f"GitHub Actions script in {__file__}"
    }

    def raise_for_status(resp, *args, **kwargs):
        try:
            resp.raise_for_status()
        except Exception:
            print(resp.text)
            sys.exit("Error: Invalid repo, token or network issue!")

    sess.hooks["response"].append(raise_for_status)
    return sess


if __name__ == '__main__':
    github_token = os.environ["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"]
    github_repository = os.environ["https://github.com/Shivam8795/action-repo/edit/main/actionrepo.py"]

    github_event_path = os.environ["https://github.com/Shivam8795/action-repo/edit/main/actionrepo.py"]
    event_data = json.load(open(https://github.com/Shivam8795/action-repo/edit/main/actionrepo.py))

    check_run = event_data["check_run"]
    name = check_run["name"]

    sess = get_session(github_token)

    if len(check_run["pull_requests"]) == 0:
        print("*** Check run is not part of a pull request, so nothing to do")
        neutral_exit()

    
    
    conclusion = check_run["conclusion"]
    print(f"*** Conclusion of {name} is {conclusion}")

    if conclusion is None:
        print(f"*** Check run {name} has not completed, skipping")
        neutral_exit()

    if conclusion != "success":
        print(f"*** Check run {name} has failed, will not merge PR")
        sys.exit(1)

   
    assert len(check_run["pull_requests"]) == 1
    pull_request = check_run["pull_requests"][0]
    pr_number = pull_request["number"]
    pr_src = pull_request["head"]["ref"]
    pr_dst = pull_request["base"]["ref"]

    print(f"*** Checking pull request #{pr_number}: {pr_src} ~> {pr_dst}")
    pr_data = sess.get(pull_request["url"]).json()

    pr_title = pr_data["title"]
    print(f"*** Title of PR is {pr_title!r}")
    if pr_title.startswith("[WIP] "):
        print("*** This is a WIP PR, will not merge")
        neutral_exit()

    pr_user = pr_data["user"]["login"]
    print(f"*** This PR was opened by {pr_user}")
    if pr_user != "alexwlchan":
        print("*** This PR was opened by somebody who isn't me; requires manual merge")
        neutral_exit()

    print("*** This PR is ready to be merged.")
    merge_url = pull_request["https://github.com/Shivam8795/action-repo/edit/main/actionrepo.py"] + "/merge"
    sess.put(merge_url)

    print("*** Cleaning up PR branch")
    pr_ref = pr_data["head"]["ref"]
    api_base_url = pr_data["base"]["repo"]["url"]
    ref_url = f"{api_base_url}/git/refs/heads/{pr_ref}"
    sess.delete(ref_url)
