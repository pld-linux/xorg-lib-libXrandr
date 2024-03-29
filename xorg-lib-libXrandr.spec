Summary:	X Randr extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Randr
Name:		xorg-lib-libXrandr
Version:	1.5.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.xz
# Source0-md5:	24e0b72abe16efce9bf10579beaffc27
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-randrproto-devel >= 1.5
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
Obsoletes:	libXrandr < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Resize and Rotate extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X Resize and Rotate, służącego do zmiany
rozmiaru i obracania ekranu X.

%package devel
Summary:	Header files for libXrandr library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXrandr
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-proto-randrproto-devel >= 1.5
Obsoletes:	libXrandr-devel < 1.1

%description devel
X Resize and Rotate extension library.

This package contains the header files needed to develop programs that
use libXrandr.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X Resize and Rotate, służącego do zmiany
rozmiaru i obracania ekranu X.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXrandr.

%package static
Summary:	Static libXrandr libraries
Summary(pl.UTF-8):	Biblioteki statyczne libXrandr
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXrandr-static < 1.1

%description static
X Resize and Rotate extension library.

This package contains the static libXrandr library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X Resize and Rotate, służącego do zmiany
rozmiaru i obracania ekranu X.

Pakiet zawiera statyczną bibliotekę libXrandr.

%prep
%setup -q -n libXrandr-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXrandr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXrandr.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrandr.so
%{_libdir}/libXrandr.la
%{_includedir}/X11/extensions/Xrandr.h
%{_pkgconfigdir}/xrandr.pc
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXrandr.a
