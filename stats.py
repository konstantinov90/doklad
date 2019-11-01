#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import json
from datetime import datetime

headers = {
    'Authorization': 'OAuth ' + os.environ['TWILIGHT_OAUTH_TOKEN'],
    'Content-Type': 'application/json',
}

data = {
    'filter': {
        'queue': 'TRANSLATE',
        'serviceServiceGroup': 'Direct',
        'createdBy': 'robot-twilight'
    },
    'order': '-key'
}

issues = requests.post('https://st-api.yandex-team.ru/v2/issues/_search?perPage=1000', headers=headers, data=json.dumps(data)).json()

def parseDate(datestr):
    return datetime.strptime(datestr.strip('+0000'), '%Y-%m-%dT%H:%M:%S.%f')

issues_by_week = {}
deadline_exceeded_by_week = {}


for issue in issues:
    changelog = requests.get('https://st-api.yandex-team.ru/v2/issues/%s/changelog' % issue['key'], headers=headers).json()
    # issue['changelog'] = changelog

    workflows = [rec for rec in changelog if rec['type'] == 'IssueWorkflow']

    opened = [rec for rec in workflows if len([field for field in rec['fields'] if field['field']['id'] == 'status' and field['from']['key'] == 'pending' and field['to']['key'] == 'open']) > 0]
    closed = [rec for rec in workflows if len([field for field in rec['fields'] if field['field']['id'] == 'status'and field['to']['key'] == 'closed']) > 0]
    if (opened):
        issue['opened'] = opened[0]['updatedAt']
        issue['closed'] = closed[0]['updatedAt'] if closed else None
        week = parseDate(issue['opened']).strftime('%U')
        issue['timespan'] = (parseDate(issue['closed']) - parseDate(issue['opened'])).days if closed else 0
        issues_by_week[week] = issues_by_week.get(week, []) + [issue]
        deadline_exceeded_by_week[week] = deadline_exceeded_by_week.get(week, 0) + (1 if issue['timespan'] > 3 else 0)

print 'tickets'

for week in sorted([int(key) for key in issues_by_week.keys()]):
    print '%d, %d' % (week, len(issues_by_week.get(str(week), [])))

print 'deadlines'

for week in sorted([int(key) for key in deadline_exceeded_by_week.keys()]):
    print '%d, %d' % (week, deadline_exceeded_by_week.get(str(week), 0))
