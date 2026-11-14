"""当前资料入口；不实现统计分析目标。"""
import json
from common import read
from tasks import tasks
from battery import readings
from charging import sessions
def prepare_sources():
    data=read()
    return {'tasks': tasks(data), 'readings': readings(data), 'sessions': sessions(data)}
if __name__=="__main__":print(json.dumps(prepare_sources(),ensure_ascii=False,default=str,indent=2))