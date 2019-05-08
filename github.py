from api.repositories.repos import Repos
from api.repositories.hooks import Hooks


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)
        self.hooks=Hooks(self.api_root_url, **kwargs)

if __name__ == '__main__':
    r = Github() #token="a589408c719dbbe39fb2cae84585ea4295cf04a0"
    username = "qinfei55"
    repo = "webhooks"
    x=r.hooks.list_hooks(username,repo)
    print('x:',x)
    print(x.status_code)
    print(x.text)

    # x=r.repos.list_your_repos()
    # print(x.text)
    # case 1
    # data = {
    #     "name": "Hello-World654322",
    #     "description": "This is your first repository",
    #     "homepage": "https://github.com",
    #     "private": False,
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_wiki": True
    # }
    # import json as json_parser
    # x = r.repos.create_user_repo(data=json_parser.dumps(data))
    # print(x.status_code)
    # assert x.status_code == 201
    # print(x.text)

    # # case 2
    # x = r.repos.create_organization_repo(org=orgnname, json=data)
    # print(x.status_code)
    # assert x.status_code == 201
    #
    # # case 3
    # x = r.repos.get_repo(username, "Hello-World654")
    # print(x.status_code)
    # assert x.status_code == 200
    # print(x.text)

    # case 4
    # data = {
    #     "name": "Hello-World654",
    #     "description": "YYYY:This is your first repository ",
    #     "homepage": "https://github.com",
    #     "private": False,
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_wiki": True
    # }
    #
    # x = r.repos.edit_repo(username, "Hello-World654", json=data)
    # print(x.status_code)
    # print(x.text)
    # assert x.status_code == 200
