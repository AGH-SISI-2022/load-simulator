import requests
from threading import Timer
from src.utils import normal_distribution, get_random_youtuber
from src.youtuber import YouTuber
from src.video import Video
from src.repeated_timer import RepeatedTimer

class LoadSimulator:
    def __init__(self, ip: str, send_period: int = 10, watch_period: int = 1, subscribers_mltpr: int = 1):
        self.ip = ip

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
        self.send_timer = RepeatedTimer(send_period, self.__send_video)
        self.view_videos = RepeatedTimer(watch_period, self.__view_videos)

    def __send_video(self) -> None:
        # make video for one of ytbers
        ytber = get_random_youtuber(self.youtubers)
        video_name = "test video" # TODO randomize it later
        video_time = normal_distribution(ytber.avg_video_time, ytber.avg_video_time//2, 1)
        video = Video(video_name, video_time, ytber)

        # save it 
        self.videos.append(video)

        # send video
        print(f'Sending video {video.title} from {ytber.username}')
        requests.post(f'{self.ip}/send', video.get_video_information())

        # add timer to remove it later
        Timer(max(20, 3 * video.video_time), self.__remove_video, [video]).start()

    def __view_videos(self) -> None:
        for v in self.videos:
            views = v.get_views()
            for _ in range(views):
                requests.post(f'{self.ip}/watch', v.get_video_information())

    def __remove_video(self, video: Video) -> None:
        try:
            self.videos.remove(video)
        except:
            print(f"Failed to remove {video} (shouldn't happen 🤣")