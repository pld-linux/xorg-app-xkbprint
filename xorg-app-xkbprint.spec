Summary:	xkbprint application to print XKB keyboard description
Summary(pl.UTF-8):	Aplikacja xkbprint do drukowania opisów klawiatur XKB
Name:		xorg-app-xkbprint
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xkbprint-%{version}.tar.bz2
# Source0-md5:	3d3eb10466442354d6b73b503b9829db
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbprint application generates a printable or encapsulated PostScript
description of an XKB keyboard description.

%description -l pl.UTF-8
Aplikacja xkbprint generuje z opisu klawiatury XKB opis w postaci
drukowalnego lub obudowanego PostScriptu.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xkbprint
%{_mandir}/man1/xkbprint.1*
