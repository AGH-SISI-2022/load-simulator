import configparser
from src.load_simulator import LoadSimulator
from src.past_data_generator import PastDataGenerator

if __name__ == '__main__':
    config_parser = configparser.ConfigParser()
    config_parser.read('config.ini')
    send_period = int(config_parser['requests']['send_period'])
    watch_period = int(config_parser['requests']['watch_period'])
    subscribers_mltpr = int(config_parser['requests']['subscribers_mltpr'])
    time_mltpr = int(config_parser['requests']['time_mltpr'])

    # generate old data
    # data_generator = PastDataGenerator((2020,1,1), (2020,1,2), send_period, watch_period, subscribers_mltpr, time_mltpr)

    # simulate load
    load_simulator = LoadSimulator('http://127.0.0.1:8080', send_period, watch_period, subscribers_mltpr, time_mltpr)
