import requests
from threading import Timer
from src.utils import normal_distribution, get_random_youtuber, youtubers
from src.video import Video
from src.repeated_timer import RepeatedTimer

class LoadSimulator:
    def __init__(self, ip: str, send_period: int = 10, watch_period: int = 1, subscribers_mltpr: int = 1):
        self.ip = ip

        self.youtubers = youtubers

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
            print(f'Sending {views} view requests for video from {v.youtuber.username}')
            for _ in range(views):
                requests.post(f'{self.ip}/watch', v.get_video_information())

    def __remove_video(self, video: Video) -> None:
        try:
            self.videos.remove(video)
        except:
            print(f"Failed to remove {video} (shouldn't happen 🤣")