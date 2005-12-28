Summary:	X Randr extension library
Summary(pl):	Biblioteka rozszerzenia X Randr
Name:		xorg-lib-libXrandr
Version:	1.1.0.2
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/libXrandr-%{version}.tar.bz2
# Source0-md5:	9188bb611be2a67f9019208b27016670
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-randrproto-devel >= 0.99
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXrandr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Resize and Rotate extension library.

%description -l pl
Biblioteka rozszerzenia X Resize and Rotate, s³u¿±cego do zmiany
rozmiaru i obracania ekranu X.

%package devel
Summary:	Header files for libXrandr library
Summary(pl):	Pliki nag³ówkowe biblioteki libXrandr
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-proto-randrproto-devel >= 0.99
Obsoletes:	libXrandr-devel

%description devel
X Resize and Rotate extension library.

This package contains the header files needed to develop programs that
use libXrandr.

%description devel -l pl
Biblioteka rozszerzenia X Resize and Rotate, s³u¿±cego do zmiany
rozmiaru i obracania ekranu X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXrandr.

%package static
Summary:	Static libXrandr libraries
Summary(pl):	Biblioteki statyczne libXrandr
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXrandr-static

%description static
X Resize and Rotate extension library.

This package contains the static libXrandr library.

%description static -l pl
Biblioteka rozszerzenia X Resize and Rotate, s³u¿±cego do zmiany
rozmiaru i obracania ekranu X.

Pakiet zawiera statyczn± bibliotekê libXrandr.

%prep
%setup -q -n libXrandr-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXrandr.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrandr.so
%{_libdir}/libXrandr.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xrandr.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXrandr.a
