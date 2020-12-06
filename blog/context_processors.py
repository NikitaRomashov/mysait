
from .models import Sponsor, SponsorImage


def sponsors(request):
    sponsors_list = Sponsor.objects.all()
    return {'context_sponsors': sponsors_list}
