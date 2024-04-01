# Import datetime, timezone
from datetime import datetime, timezone

# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat()) # 2017-10-01T15:26:26+00:00

# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone
# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours=11))

# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)

# Print results
print(dt.isoformat()) # 2017-10-01T15:26:26+11:00

# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start
  dt = trip['start']
  # Move dt to be in UTC
  dt = dt.astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())
  
# Original: 2017-10-01 15:23:25-04:00 | UTC: 2017-10-01T19:23:25+00:00
# Original: 2017-10-01 15:42:57-04:00 | UTC: 2017-10-01T19:42:57+00:00
# Original: 2017-10-02 06:37:10-04:00 | UTC: 2017-10-02T10:37:10+00:00
# Original: 2017-10-02 08:56:45-04:00 | UTC: 2017-10-02T12:56:45+00:00
# Original: 2017-10-02 18:23:48-04:00 | UTC: 2017-10-02T22:23:48+00:00
# Original: 2017-10-02 18:48:08-04:00 | UTC: 2017-10-02T22:48:08+00:00
# Original: 2017-10-02 19:18:10-04:00 | UTC: 2017-10-02T23:18:10+00:00
# Original: 2017-10-02 19:37:32-04:00 | UTC: 2017-10-02T23:37:32+00:00
# Original: 2017-10-03 08:24:16-04:00 | UTC: 2017-10-03T12:24:16+00:00
# Original: 2017-10-03 18:17:07-04:00 | UTC: 2017-10-03T22:17:07+00:00