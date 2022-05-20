statuses = {
    "Ayla": "online",
    "Ardita": "online",
    "Mark": "offline"
}
def online_count(stats):
    return len([value for value in stats.values()
            if value == "online"])
print(online_count(statuses))            