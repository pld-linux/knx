%define	_snap	20060521
Summary:	KDE client for the NX Protocol
Summary(pl.UTF-8):	Klient KDE dla protokołu NX
Name:		knx
Version:	0.1
Release:	0.%{_snap}.2
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	16cb5e4e8145d723a6dd04f1bda384a8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	nxc-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
Requires:	nxproxy
Requires:	nxssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client for the NX Protocol. It can talk to the commercial/closed
source and the free NX authentication server.

%description -l pl.UTF-8
Klient protokołu NX. Potrafi komunikować się z komercyjnym (o
zamkniętych źródłach) jak i wolnodostępnym serwerem uwierzytelnienia
NX.

%prep
%setup -q -n %{name}

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	kdelnkdir=%{_desktopdir}/kde \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kicker/menuext/*.desktop
%{_datadir}/apps/knx
%{_iconsdir}/*/*/apps/*.png
%{_desktopdir}/kde/*.desktop
