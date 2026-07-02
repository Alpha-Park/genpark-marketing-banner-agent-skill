from client import MarketingBannerClient
def main():
    c = MarketingBannerClient()
    print(c.resolve_banner("summer", True))
if __name__ == '__main__':
    main()
