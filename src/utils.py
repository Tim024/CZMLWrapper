ISO8601_FORMAT_Z = "%Y-%m-%dT%H:%M:%SZ"  # TODO: Add milliseconds?


def name_to_id(name):
    return str(name).lower().replace(' ', '_')


def format_date(date) -> str:
    return date.strftime(ISO8601_FORMAT_Z)


def format_interval(date1, date2) -> str:
    return date1.strftime(ISO8601_FORMAT_Z) + "/" + date2.strftime(ISO8601_FORMAT_Z)


def check_equal(dict, key, value):
    if key in dict.keys():
        if dict[key] == value:
            return True
    return False

