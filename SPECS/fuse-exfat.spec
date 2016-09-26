Name:	        fuse-exfat
Version:	1.2.4
Release:	1%{?dist}
Summary:	Free exFAT file system implementation

Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/relan/exfat
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/fuse-exfat-%{version}.tar.gz
#Source0:	https://dl.deskosproject.org/sources/fuse-exfat/

BuildRequires:	pkgconfig(fuse)

%description
This driver is the first free exFAT file system implementation with write support. exFAT is a simple file system created by Microsoft. It is intended to replace FAT32 removing some of it's limitations. exFAT is a standard FS for SDXC memory cards.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install INSTALL="install -p"


%files
%license COPYING
%{_sbindir}/mount.exfat-fuse
%{_sbindir}/mount.exfat
%{_mandir}/man8/mount.exfat-fuse.8*

%changelog
* Mon Sep 26 2016 Darío Córdova <dcordova@deskosproject.org> - 1.2.4-1
- Initial package for DeskOS.
