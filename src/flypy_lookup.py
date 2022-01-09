import json
import re
import sys

from ch2code import ch2code
from code2ch import code2ch


def lookup_by_code(code):
    temp = code2ch
    for c in code:
        temp = temp[c]
        if temp == None:
            break
    return temp['value'] or []


input = sys.argv[1]
input = input.strip()
isAlphanumeric = bool(re.match('^[a-zA-Z]+$', input))

pairs = []
if isAlphanumeric:
    for lookup in lookup_by_code(input):
        pairs.append(tuple((input, lookup)))
else:
    found = ch2code[input] or []
    for f in found:
        for lookup in lookup_by_code(f):
            pairs.append(tuple((f, lookup)))


items = []
for code,word in pairs:
    items.append({
        "type": "none",
        "title": f"{code} - {word}"
        # "subtitle": sub_title,
    })

flow = {
    "items": items
}
sys.stdout.write(json.dumps(flow, indent=3))
