from datetime import datetime, timezone
import zoneinfo

zones = (
    "Europe/Paris",
    "Europe/London",
    "Asia/Hong_Kong",
    "Africa/Nairobi",
)

# Get current time in UTC
# utc_now = datetime.now(tz=timezone.utc)
#
# for zone in zones:
#     tz = zoneinfo.ZoneInfo(zone)
#     required_time = utc_now.astimezone(tz)
#
#     city = zone.split('/')[1]
#     print(f"The time in {city} is {required_time}")


# Alternative Code
# for zone in zones:
#     tz = zoneinfo.ZoneInfo(zone)
#     required_time = datetime.now(tz=tz)
#
#     city = zone.split('/')[1]
#     print(f"The time in {city} is {required_time}")


locale_now = datetime.now()
# locale_now = locale_now.replace(microsecond=0)

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    required_time = locale_now.astimezone(tz)

    city = zone.split('/')[1]
    # print(f"The time in {city} is {required_time.strftime('%m/%d/%Y %H:%M:%S %z %Z')}")
    print(f"The time in {city} is {required_time} {required_time.tzname()}")
