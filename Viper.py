import argparse
from modules.info_disclosure import Info_disclosure


class Viper():
    """
    """
    def __init__(self):
        pass


def main():
    viper = Viper()
    parser = argparse.ArgumentParser(description="Web Recon Script")
    parser.add_argument('-u', '--url', type=str, help='URL', required=True)
    args = parser.parse_args()
    target = args.url
    i = Info_disclosure()
    i.robots(target)

if __name__ == '__main__':
        main()
