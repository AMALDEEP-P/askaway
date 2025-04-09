from django import template
from django.utils import timezone


register = template.Library()


@register.filter(name="time_ago")
def time_ago(value):
    """
    Converrt a datetime object to a human-readable time ago string.
    """
    now = timezone.now()
    time_difference = now - value

    if time_difference.days > 365:
        years = time_difference.days // 365
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif time_difference.days > 30:
        months = time_difference.days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif time_difference.days > 0:
        return (
            f"{time_difference.days} day{'s' if time_difference.days > 1 else ''} ago"
        )

    elif time_difference.seconds > 3600:
        hours = time_difference.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"

    elif time_difference.seconds >= 60:
        minutes = time_difference.seconds // 60
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        return "Just now"
