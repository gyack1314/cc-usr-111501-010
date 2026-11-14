# 电动无人车队的任务能耗与补能可用性核算

本项目整理电动无人车队的任务能耗与补能可用性核算所需的业务来源记录，并核对不同系统间的身份、版本、时序与单位口径。数据为离线合成资料。各来源职责和已有边界见[来源口径](docs/contracts.md)。当前没有实现统计估计、预测模型或业务方案求解。

Python 3.11，运行与验证命令均在项目根目录执行：

```sh
python -m unittest discover -s tests -v
python -m compileall -q .
python -m analytics
```
