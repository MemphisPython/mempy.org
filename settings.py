# -*- coding: utf-8 -*-
AUTHOR = u'The Memphis Python User Group'
SITENAME = u'MEMpy'
SITEURL = 'https://www.mempy.org'
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
DISPLAY_TAGS_ON_SIDEBAR = False
THEME = 'themes/pelican-bootstrap3'

USE_OPEN_GRAPH = True
TWITTER_CARDS = True
TWITTER_USERNAME = 'MemphisPython'
SOCIAL = (
    ('Meetup', 'https://www.meetup.com/memphis-technology-user-groups/'),
    ('Twitter', 'https://twitter.com/MemphisPython'),
    ('Facebook', 'https://facebook.com/MemphisPython'),
    ('Mailing List', 'https://bit.ly/mempy-google-group'),
    ('Email Us', 'mailto:brad@mempy.org'),
)

LINKS = (
    ('WebWorkers', 'https://memphiswebworkers.com/'),
    ('MemphisPHP', 'https://www.memphisphp.org/'),
    ('HACKmemphis', 'https://hackmemphis.com/'),
    ('MTF', 'https://memphistechnology.org'),
    ('PyTN', 'https://www.pytennessee.org/'),
)
GOOGLE_ANALYTICS = 'UA-46826960-1'

PATH = "content"
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['memtech', 'meetings', 'announcements']
STATIC_PATHS = ["logos"]

# Bootstrap3 theme options
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
USE_PAGER = True
BOOTSTRAP_THEME = 'united'
