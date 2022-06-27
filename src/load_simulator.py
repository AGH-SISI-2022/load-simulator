import grequests, csv, time
from threading import Timer, Thread
from src.utils import normal_distribution, get_random_youtuber, generate_title, youtubers
from src.video import Video
from src.repeated_timer import RepeatedTimer

class LoadSimulator:
    def __init__(self, ip: str, send_period: int = 10, watch_period: int = 1, subscribers_mltpr: int = 1, time_mltpr: int = 1):
        self.ip = ip
        self.send_period = send_period
        self.watch_period = watch_period
        self.subscribers_mltpr = subscribers_mltpr
        self.time_mltpr = time_mltpr

        self.youtubers = youtubers

        for ytber in self.youtubers:
            ytber.subscribers *= subscribers_mltpr
            ytber.avg_video_time *= time_mltpr

        self.videos = []
        self.send_timer = RepeatedTimer(send_period, self.__send_video)
        self.view_videos = RepeatedTimer(watch_period, self.__view_videos)
        with open('resp_times.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'requests count', 'avg response time', 'min response time', 'max response time'])

    def __get_response_times(self, rs, req_times) -> None:
        for resp in grequests.imap(rs, size=10):
            req_times.append(resp.elapsed.total_seconds())

    def __get_response_time_stats(self, tm, req_times, req_threads):
        for t in req_threads:
            t.join()
        with open('resp_times.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([tm, len(req_times), sum(req_times)/len(req_times), min(req_times), max(req_times)])

    def __send_video(self) -> None:
        # make video for one of ytbers
        ytber = get_random_youtuber(self.youtubers)
        video_name = generate_title()
        video_time = normal_distribution(ytber.avg_video_time, ytber.avg_video_time//2, 1)
        video = Video(video_name, video_time, ytber)

        # save it 
        self.videos.append(video)

        # send video
        print(f'Sending video {video.title} from {ytber.username}')
        rs = (grequests.post(f'{self.ip}/send', data=video.get_video_information()), )
        grequests.map(rs)

        # add timer to remove it later
        Timer(max(20*self.time_mltpr, 3 * video.video_time), self.__remove_video, [video]).start()

    def __view_videos(self) -> None:
        if not self.videos:
            return

        req_times = []
        req_threads = []
        tm = int(time.time())
        for v in self.videos:
            views = v.get_views()
            print(f'Sending {views} view requests for video from {v.youtuber.username}')
            rs = (grequests.post(f'{self.ip}/watch', data=v.get_video_information()) for _ in range(views))
            t = Thread(target=self.__get_response_times, args=(rs,req_times,))
            t.start()
            req_threads.append(t)

        Thread(target=self.__get_response_time_stats, args=(tm, req_times, req_threads, )).start()

    def __remove_video(self, video: Video) -> None:
        try:
            self.videos.remove(video)
        except:
            print(f"Failed to remove {video} (shouldn't happen 🤣)")