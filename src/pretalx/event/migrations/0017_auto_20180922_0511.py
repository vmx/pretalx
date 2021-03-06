# Generated by Django 2.0.8 on 2018-09-22 10:11

from django.db import migrations, models
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_remove_event_permitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='landing_page_text',
            field=i18nfield.fields.I18nTextField(blank=True, help_text='This text will be shown on the landing page, alongside with links to the CfP and schedule, if appropriate. You can use <a href="https://docs.pretalx.org/en/latest/user/markdown.html" target="_blank" rel="noopener">Markdown</a> here.', null=True, verbose_name='Landing page text'),
        ),
        migrations.AlterField(
            model_name='event',
            name='locale',
            field=models.CharField(choices=[('en', 'English'), ('de', 'German'), ('fr', 'French')], default='en', max_length=32, verbose_name='Default language'),
        ),
        migrations.AlterField(
            model_name='team',
            name='review_override_votes',
            field=models.PositiveIntegerField(default=0, help_text='Each member of this team will have this amount of override votes per event to indicate an absolute positive or negative opinion of a submission.', verbose_name='Override votes'),
        ),
    ]
