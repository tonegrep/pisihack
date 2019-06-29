from allauth.socialaccount.signals import pre_social_login, social_account_added

# autofill the repo table with users repos
from github import Github

from projects.models import Repository


def test_this(sender, **kwargs):
    sociallogin = kwargs['sociallogin']
    g = Github(str(sociallogin.token))

    repo_listing = g.get_user().get_repos()
    repo_ids = (repo.id for repo in repo_listing)

    repo_objs = Repository.objects.filter(repo_id__in=repo_ids)

    # we have all repos
    if len(repo_objs) == len(tuple(repo_ids)):
        pass
    else:
        for repo in repo_listing:
            repo_obj = Repository(
                repo_id=repo.id,
                name=repo.full_name,
                description=repo.description,
                author=repo.owner
            ).save()


pre_social_login.connect(test_this)
# use this in prod instead
# social_account_added.connect(test_this)
