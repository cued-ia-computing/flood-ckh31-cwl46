# CUED Part IA Flood Warning System

This is the Part IA Lent Term computing activity at the Department of
Engineering, University of Cambridge.

The activity is documented at
https://cued-partia-flood-warning.readthedocs.io/. Fork this repository
to start the activity.

Criteria for flood warnings issued are as follows:
- Each MonitoringStation will have a risk index, which is derived from its
current water level and 6 predicted water levels 15 minutes, 1 hour, 2 hours,
6 hours, 12 hours and 24 hours after the previous measurement.
- Risk indice take discrete values from 0 to 7 which counts the total number
of the 7 water levels aforementioned exceeding the relative level of 0.8.
- Flood warnings are issued for towns. Each town has a risk index calculated
by the average risk index of all stations in the town, which has continuous
values from 0 to 7.
- Warnings are then issued according to the town's risk index. Risk indices
above or equal to 6 are classified as "severe"; those below 6 but above or
equal to 4 are classified as "high"; those below 4 but above or equal to 2
are classified as "moderate"; the rest of the towns with valid risk indices
are classified as "low"
- If none of the stations in the town can provide a valid risk index,
the town has invalid risk index. This may be due to inconsistent typical range,
no available latest level or no available past levels.