# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('a_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='bug.A')),
            ],
            options={
            },
            bases=('bug.a',),
        ),
    ]
