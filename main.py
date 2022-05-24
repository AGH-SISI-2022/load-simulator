import configparser
from src.load_simulator import LoadSimulator

if __name__ == '__main__':
    config_parser = configparser.ConfigParser()
    config_parser.read('config.ini')
    send_period = int(config_parser['requests']['send_period'])
    watch_period = int(config_parser['requests']['watch_period'])
    subscribers_mltpr = int(config_parser['requests']['subscribers_mltpr'])
    load_simulator = LoadSimulator('http://127.0.0.1:8080', send_period, watch_period, subscribers_mltpr)
