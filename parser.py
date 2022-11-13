from feedparser import parse

latest_rss = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/miui-updates-tracker/master/rss/latest.xml"
rss = parse(latest_rss)
print(rss["entries"][0]["link"])
