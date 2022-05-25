class YouTuber: 
    '''
    A data class to represent a YouTuber.
    
    Attributes
    ----------
    username: str
        YouTuber's username
    subscribers: int
        Number of subscribers channel has got
    real_subs: float
        Percentage of real subscribers (0.0-1.0]
    avg_video_time: int
        Average time of uploaded video by YouTuber
    upload_rate: int
        Average upload rate of videos - per month
    video_tags: [(Tag, float), (Tag, float), ...]
        Tags that YouTuber uses and their propabilities
    '''
    def __init__(self, username: str, subscribers: int, real_subs: float, avg_video_time: int, upload_rate: int, video_tags: list):
        self.username = username
        self.subscribers = subscribers
        self.real_subs = real_subs
        self.avg_video_time = avg_video_time
        self.upload_rate = upload_rate
        self.video_tags = video_tags

    def __str__(self):
        return f'''YouTuber {self.username} - {self.subscribers} subscribers
            {self.real_subs * 100}% are real subscribers
            Average video time {self.avg_video_time} min
            Averaging {self.upload_rate} videos a month'''