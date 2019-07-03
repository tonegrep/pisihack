# autofill the repo table with users repos


# def test_this(sender, **kwargs):
#     print('are we in there???')
#     sociallogin = kwargs['sociallogin']
#     g = Github(str(sociallogin.token))
#
#     repo_listing = g.get_user().get_repos()
#     repo_ids = tuple(repo.id for repo in repo_listing)
#     print(repo_ids)
#
#     repo_objs = Repository.objects.filter(repo_id__in=repo_ids)
#     print(repo_objs)
#
#     # we have all repos
#     if len(repo_objs) == len(list(repo_ids)):
#         print('all repos syned', len(repo_objs), repo_ids)
#         print(Repository.objects.all())
#         pass
#     else:
#         user_profile = UserProfile(
#             user=sociallogin.user.name,
#             total_points=0
#         )
#         user_profile.save()
#         print('syncing repos')
#         for repo in repo_listing:
#             print('a')
#             repo_obj = Repository(
#                 repo_id=repo.id,
#                 name=repo.full_name,
#                 description=repo.description,
#                 author=UserProfile.objects.get(user__username='pepe')
#             )
#             repo_obj.save()
#
#
# def test_other(request, **kwargs):
#     token = str(kwargs['user'].socialaccount_set.get().socialtoken_set.get())
#     g = Github(token)
#
#     repo_listing = g.get_user().get_repos()
#     repo_ids = tuple(repo.id for repo in repo_listing)
#
#     repo_objs = Repository.objects.filter(repo_id__in=repo_ids)
#
#     # we have all repos
#     if len(repo_objs) == len(list(repo_ids)):
#         print('all repos syned', len(repo_objs), repo_ids)
#         print(Repository.objects.all())
#         pass
#     else:
#         print('syncing repos')
#         for repo in repo_listing:
#             print(repo.description)
#             repo_obj = Repository(
#                 repo_id=repo.id,
#                 name=repo.full_name,
#                 description=repo.description or '',
#                 author=user_profile
#             )
#             repo_obj.save()


from allauth.account.signals import user_signed_up
# pre_social_login.connect(test_this)
# use this in prod instead
# user_signed_up.connect(test_other)
from django.dispatch import receiver
from django.utils.timezone import make_aware
from github import Github

from projects.models import Repository
from .models import PisiUser


@receiver(user_signed_up, sender=PisiUser)
def update_repos(sender, **kwargs):
    print('received signup signal', kwargs)

    user = kwargs.pop('user')
    token = kwargs.pop('sociallogin').token.token

    g = Github(token)

    # if a db repo table doesnt have all the latest gh repos
    # then get all changed/new repos and update/create them
    repos = {repo.id: repo for repo in g.get_user().get_repos(visibility='public')}
    repo_objs = Repository.objects.filter(author=user)

    # update
    to_update = []
    for repo in repo_objs:
        gh_repo = repos[repo.repo_id]
        if gh_repo.modified_at > repo.last_updated:
            repo.last_updated = make_aware(gh_repo.modified_at)
            to_update.append(repo)

    Repository.objects.bulk_update(to_update, ['last_updated'])

    # create
    def create_db_repo(repo_id):
        repo = repos[repo_id]
        return Repository(
            repo_id=repo.id,
            name=repo.full_name,
            description=repo.description or '',
            author=user,
            last_updated=repo.updated_at
        )

    # repo ids not in db will be created
    repo_obj_ids = set(repo.repo_id for repo in repo_objs)
    to_create = map(create_db_repo, (repos.keys() - repo_obj_ids))
    Repository.objects.bulk_create(to_create)
