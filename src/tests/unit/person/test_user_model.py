import pytest

from pretalx.person.models.user import User
from pretalx.submission.models.question import Answer


@pytest.mark.parametrize('email,expected', (
    ('one@two.com', 'ac5be7f974137dc75bacee19b94fe0f8'),
    ('a_very_long.email@orga.org', '79bd022bbbd718d8e30f730169067b2a'),
))
def test_gravatar_parameter(email, expected):
    user = User(email=email)
    assert user.gravatar_parameter == expected


@pytest.mark.django_db
def test_user_deactivate(speaker, personal_answer, impersonal_answer, other_speaker):
    assert Answer.objects.count() == 2
    count = speaker.own_actions().count()
    name = speaker.name
    email = speaker.email
    organiser = speaker.submissions.first().event.organiser
    team = organiser.teams.first()
    team.members.add(speaker)
    team.save()
    team_members = team.members.count()
    speaker.deactivate()
    speaker.refresh_from_db()
    assert speaker.own_actions().count() == count
    assert speaker.profiles.first().biography == ''
    assert speaker.name != name
    assert speaker.email != email
    assert Answer.objects.count() == 1
    assert Answer.objects.first().question.contains_personal_data is False
    assert team.members.count() == team_members - 1
    assert 'deleted' in str(speaker).lower()
    assert speaker.get_permissions_for_event(Answer.objects.first().event) == set()


def test_administrator_permissions():
    user = User(email='one@two.com', is_administrator=True)
    assert user.get_permissions_for_event('randomthing') == {
        'can_create_events', 'can_change_teams', 'can_change_organiser_settings',
        'can_change_event_settings', 'can_change_submissions', 'is_reviewer',
    }
