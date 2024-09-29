# SPECIAL rules

## Why do we need it?

As PyFunceble grew up, I thought that a bit of filtering for special cases
would be great to introduce. That where the idea came from.

## How does it work?

!!! note "Note"

    For any new suggestion of domains where a special rule can enhance
    PyFunceble please either open a new issue or make your
    `contribution <../contributing/index.html#contribute>`_ directly into the
    project.

!!! note "Note"

    **Contribution to the SPECIAL rules**

    To add directly to the special rules please modify both the source code
    `extra_rules.py <https://github.com/funilrys/PyFunceble/blob/dev/PyFunceble/checker/availability/extra_rules.py>`_
    and the documentation (here).

Below is the list of all special rules that are implemented into PyFunceble.
Please keep in mind that you can disable the usage those rules at any time.

------

### IP range

Any IPv4 and IPv6 ranges are supplied as `ACTIVE`.

------

### How to use it?

Special rules are activated by default, but you can switch its usage through:

- the (Python) API,
- the CLI argument,
- or, your configuration file.

------

### Parked Subjects

**WARNING:** This options is not available yet.

Any subjects that are considered parked by PyFunceble are supplied as `INACTIVE`.

------

### ChangeIP.com Platform domains

Any subjects that are part of the known ChangeIP.com platform domains which contain
`abuse.changeip.com.` in their `SOA` record are supplied as
`INACTIVE`.

Here is a rough list of the affected domains:

    - 25u.com
    - 2waky.com
    - 3-a.net
    - 4dq.com
    - 4pu.com
    - acmetoy.com
    - almostmy.com
    - americanunfinished.com
    - as19557.net
    - authorizeddns.net
    - authorizeddns.org
    - authorizeddns.us
    - b0tnet.com
    - bigmoney.biz
    - changeip.biz
    - changeip.co
    - changeip.net
    - changeip.org
    - changeip.us
    - cleansite.biz
    - cleansite.info
    - cleansite.us
    - ddns.info
    - ddns.mobi
    - ddns.ms
    - ddns.us
    - dhcp.biz
    - dns-dns.com
    - dns-report.com
    - dns-stuff.com
    - dns04.com
    - dns05.com
    - dns1.us
    - dns2.us
    - dnset.com
    - dnsfailover.net
    - dnsrd.com
    - dsmtp.biz
    - dsmtp.com
    - dubya.biz
    - dubya.info
    - dubya.net
    - dubya.us
    - dumb1.com
    - dynamic-dns.net
    - dynamicdns.biz
    - dynssl.com
    - edns.biz
    - esmtp.biz
    - ezua.com
    - faqserv.com
    - fartit.com
    - freeddns.com
    - freetcp.com
    - freewww.biz
    - freewww.info
    - ftp1.biz
    - ftpserver.biz
    - gettrials.com
    - got-game.org
    - gr8domain.biz
    - gr8name.biz
    - homingbeacon.net
    - https443.net
    - https443.org
    - ikwb.com
    - instanthq.com
    - iownyour.biz
    - iownyour.org
    - isasecret.com
    - itemdb.com
    - itsaol.com
    - jetos.com
    - jkub.com
    - jungleheart.com
    - justdied.com
    - lflink.com
    - lflinkup.com
    - lflinkup.net
    - lflinkup.org
    - longmusic.com
    - mefound.com
    - misecure.com
    - moneyhome.biz
    - mrbasic.com
    - mrbonus.com
    - mrface.com
    - mrslove.com
    - my03.com
    - mydad.info
    - myddns.com
    - myftp.info
    - mylftv.com
    - mymom.info
    - mynetav.com
    - mynetav.net
    - mynetav.org
    - mynumber.org
    - mypicture.info
    - mypop3.net
    - mypop3.org
    - mysecondarydns.com
    - mywww.biz
    - myz.info
    - ninth.biz
    - ns01.biz
    - ns01.info
    - ns01.us
    - ns02.biz
    - ns02.info
    - ns02.us
    - ns1.name
    - ns2.name
    - ns3.name
    - ocry.com
    - onedumb.com
    - onmypc.biz
    - onmypc.info
    - onmypc.net
    - onmypc.org
    - onmypc.us
    - organiccrap.com
    - otzo.com
    - ourhobby.com
    - port25.biz
    - proxydns.com
    - qhigh.com
    - qpoe.com
    - rebatesrule.net
    - sendsmtp.com
    - serveuser.com
    - serveusers.com
    - sexidude.com
    - sexxxy.biz
    - sixth.biz
    - squirly.info
    - ssl443.org
    - ssmailer.com
    - toh.info
    - toshibanetcam.com
    - toythieves.com
    - trickip.net
    - trickip.org
    - vizvaz.com
    - wikaba.com
    - www1.biz
    - wwwhost.biz
    - wwwhost.us
    - x24hr.com
    - xxuz.com
    - xxxy.biz
    - xxxy.info
    - ygto.com
    - youdontcare.com
    - yourtrap.com
    - zyns.com
    - zzux.com

------

### `*.000webhostapp.com`

Any subjects matching the given pattern and the `410` status code are
supplied as `INACTIVE`.

------

### `*.24.eu`

Any subjects matching the given pattern and the `503` status code are
supplied as `INACTIVE`.

------

### `*.altervista.org`

.. versionadded:: 4.1.0b13

Any subjects matching the given pattern and the `403` status code are
supplied as `INACTIVE`.

------

### `*.angelfire.com`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.blogspot.*`

Any subjects matching the given pattern and:

- the `404` status code
- the `301` status code that does not exists or are blocked by Google
- the `303` status code that are blocked by Google

are supplied as `INACTIVE`.

------

### `*.canalblog.com`

Any subjects matching the given pattern and the `404` status code
are supplied as `INACTIVE`.

------

### `*.dr.ag`

Any subjects matching the given pattern and the `503` status code
are supplied as `INACTIVE`.

------

### `*.fc2.com`

Any subjects matching the given pattern and the `error.fc2.com`
subdomain is into the `Location` headers are supplied as `INACTIVE`.

------

### `*.github.io`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.godaddysites.com`

Any subjects matching the given pattern and the `404` status codes are
supplied as `INACTIVE`.

------

### `*.hpg.com.br`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.imgur.com`

Any subjects matching the given pattern and:

    - the `/removed.png` path in the end URL (after redirect).

are supplied as `INACTIVE`.

------

### `*.liveadvert.com`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.skyrock.com`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.tumblr.com`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.weebly.com`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.wix.com`

Any subjects matching the given pattern and the `404` status code are
supplied as `INACTIVE`.

------

### `*.wordpress.com`

Any subjects matching the given pattern and the `301` status code along
with the pattern `doesn’t exist` are supplied as `INACTIVE`.
