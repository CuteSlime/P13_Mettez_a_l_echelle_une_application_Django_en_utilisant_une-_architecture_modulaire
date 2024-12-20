import logging

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from profiles.models import Profile

logger = logging.getLogger('profiles')

# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request):
    """Return the home page of the profile app

        **URL:** /profiles/
    """

    try:
        profiles_list = Profile.objects.all()
    except Exception:
        logger.error("Error retrieving profiles from the database", exc_info=True)
        return render(request, '500.html', status=500)

    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui.
# Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it.
# Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """return the profile page

        **URL:** /profiles/<username>/
    """

    try:
        profile = get_object_or_404(Profile, user__username=username)
    except (Profile.DoesNotExist, Http404):
        logger.warning(f"Profile with username {username} not found")
        return render(request, '404.html', status=404)
    except Exception:
        logger.error(f"""Unexpected error retrieving profile with username {
                     username}""", exc_info=True)
        return render(request, '500.html', status=500)

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
