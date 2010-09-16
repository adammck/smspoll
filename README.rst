an Iraq Fit For Children: SMS Poll
==================================

This is the *SMS Poll* component of the `Iraq Fit For Children`_ project.

Starting in October of 2010, the UNICEF Iraq country office will be conducting an informal poll around the issues facing the children of Iraq. This `RapidSMS`_ project will be receiving the submissions via a shortcode and SMPP end-point generously provided by `Zain Iraq`_.

The results of the poll will be presented live on the website, along with our key messages, related media, guiding documents, and delicious visualizations of `MICS4`_ data.

.. _Iraq Fit For Children: http://iraqfitforchildren.org
.. _RapidSMS: http://github.com/rapidsms/rapidsms
.. _Zain Iraq: http://www.iq.zain.com
.. _MICS4: http://www.childinfo.org/mics4.html


Functionality
-------------

User sees a billboard which says something along the lines of::

  What is the most urgent need of children in your community?

    A: Clean Water and Sanitation
    B: Quality Health Care
    C: Nutritious Food
    D: Education
    E: Safety

  Send your answer to 12345.

User sends their answer over SMS. We're trying to be as forgiving as possible, so acceptable responses include::

  << A
  << BBB
  << 3
  << Education
  << EDU
  << Safety is the most urgent need.
  << We children need good food for life happy.

The user receives a confirmation, including an optional follow-up question. Something like::

  >> Thank you. 20% of Iraqis agree with you.
     What is your age, gender, and city or district?

Like the first time, we'll accept as many varieties of response that I can think of, off the top of my head::

  << 13
  << 14 Male
  << 15 Female Baghdad
  << Male 16
  << Mosul
  << Basra 17 F

The user receives a final confirmation, along with a key message, and an invitation to visit the website to learn more::

  >> Thank you. [Education] is important, because [blah blah blah].
     Learn more about this issue at http://iraqfitforchildren.org.


Installing
----------

This project is built upon `RapidSMS`_, which is available on PyPi. To give it a try, create a `virtualenv`_ and install the dependencies::

  $ virtualenv --no-site-packages rapidsms_dev
  $ source rapidsms_dev/bin/activate
  $ pip install rapidsms

Grab the latest source, and check that it works::

  $ git clone http://github.com/ysdoc/iffcpoll
  $ python smspoll/manage.py test

All being well, you can (optionally) update the settings for your environment, then run the RapidSMS router and the Django development server (in separate terminals) as usual::

  $ cd smspoll
  $ ./manage.py runrouter
  $ ./manage.py runserver

.. _virtualenv: http://pypi.python.org/pypi/virtualenv


License
-------

This project is free software, available under `the BSD license`_.

.. _the BSD license: http://github.com/ysdoc/iffcpoll/blob/master/LICENSE


Bugs
----

Please file bugs on `GitHub`_.

.. _GitHub: http://github.com/ysdoc/iffcpoll/issues
