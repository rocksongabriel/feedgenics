import feedparser
from schedule import every, repeat, run_pending
import time

def send_email():
    pass

@repeat(every(2).minutes)
def check_most_recent_feed():
    most_recent__url = "https://www.upwork.com/ab/feed/topics/rss?securityToken=2f5d5ccd155d0ed6da9d7645a7a421fd418dfbd3d61b4c516bf0367377c57f619ebc1852950b1f1d78e111c66f552da4eb3297b0beefa4d1c9b9d4b97883aac8&userUid=1492101406951632896&orgUid=1492101406951632897&topic=most-recent"
    rss = feedparser.parse(most_recent__url)

    number_of_last_entries = 2

    entries = rss.entries[:number_of_last_entries]

    for idx, entry in enumerate(entries):
        print(rss.feed.title)
        print(
            "======================================================================================"
        )
        print(f"---------entry {idx}---------")
        print(entry.title)
        print(entry.link)
        print("--------------------------------------------------------")


def main():
    while True:
        run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
