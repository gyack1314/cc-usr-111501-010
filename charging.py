from common import unique
from battery import readings
def sessions(data):
    rr=readings(data);rows=unique(data['charge_sessions'],'session_id')
    for r in rows.values():
        if r['vehicle'] not in data['vehicles'] or r['plug'] not in data['plugs'] or r['end']<r['start'] or r['energy_in_kwh']<0:raise ValueError('补能会话非法')
    occupancy={}
    for r in rows.values():occupancy.setdefault(r['plug'],[]).append((r['start'],r['end'],r['session_id']))
    for seq in occupancy.values():
        seq.sort()
        if any(b[0]<a[1] for a,b in zip(seq,seq[1:])):raise ValueError('同一充电位时段冲突')
    return {'sessions':rows,'readings':rr,'energy_in_kwh':sum(r['energy_in_kwh'] for r in rows.values())}
