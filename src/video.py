import time, json, random
from math import floor, ceil
from src.utils import gaussian, get_random_tag, get_tag_mltprs
from src.youtuber import YouTuber
from src.tag import Tag

class Video:
    '''
    A data class to represent a video.
    
    Attributes
    ----------
    title: str
        Video's title
    video_time: int
        Video's length (in minutes)
    youtuber: YouTuber
        YouTuber that uploaded the video
    upload_time: int
        Time when the video was uploaded
    '''
    def __init__(self, title: str, video_time: int, youtuber: YouTuber, upload_time: int = 0):
        self.title = title
        self.upload_time = int(time.time()) if not upload_time else upload_time
        self.video_time = video_time
        self.youtuber = youtuber
        self.expiration = self.upload_time + max(20, 3*self.video_time)
        self.tags = self.__generate_tags()

    def __str__(self):
        return f"""'{self.title}'({self.video_time} mins) from {self.youtuber.username}
        """

    def get_video_information(self) -> str: 
        return json.dumps({
            "title": self.title, 
            "video_time": self.video_time,
            "upload_time": self.upload_time, 
            "youtuber_username": self.youtuber.username,
            "subscribers": self.youtuber.subscribers,
            "tag": self.tags[0].name,
            })

    def get_views(self, current_time = None) -> int:
        if not current_time:
            current_time=int(time.time()) 
        time_diff = current_time - self.upload_time
        max_views = int(self.youtuber.subscribers * self.youtuber.real_subs) // 2
        (x,y,z) = get_tag_mltprs(self.tags)
        views = x * gaussian(time_diff, y * self.video_time * 1.5, z * self.video_time) * max_views
        return max(0, random.randint(floor(min(views - 2, 0.9 * views)), ceil(max(views + 2, 1.1 * views))))
        
    def __generate_tags(self) -> None:
        main_tag = get_random_tag(self)
        if random.random() < 0.01:
            return [main_tag, Tag.HIT]
        elif random.random() < 0.01:
            return [main_tag, Tag.MISS]
        return [main_tag]