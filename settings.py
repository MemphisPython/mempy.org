# -*- coding: utf-8 -*-
AUTHOR = u'The Memphis Python User Group'
SITENAME = u'MEMpy'
SITEURL = 'http://www.mempy.org'
DEFAULT_CATEGORY = u'meetings'
GITHUB_URL = 'https://github.com/MemphisPython'
PDF_GENERATOR = False
TIMEZONE = "America/Chicago"

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 2
TAG_CLOUD_MAX_ITEMS = 6
TAG_CLOUD_STEPS = 4
THEME = 'themes/pelican-bootstrap3'

TWITTER_USERNAME = 'MemphisPython'
SOCIAL = (
    ('Meetup', 'http://www.meetup.com/memphis-technology-user-groups/'),
    ('Twitter', 'http://twitter.com/MemphisPython'),
    ('Facebook', 'http://facebook.com/MemphisPython'),
    ('Google+', 'https://plus.google.com/+MempyOrg/'),
    ('Mailing List', 'http://bit.ly/mempy-google-group'),
    ('Email Us', 'mailto:brad@mempy.org'),
)

LINKS = (
    ('PyTN', 'https://www.pytennessee.org/'),
    ('MTF', 'http://memphistechnology.org'),
    ('HACKmemphis', 'http://hackmemphis.com/'),
)
GOOGLE_ANALYTICS = 'UA-46826960-1'

PATH = "content"
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['meetings', 'announcements']
STATIC_PATHS = ["logos"]

# Bootstrap3 theme options
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
USE_PAGER = True
