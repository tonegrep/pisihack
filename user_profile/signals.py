from allauth.socialaccount.models import SocialLogin, SocialAccount
from allauth.account.signals import user_signed_up

# autofill the repo table with users repos
from github import Github

from projects.models import Repository
from user_profile.models import UserProfile


def test_this(sender, **kwargs):
    print('are we in there???')
    sociallogin = kwargs['sociallogin']
    g = Github(str(sociallogin.token))

    repo_listing = g.get_user().get_repos()
    repo_ids = tuple(repo.id for repo in repo_listing)
    print(repo_ids)
    SocialLogin

    repo_objs = Repository.objects.filter(repo_id__in=repo_ids)
    print(repo_objs)

    # we have all repos
    if len(repo_objs) == len(list(repo_ids)):
        print('all repos syned', len(repo_objs), repo_ids)
        print(Repository.objects.all())
        pass
    else:
        user_profile = UserProfile(
            user=sociallogin.user.name,
            total_points=0
        )
        user_profile.save()
        print('syncing repos')
        for repo in repo_listing:
            print('a')
            repo_obj = Repository(
                repo_id=repo.id,
                name=repo.full_name,
                description=repo.description,
                author=UserProfile.objects.get(user__username='pepe')
            )
            repo_obj.save()


def test_other(request, **kwargs):
    user_profile = UserProfile(
        user=kwargs['user'],
        total_points=0
    )
    user_profile.save()

    token = str(kwargs['user'].socialaccount_set.get().socialtoken_set.get())
    g = Github(token)

    repo_listing = g.get_user().get_repos()
    repo_ids = tuple(repo.id for repo in repo_listing)

    repo_objs = Repository.objects.filter(repo_id__in=repo_ids)

    # we have all repos
    if len(repo_objs) == len(list(repo_ids)):
        print('all repos syned', len(repo_objs), repo_ids)
        print(Repository.objects.all())
        pass
    else:
        print('syncing repos')
        for repo in repo_listing:
            print(repo.description)
            repo_obj = Repository(
                repo_id=repo.id,
                name=repo.full_name,
                description=repo.description or '',
                author=user_profile
            )
            repo_obj.save()


# pre_social_login.connect(test_this)
# use this in prod instead
user_signed_up.connect(test_other)
