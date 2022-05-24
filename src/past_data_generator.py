from datetime import datetime
from math import gcd
import csv
from src.utils import get_random_youtuber, normal_distribution
from src.youtuber import YouTuber
from src.video import Video

class PastDataGenerator: 
    def __init__(self, date_start, date_end, send_period, watch_period, subscribers_mltpr):

        self.youtubers = [
            YouTuber('PewDiePie', 100, 0.2, 20, 15),
            YouTuber('Mark Rober', 40, 1.0, 20, 1),
            YouTuber('RATIRL', 10, 0.9, 15, 16),
            YouTuber('DIY Perks', 25, 0.95, 20, 1),
            YouTuber('Linus Tech Tips', 60, 0.3, 10, 30),
            YouTuber('Uwaga! Naukowy Bełkot', 15, 0.5, 18, 5),
            YouTuber('Thebausffs', 10, 1.0, 11, 12),
            YouTuber('LEC', 10, 0.5, 5, 10),
            YouTuber('TikTok ABC', 30, 0.8, 1, 50),
            YouTuber('ilmango', 20, 0.3, 10, 15),
        ]

        for ytber in self.youtubers:
            ytber.subscribers *= subscribers_mltpr

        self.videos = []
        self.videos_to_remove = []

        date_start = int(datetime.timestamp(datetime(*date_start)))
        date_end =  int(datetime.timestamp(datetime(*date_end)))
        
        step = gcd(send_period, watch_period)

        with open('data/requests_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['endpoint', 'current_time', 'title', 'video_time', 'upload_time', 'youtuber_username', 'subscribers', 'request_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            while date_start < date_end:

                if date_start % send_period == 0:
                    ytber = get_random_youtuber(self.youtubers)
                    video_name = "test video"
                    video_time = normal_distribution(ytber.avg_video_time, ytber.avg_video_time//2, 1)
                    video = Video(video_name, video_time, ytber)
                    self.videos.append(video)
                    writer.writerow({
                        'endpoint': '/send', 
                        'current_time': date_start,
                        'title': video.title, 
                        'video_time': video.video_time, 
                        'upload_time': video.upload_time,
                        'youtuber_username': video.youtuber.username,
                        'subscribers': video.youtuber.subscribers, 
                        'request_count': 1
                    })
                    self.videos_to_remove.append((date_start + max(20, 3 * video.video_time), video))

                if date_start % watch_period == 0:
                    for v in self.videos:
                        views = v.get_views()
                        writer.writerow({
                            'endpoint': '/watch', 
                            'current_time': date_start,
                            'title': v.title, 
                            'video_time': v.video_time, 
                            'upload_time': v.upload_time,
                            'youtuber_username': v.youtuber.username,
                            'subscribers': v.youtuber.subscribers, 
                            'request_count': views
                        })

                for (date_time, vid) in self.videos_to_remove:
                    if date_start >= date_time:
                        self.videos_to_remove.remove((date_time, vid))
                        self.videos.remove(vid)

                date_start += step