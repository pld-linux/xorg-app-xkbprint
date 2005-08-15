# $Rev: 3397 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xkbprint application
Summary(pl):	Aplikacja xkbprint
Name:		xorg-app-xkbprint
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xkbprint-%{version}.tar.bz2
# Source0-md5:	7e0042e2bc612b24fbef8e5f1a3e4b88
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xkbprint-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xkbprint application.

%description -l pl
Aplikacja xkbprint.


%prep
%setup -q -n xkbprint-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
