from common import unique
from tasks import tasks
def readings(data):
    tt=tasks(data);rows=unique(data['battery_readings'],'reading_id');last={}
    for r in sorted(rows.values(),key=lambda x:(x['vehicle'],x['at'])):
        if r['vehicle'] not in data['vehicles'] or r['task_id'] not in tt or not 0<=r['soc_kwh']<=r['capacity_kwh']:raise ValueError('电池读数或任务非法')
        key=r['vehicle']
        if key in last and r['at']<=last[key]['at']:raise ValueError('电池读数时间不递增')
        if key in last and r['meter_epoch']==last[key]['meter_epoch'] and r['soc_kwh']>r['capacity_kwh']:raise ValueError('电池容量读数越界')
        last[key]=r
    return rows
