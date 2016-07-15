#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gstreamer-codecparsers
Version  : master
Release  : 1
URL      : https://github.com/01org/gstreamer-codecparsers/archive/master.tar.gz
Source0  : https://github.com/01org/gstreamer-codecparsers/archive/master.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0
Requires: gstreamer-codecparsers-lib
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : gstreamer-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(glib-2.0)
Patch1: build.patch

%description
No detailed description available

%package dev
Summary: dev components for the gstreamer-codecparsers package.
Group: Development
Requires: gstreamer-codecparsers-lib
Provides: gstreamer-codecparsers-devel

%description dev
dev components for the gstreamer-codecparsers package.


%package lib
Summary: lib components for the gstreamer-codecparsers package.
Group: Libraries

%description lib
lib components for the gstreamer-codecparsers package.


%prep
%setup -q -n gstreamer-codecparsers-master
%patch1 -p1

%build
export LANG=C
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/gstreamer-1.0/gst/codecparsers/gsth264parser.h
/usr/include/gstreamer-1.0/gst/codecparsers/gsth265parser.h
/usr/include/gstreamer-1.0/gst/codecparsers/gstjpegparser.h
/usr/include/gstreamer-1.0/gst/codecparsers/gstmpeg4parser.h
/usr/include/gstreamer-1.0/gst/codecparsers/gstmpegvideometa.h
/usr/include/gstreamer-1.0/gst/codecparsers/gstmpegvideoparser.h
/usr/include/gstreamer-1.0/gst/codecparsers/gstvc1parser.h
/usr/include/gstreamer-1.0/gst/codecparsers/gstvp8parser.h
/usr/include/gstreamer-1.0/gst/codecparsers/gstvp8rangedecoder.h
/usr/lib64/*.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
