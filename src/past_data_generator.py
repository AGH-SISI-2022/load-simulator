from datetime import datetime
from math import gcd
import csv
from src.utils import get_random_youtuber, normal_distribution, generate_title, youtubers
from src.video import Video

class PastDataGenerator: 
    def __init__(self, date_start, date_end, send_period, watch_period, subscribers_mltpr):

        self.youtubers = youtubers

        for ytber in self.youtubers:
            ytber.subscribers *= subscribers_mltpr

        self.videos = []
        self.videos_to_remove = []

        self.date_start = int(datetime.timestamp(datetime(*date_start)))
        self.date_end =  int(datetime.timestamp(datetime(*date_end)))
        
        step = gcd(send_period, watch_period)

        with open('data/requests_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['endpoint', 'current_time', 'title', 'video_time', 'upload_time', 'youtuber_username', 'subscribers', 'tag', 'request_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            while self.date_start < self.date_end:

                if self.date_start % send_period == 0:
                    ytber = get_random_youtuber(self.youtubers)
                    video_name = generate_title()
                    video_time = normal_distribution(ytber.avg_video_time, ytber.avg_video_time//2, 1)
                    video = Video(video_name, video_time, ytber, self.date_start)
                    self.videos.append(video)
                    self.write_row(writer, '/send', video, 1)
                    self.videos_to_remove.append((self.date_start + max(20, 3 * video.video_time), video))

                if self.date_start % watch_period == 0:
                    for v in self.videos:
                        views = v.get_views(self.date_start)
                        self.write_row(writer, '/watch', v, views)
                        
                for (date_time, vid) in self.videos_to_remove:
                    if self.date_start >= date_time:
                        self.videos_to_remove.remove((date_time, vid))
                        self.videos.remove(vid)

                self.date_start += step

    def write_row(self, writer, endpoint, v, views):
        writer.writerow({
            'endpoint': endpoint, 
            'current_time': self.date_start,
            'title': v.title, 
            'video_time': v.video_time, 
            'upload_time': v.upload_time,
            'youtuber_username': v.youtuber.username,
            'subscribers': v.youtuber.subscribers, 
            'tag': v.tags[0].name,
            'request_count': views
        })