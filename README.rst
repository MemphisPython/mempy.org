mempy.org
=========

This is the website for the Memphis Python User group. It's
generated with pelican_. So, to publish content you'll need that.

You can get it with::

    pip install -r requirements.txt


contributing
------------

Content for the site is in the ``content`` directory, so to contribute a post,
just create a file.

* For monthly meeting information, create a ``content/meetings/YYYY-MM-DD.rst``
  file and add the appropriate content.
* For announcments, create a file in ``content/announcements/``.
* Stand-alone pages go in ``content/pages/``

Once you've added your new content, commit it and send a Pull Request.


.. _`pelican`: http://alexis.notmyidea.org/pelican/
