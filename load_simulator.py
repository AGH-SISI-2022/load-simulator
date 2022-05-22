import requests
import random
import json
from threading import Timer

class YouTuber: 
    def __init__(self, username, subscribers, real_subs, avg_video_time, upload_rate):
        self.username = username # YT-ber username
        self.subscribers = subscribers # number of subscribers channel has got
        self.real_subs = real_subs # % of real subscribers that tend to watch a YT-ber 
        self.avg_video_time = avg_video_time # avg time of video (in mins) that YT-ber posts
        self.upload_rate = upload_rate # upload rate of videos (based on average) - uploads per month

    def __str__(self):
        return f'''YouTuber {self.username} - {self.subscribers} subscribers
            {self.subscribers}% are real subscribers
            Average video time {self.avg_video_time}
            Averaging {self.upload_rate} videos a month'''

class Video:
    def __init__(self, title: str, video_time: int, youtuber: YouTuber):
        self.title = title
        self.video_time = video_time
        self.youtuber = youtuber

    def __str__(self):
        return f"""'{self.title}'({self.video_time} mins) from {self.youtuber.username}
        """

class RepeatedTimer:
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def __run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self.__run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class LoadSimulator:
    def __init__(self, ip):
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

        self.videos = []
        self.send_timer = RepeatedTimer(10, self.__send_video)
        self.view_videos = RepeatedTimer(2, self.__view_videos)

    def __get_random_youtuber(self) -> YouTuber:
        return random.choices(self.youtubers, [yt.upload_rate for yt in self.youtubers], k=1)[0]

    def __send_video(self) -> None:
        # make video for one of ytbers
        ytber = self.__get_random_youtuber()
        video_name = "test video" # randomize it later TODO
        video_time = ytber.avg_video_time # randomize it later TODO
        video = Video(video_name, video_time, ytber)

        # save it 
        self.videos.append(video)

        # send video
        print(f'Sending video {video.title} from {ytber.username}')
        requests.post(f'{self.ip}/send', json.dumps(video, default=lambda o: o.__dict__))

        # add timer to remove it later
        Timer(3 * video.video_time, self.__remove_video, [video]).start() # might change length how long video stays TODO

    def __view_videos(self) -> None:
        for v in self.videos:
            # make a requests in time function for videos TODO
            requests.post(f'{self.ip}/watch', json.dumps(v, default=lambda o: o.__dict__))

    def __remove_video(self, video: Video) -> None:
        try:
            self.videos.remove(video)
        except:
            print(f"Failed to remove {video} (shouldn't happen 🤣")

if __name__ == '__main__':
    load_simulator = LoadSimulator('http://127.0.0.1:8080')
