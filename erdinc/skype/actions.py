#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/"]

# Use dynamic skype in i686, static in x86_64
if "_" in get.srcVERSION():
    # Snapshot
    WorkDir = "skype"
else:
    # Upstream tarball
    WorkDir = "skype-%s" % get.srcVERSION()

def install():
    for data in ["avatars","lang","sounds"]:
        pisitools.insinto("/usr/share/skype",data)

    pisitools.dobin("skype")
    pisitools.rename("/usr/bin/skype", "skype.bin")

    if get.ARCH() == "x86_64":
        pisitools.domove("/usr/bin/skype.bin", "/usr/bin/32/")

    # Dbus config
    pisitools.insinto("/etc/dbus-1/system.d", "skype.conf")

    for size in ("16", "32", "48"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (size, size),
                          "icons/SkypeBlue_%sx%s.png" % (size, size),
                          "skype.png")

    pisitools.dodoc("README", "LICENSE")
