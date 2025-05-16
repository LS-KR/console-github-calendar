import json
import requests

levels = [
    "\033[48;2;238;238;238m  ",
    "\033[48;2;187;222;251m  ",
    "\033[48;2;100;181;246m  ",
    "\033[48;2;30;136;229m  ",
    "\033[48;2;13;71;161m  "
]

def getCalendar(username: str, week = 7):
    ret = ""
    if (week < 0) or (week > 52):
        return ret
    uri = f"https://gh-calendar.rschristian.dev/user/{username}"
    res = requests.get(uri)
    data = json.loads(res.content)
    contributions = data['contributions']
    weeks = contributions[-week - 1: -1]
    _max = 0
    for w in weeks:
        for d in w:
            if d['count'] > _max:
                _max = d['count']
    for i in range(0, 7):
        for w in weeks:
            if len(w) < i:
                continue
            d = w[i]
            count = d['count']
            if count == 0:
                ret += levels[0]
            else:
                ret += levels[int((count - 1) / _max * 3.9 + 1)]
        ret += "\033[0m\n"
    return ret

if __name__ == "__main__":
    print(getCalendar("LS-KR", 7))