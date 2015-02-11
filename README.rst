mempy.org
=========

This is the website for the Memphis Python User group. It's
generated with pelican_. So, to publish content you'll need that.

You can get it with::

    pip install -r requirements.txt


How to add content
------------------

Content for the site is in the ``content`` directory, so to contribute a post,
just create a file.

* For monthly meeting information, create a ``content/meetings/YYYY-MM-DD.rst``
  file and add the appropriate content.
* For announcments, create a file in ``content/announcements/``.
* Stand-alone pages go in ``content/pages/``

Once you've added your new content, commit it and send a Pull Request.


How to publish content
----------------------

If you have access to the appropriate repo, here's what you do to publish:

1. Add the content (accept a PR or do the above)
2. Commit any changes
3. Run `make`.  This should update the MemphisPython.github.io submodule, build
   the html, push that back up to github, commit & push any leftover changes.
4. Profit?

.. _`pelican`: http://alexis.notmyidea.org/pelican/
