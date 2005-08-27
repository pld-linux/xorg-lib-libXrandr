Summary:	X Randr extension library
Summary(pl):	Biblioteka rozszerzenia X Randr
Name:		xorg-lib-libXrandr
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXrandr-%{version}.tar.bz2
# Source0-md5:	1bf96aa604b2ecad9abff643a663f2e3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXrandr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Resize and Rotate extension library.

%description -l pl
Biblioteka rozszerzenia X Resize and Rotate, służącego do zmiany
rozmiaru i obracania ekranu X.

%package devel
Summary:	Header files libXrandr development
Summary(pl):	Pliki nagłówkowe do biblioteki libXrandr
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-proto-randrproto-devel
Obsoletes:	libXrandr-devel

%description devel
X Resize and Rotate extension library.

This package contains the header files needed to develop programs that
use these libXrandr.

%description devel -l pl
Biblioteka rozszerzenia X Resize and Rotate, służącego do zmiany
rozmiaru i obracania ekranu X.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXrandr.

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
Biblioteka rozszerzenia X Resize and Rotate, służącego do zmiany
rozmiaru i obracania ekranu X.

Pakiet zawiera statyczną bibliotekę libXrandr.

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libXrandr.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrandr.so
%{_libdir}/libXrandr.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xrandr.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXrandr.a
