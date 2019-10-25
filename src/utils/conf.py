import configparser


def get_conf():
    try:
        conf = configparser.ConfigParser()
        cfg_path = 'configs/config.ini'
        conf.read(cfg_path)
        return conf
    except Exception as e:
        print(e)
