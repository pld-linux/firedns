Summary:	FireDNS - library for handling asynchronous DNS requests
Summary(pl):	FireDNS - biblioteka do obs³ugi asynchronicznych zapytañ DNS
Name:		firedns
Version:	0.1.30
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://messagewall.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	0e18e14615036555183ee01b43fffd3c
URL:		http://messagewall.org/firedns.html
BuildRequires:	firestring-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfiredns is a library for handling asynchronous DNS requests. It
provides a very simple interface for sending requests and parsing
reponses, as well as low-timeout blocking functions. It can also be
compiled to override the BIND/LIBC functions with its alternative
implementations. libfiredns functions have much lower timeouts than
the stock functions and tend to be faster because they send requests
to all configured system nameservers at the same time.

%description -l pl
libfiredns to biblioteka do obs³ugi asynchronicznych zapytañ DNS.
Dostarcza bardzo prosty interfejs do wysy³ania zapytañ oraz
przetwarzania odpowiedzi, a tak¿e funkcje blokuj±ce z ma³ym timeoutem.
Mo¿e byæ tak¿e skompilowana tak, aby przykrywaæ funkcje BIND/LIBC
w³asnymi, alternatywnymi implementacjami. Funkcje libfiredns maj± du¿o
mniejsze timeouty ni¿ standardowe funkcje i powinny byæ szybsze,
poniewa¿ wysy³aj± zapytania do wszystkich skonfigurowanych serwerów
nazw jednocze¶nie.

%package devel
Summary:	Header files for firedns library
Summary(pl):	Pliki nag³ówkowe biblioteki firedns
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for firedns library.

%description devel -l pl
Pliki nag³ówkowe biblioteki firedns.

%package static
Summary:	Static firedns library
Summary(pl):	Statyczna biblioteka firedns
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static firedns library.

%description static -l pl
Statyczna biblioteka firedns.

%package utils
Summary:	FireDNS utilities
Summary(pl):	Narzêdzia FireDNS
Group:		Networking/Utilities
Requires:	%{name} = %{version}

%description utils
FireDNS utilities: fdnsip, fdnsname, fdnstxt.

%description utils -l pl
Narzêdzia FireDNS: fdnsip, fdnsname, fdnstxt.

%prep
%setup -q -n %{name}

%build
# it's FireMake, not autoconf-generated configure
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
./configure

%{__make} \
	SHAREDFLAGS="-shared -Wl,-soname=libfiredns.so"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INSTALL_USER="`id -u`" \
	INSTALL_GROUP="`id -g`"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS README
%attr(755,root,root) %{_libdir}/libfiredns.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/firedns.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfiredns.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fdns*
