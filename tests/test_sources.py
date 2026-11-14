"""既有资料契约与错误数据检查。"""
import unittest
from common import read
from tasks import tasks as first
from battery import readings as second
from charging import sessions as third
class SourceTests(unittest.TestCase):
    def test_source_interfaces(self):
        data=read();self.assertTrue(first(data));self.assertTrue(second(data));self.assertTrue(third(data))
    def test_reject_corrupt_identity(self):
        data=read()
        key={1:('shifts','shift_id'),2:('simulations','run_id'),3:('requests','request_id'),4:('map_segments','segment_id'),5:('orders','parcel_id'),6:('rules','rule_id'),7:('rollouts','rollout_id'),8:('vehicle_states','state_id'),9:('prompts','prompt_id'),10:('tasks','task_id')}[10][0]
        identity={1:'shift_id',2:'run_id',3:'request_id',4:'segment_id',5:'parcel_id',6:'rule_id',7:'rollout_id',8:'state_id',9:'prompt_id',10:'task_id'}[10]
        row=dict(data[key][0]);row[identity]=data[key][0][identity];field=next(k for k in row if k!=identity);row[field]=str(row[field])+'-conflict'
        data[key].append(row)
        with self.assertRaises(ValueError):first(data)
    def test_reject_wrong_link(self):
        data=read()
        if 10==1:data['cycles'][0]['shift_id']='missing';fn=second
        elif 10==2:data['simulations'][0]['scene_id']='missing';fn=second
        elif 10==3:data['dispatch'][0]['request_id']='missing';fn=second
        elif 10==4:data['work_runs'][0]['map_version']='missing';fn=third
        elif 10==5:data['handoffs'][0]['parcel_id']='missing';fn=second
        elif 10==6:data['evidence'][0]['config_id']='missing';fn=third
        elif 10==7:data['exposure'][0]['rollout_id']='missing';fn=second
        elif 10==8:data['vehicle_states'][0]['mode']='mystery';fn=first
        elif 10==9:data['responses'][0]['kind']='mystery';fn=second
        else:data['charge_sessions'][0]['plug']='missing';fn=third
        with self.assertRaises(ValueError):fn(data)
