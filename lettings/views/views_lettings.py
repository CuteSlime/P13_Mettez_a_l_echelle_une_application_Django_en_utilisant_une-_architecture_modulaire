import logging

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from lettings.models import Letting

logger = logging.getLogger('lettings')

# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa.
# Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
# Cras eget scelerisque


def index(request):
    """Return the home page of the letting app

        **URL:** /lettings/
    """

    try:
        lettings_list = Letting.objects.all()
    except Exception:
        logger.error("Error retrieving lettings from the database", exc_info=True)
        return render(request, '500.html', status=500)

    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend.
# Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus.
# Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna.
# Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum.
# Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """return the letting page

        **URL:** /lettings/<letting_id>/
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)

    except (Letting.DoesNotExist, Http404):
        logger.warning(f"Letting with ID {letting_id} not found")
        return render(request, '404.html', status=404)
    except Exception:
        logger.error(f"Unexpected error retrieving letting with ID {letting_id}", exc_info=True)
        return render(request, '500.html', status=500)

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
