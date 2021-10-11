import json

from CZMLWrapper import *
from datetime import datetime

time_start = datetime(2021, 1, 1, 0, 0, 0)
time_end = datetime(2021, 1, 1, 1, 30, 0)

billboard_packet = CZMLPacket(
    name="billboard",
    availability=(time_start, time_end),
    billboard=True,
    billboard_image="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACvSURBVDhPrZDRDcMgDAU9GqN0lIzijw6SUbJJygUeNQgSqepJTyHG91LVVpwDdfxM3T9TSl1EXZvDwii471fivK73cBFFQNTT/d2KoGpfGOpSIkhUpgUMxq9DFEsWv4IXhlyCnhBFnZcFEEuYqbiUlNwWgMTdrZ3JbQFoEVG53rd8ztG9aPJMnBUQf/VFraBJeWnLS0RfjbKyLJA8FkT5seDYS1Qwyv8t0B/5C2ZmH2/eTGNNBgMmAAAAAElFTkSuQmCC",
    billboard_scale=1.5,
    position=True,
    position_cartesian=[
        1216361.4096947117,
        -4736253.175342511,
        4081267.4865667094
    ],
    label=True,
    label_text="Label text"
).data

doc = CZMLDocument(
    name="billboard_example",
    interval=(time_start, time_end),
    packets=[billboard_packet]
).czml

print(doc)
