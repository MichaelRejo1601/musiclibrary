from django import template

register = template.Library()

@register.filter(name='filter_by_danceability')
def filter_by_danceability(playsongs, request):
    if 'danceabilityCheckbox' in request.GET:
        if request.GET['danceabilityCheckbox']:
            return [song for song in playsongs if song.ps_sid.s_danceability > 0.5]
        
    return playsongs
