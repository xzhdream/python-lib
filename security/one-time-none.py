import time
import hashlib

import redis

r = redis.Redis(host='122.51.198.168', port=6379, password='qwer@1234',db=0)
r.zadd('test',{'x111111111':str(time.time())})


def check_one_time_nonce(key,rtime,token,nonce,sign):
    #1、校验时间
    if time.time() - rtime > 60:
        return False

    #2、校验签名
    _sign = hashlib.md5(f'{rtime}#{token}#{nonce}').hexdigest()
    if _sign != sign:
        return False

    #3、校验sign是否已被使用
    score = r.zscore(key,sign)
    if score:
        return False

    #4、新加入sign
    try:
        r.zadd(key, {sign: rtime})
    except Exception as e:
        print(e)
        return False
    else:
        return True


def delay_clear_one_time_nonce(key,rtime):
    #5、删除过期sign
    try:
        r.zremrangebyscore(key,0,rtime-1)
    except Exception as e:
        print(e)







