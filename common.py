"""公共的有限数值与来源校验。"""
from pathlib import Path
import json,math,hashlib

def read(path="data/source.json"):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def number(value):
    if isinstance(value,bool):raise ValueError("布尔值不是数值")
    try:x=float(value)
    except (ValueError,TypeError):raise ValueError("数值格式错误")
    if not math.isfinite(x):raise ValueError("数值非有限")
    return x

def unique(rows,key):
    out={}
    for row in rows:
        ident=row[key]
        if ident in out and out[ident]!=row:raise ValueError("同一来源标识内容冲突")
        out[ident]=row
    return out

def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
