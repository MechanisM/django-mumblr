from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout
from mumblr.views.core import (recent_entries, tagged_entries, entry_detail, 
                               tag_cloud, archive, RssFeed, AtomFeed)
from mumblr.views.admin import (dashboard, delete_entry, add_entry, edit_entry,
                                delete_comment)

feeds = {
    'rss': RssFeed,
    'atom': AtomFeed,
}

urlpatterns = patterns('',
   url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
)

urlpatterns += patterns('',
    url('^$', recent_entries, name='recent-entries'),
    url('^(?P<page_number>\d+)/$', recent_entries, name='recent-entries'),
    url('^(\d{4}/\w{3}/\d{2})/([\w-]+)/$', entry_detail, name='entry-detail'),
    url('^tag/(?P<tag>[a-z0-9_-]+)/$', tagged_entries, name='tagged-entries'),
    url('^tag/(?P<tag>[a-z0-9_-]+)/(?P<page_number>\d+)/$', tagged_entries, 
        name='tagged-entries'),
    url('^archive/$', archive, name='archive'),
    url('^archive/(?P<page_number>\d+)/$', archive, name='archive'),
    url('^archive/(?P<entry_type>[a-z0-9_-]+)/$', archive, name='archive'),
    url('^archive/(?P<entry_type>[a-z0-9_-]+)/(?P<page_number>\d+)/$',
        archive, name='archive'),
    url('^tags/$', tag_cloud, name='tag-cloud'),
    url('^admin/$', dashboard, name='admin'),
    url('^admin/add/(\w+)/$', add_entry, name='add-entry'),
    url('^admin/edit/(\w+)/$', edit_entry, name='edit-entry'),
    url('^admin/delete/$', delete_entry, name='delete-entry'),
    url('^admin/delete-comment/$', delete_comment, name='delete-comment'),
    url('^admin/login/$', login, {'template_name': 'mumblr/admin/login.html'}, 
        name='log-in'),
    url('^admin/logout/$', logout, {'next_page': '/'}, name='log-out'),
    url('^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}, name='feeds'),
    url('^feed/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds, 'url': 'rss'}, name='feeds'),
    url('^(?P<permalink>.*)$', entry_detail),
)
