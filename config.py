#!/usr/bin/env python

ANALYTICS_ID = 'UA-30726750-12'

HOMEPAGE_URL = 'https://github.com/zhuzhuor/Unblock-Youku'

IGNORED_SHORT_URLS = frozenset([
    'favicon.ico', 'robots.txt', 'sitemap.xml', 'unit-test',
    'proxy.pac', 'ptoxy.', 'proxy,pac', 'prox.pac'  # user typos
])

SHORT_URL_MAPPING = {
    'check':        'http://ipservice.163.com/isFromMainland',
    'chrome':       'https://chrome.google.com/webstore/detail/unblock-youku/pdnfnkhpgegpcingjbfihlkjeighnddk/details',
    'chrome-bug':   'https://github.com/zhuzhuor/Unblock-Youku/issues/45#issuecomment-10457179',
    'coinbase':     'https://coinbase.com/?r=531f53c632f694d4b20000f9&utm_campaign=user-referral&src=referral-link',
    'contributors': 'https://github.com/zhuzhuor/Unblock-Youku/contributors',
    'crx':          'https://clients2.google.com/service/update2/crx?response=redirect&x=id%3Dpdnfnkhpgegpcingjbfihlkjeighnddk%26uc',
    'custom':       'https://github.com/zhuzhuor/Unblock-Youku/wiki/Custom-backend-server-for-the-redirection-mode',
    'dns':          'https://github.com/zhuzhuor/Unblock-Youku/issues/112',
    'donate':       'https://coinbase.com/checkouts/1fd2ffdb109c17a9e7bacaa116d3dbc8',
    'faq':          'https://github.com/zhuzhuor/Unblock-Youku/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95-FAQ',
    'feedback':     'https://zhuzhuor.wufoo.com/forms/z7x3p9/',
    'flash':        'https://github.com/zhuzhuor/Unblock-Youku/issues/209',
    'github':       'https://github.com/zhuzhuor/Unblock-Youku',
    'httpbin':      'http://httpbin.org/',  # for testing
    'malicious':    'https://github.com/zhuzhuor/Unblock-Youku/wiki/%E6%81%B6%E6%84%8F%E6%89%A9%E5%B1%95%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8%E5%8F%8A%E7%94%84%E5%88%AB%E5%8A%9E%E6%B3%95',
    'modes':        'https://github.com/zhuzhuor/Unblock-Youku/wiki/%E8%BF%90%E8%A1%8C%E6%A8%A1%E5%BC%8F%E7%9A%84%E4%BB%8B%E7%BB%8D%E5%92%8C%E5%8C%BA%E5%88%AB',
    'proxy':        'https://github.com/zhuzhuor/Unblock-Youku/wiki/%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%AE%BE%E7%BD%AE%E7%A4%BA%E4%BE%8B',
    'reviews':      'https://chrome.google.com/webstore/detail/unblock-youku/pdnfnkhpgegpcingjbfihlkjeighnddk/reviews',
    'screenshots':  'https://github.com/zhuzhuor/Unblock-Youku/wiki/%E5%B8%B8%E7%94%A8%E9%A1%B5%E9%9D%A2%E6%88%AA%E5%9B%BE%E7%A4%BA%E4%BE%8B',
    'share2facebook': 'https://www.facebook.com/sharer/sharer.php?u=https://chrome.google.com/webstore/detail/unblock-youku/pdnfnkhpgegpcingjbfihlkjeighnddk/',
    'share2plus':   'https://plusone.google.com/_/+1/confirm?url=https://chrome.google.com/webstore/detail/unblock-youku/pdnfnkhpgegpcingjbfihlkjeighnddk/',
    'share2renren': 'http://share.renren.com/share/buttonshare.do?link=https://chrome.google.com/webstore/detail/unblock-youku/pdnfnkhpgegpcingjbfihlkjeighnddk/',
    'share2twitter': 'https://twitter.com/intent/tweet?url=https://chrome.google.com/webstore/detail/unblock-youku/pdnfnkhpgegpcingjbfihlkjeighnddk/',
    'share2weibo':  'http://service.weibo.com/share/share.php?url=https://chrome.google.com/webstore/detail/unblock-youku/pdnfnkhpgegpcingjbfihlkjeighnddk/',
    'squid':        'https://github.com/zhuzhuor/Unblock-Youku/wiki/%E8%AE%A9Squid%E5%B8%A6%E6%9C%89Unblock-Youku%E5%8A%9F%E8%83%BD',
    'support_us':   'https://github.com/zhuzhuor/Unblock-Youku/wiki/Support-Us',
    'translators':  'https://webtranslateit.com/en/projects/4902-Unblock-Youku/top_translators',
    'viglink':      'https://github.com/zhuzhuor/Unblock-Youku/issues/47',
    'viglink.com':  'http://www.viglink.com/?vgref=140371'
}


def main():
    keys = set(SHORT_URL_MAPPING.keys())
    vals = set(SHORT_URL_MAPPING.values())
    assert len(keys) == len(vals)


if __name__ == '__main__':
    main()
