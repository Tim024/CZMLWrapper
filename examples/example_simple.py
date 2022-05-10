import json

from ...CZMLWrapper import *
from datetime import datetime, timedelta

time_start = datetime(2021, 1, 1, 0, 0, 0)
time_end = datetime(2021, 1, 1, 0, 30, 0)

ground_station = CZMLPacket(
    name="ground_station",
    availability=(time_start, time_end),
    billboard=True,
    billboard_image="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACvSURBVDhPrZDRDcMgDAU9GqN0lIzijw6SUbJJygUeNQgSqepJTyHG91LVVpwDdfxM3T9TSl1EXZvDwii471fivK73cBFFQNTT/d2KoGpfGOpSIkhUpgUMxq9DFEsWv4IXhlyCnhBFnZcFEEuYqbiUlNwWgMTdrZ3JbQFoEVG53rd8ztG9aPJMnBUQf/VFraBJeWnLS0RfjbKyLJA8FkT5seDYS1Qwyv8t0B/5C2ZmH2/eTGNNBgMmAAAAAElFTkSuQmCC",
    billboard_scale=2,
    position=True,
    position_cartographicDegrees=[5.720074, 43.144623, 100],
    label=True,
    label_text="Ground Station"
)

satellite = CZMLPacket(
    name="satellite",
    availability=(time_start, time_end),
    billboard=True,
    billboard_image="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADJSURBVDhPnZHRDcMgEEMZjVEYpaNklIzSEfLfD4qNnXAJSFWfhO7w2Zc0Tf9QG2rXrEzSUeZLOGm47WoH95x3Hl3jEgilvDgsOQUTqsNl68ezEwn1vae6lceSEEYvvWNT/Rxc4CXQNGadho1NXoJ+9iaqc2xi2xbt23PJCDIB6TQjOC6Bho/sDy3fBQT8PrVhibU7yBFcEPaRxOoeTwbwByCOYf9VGp1BYI1BA+EeHhmfzKbBoJEQwn1yzUZtyspIQUha85MpkNIXB7GizqDEECsAAAAASUVORK5CYII=",
    billboard_scale=2,
    position=True,
    position_interpolation = True,
    position_dates=[time_start+i*timedelta(minutes=15) for i in range(2)],
    position_cartographicDegrees=[[-160, 50, 8000000],
                                  [80, 50, 10000000]],
    label=True,
    label_text="Satellite",
    path=True,
    path_leadTime=15*60,
    path_trailTime=15*60,
    path_material=True,
    path_material_color_rgbaf=[0.22,1,0.66,0.85]
)

link = CZMLPacket(
    name="connection",
    availability=(time_start+timedelta(minutes=10), time_end),
    polyline=True,
    polyline_arcType="NONE",
    polyline_positions=True,
    polyline_positions_reference=["satellite","ground_station"],
    polyline_material=True,
    polyline_material_color_rgbaf=[0,1,0,1]
)

doc = CZMLDocument(
    name="billboard_example",
    interval=(time_start, time_end),
    packets=[ground_station, satellite, link]
)

doc.save("../common/czml/current.czml")
