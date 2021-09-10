from rodasci.workflow import Workflow
import yaml
from pprint import pprint

from munch import munchify

with open('test.yaml') as wfy:
    wf = yaml.load(wfy, Loader=yaml.FullLoader)

pprint(wf)
print("========")
wf = munchify(wf)
workflow = Workflow(wf)
pprint(dict(workflow))