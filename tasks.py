from common import unique
def tasks(data):
    rows=unique(data['tasks'],'task_id')
    for r in rows.values():
        if r['vehicle'] not in data['vehicles'] or r['payload_kg']<0 or r['end']<r['start']:raise ValueError('任务载荷或时段非法')
    return rows
