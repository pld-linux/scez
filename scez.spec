Summary:	Smart Card Library
Summary(pl):	Biblioteka do obs³ugi kart procesorowych
Name:		scez
Version:	1.0
%define	snap	20020621
# this snap is newer than 1.0, so I use 1.snap not 0.snap
Release:	1.%{snap}.1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.franken.de/pub/crypt/chipcards/scez/%{name}-%{snap}.tar.gz
# Source0-md5:	8689a8e2148ab58c8a9e0b64fcca1f08
Patch0:		%{name}-amfix.patch
URL:		http://www.franken.de/crypt/scez.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCEZ is a library to make portable smart card development easier.

Supported readers:
- ACS ACR20S/Cybermouse (as far as this broken reader can be
  supported)
- Dumb Mouse
- Gemplus GCR410
- Intertex IX2
- Schlumberger Reflex62/64
- Towitoko Chipdrive
- and any reader supporting CT-API

Supported cards:
- ComCard MFC (mostly untested)
- GeldKarte
- Gemplus GPK4000 and GPK8000
- Giesecke & Devrient Smr@rtCafe
- GSM SIM card
- Proton
- Quick
- Schlumberger Cryptoflex, Cyberflex and Multiflex
- Telesec TCOS2
- ZeitControl BasicCard

%description -l pl
SCEZ to biblioteka u³atwiaj±ca tworzenie przeno¶nego oprogramowanie
u¿ywaj±cego kart procesorowych.

Obs³ugiwane czytniki:
- ACS ACR20S/Cybermouse (na tyle, na ile da siê obs³u¿yæ te u³omne
  czytniki)
- Dumb Mouse
- Gemplus GCR410
- Intertex IX2
- Schlumberger Reflex 62/64
- Towitoki Chipdrive
- oraz dowolny czytnik obs³uguj±cy CT-API

Obs³ugiwane karty:
- ComCard MFC (w wiêkszo¶ci nie testowane)
- GeldKarte
- Gemplus GPK4000 i GPK8000
- Giesecke & Devrient Smr@rtCafe
- karty SIM GSM
- Proton
- Quick
- Schlumberger Cryptoflex, Cyberflex i Multiflex
- Telesec TSOS2
- ZeitControl BasicCard

%package devel
Summary:	SCEZ header files
Summary(pl):	Pliki nag³ówkowe SCEZ
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
SCEZ header files.

%description devel -l pl
Pliki nag³ówkowe SCEZ.

%package static
Summary:	SCEZ static library
Summary(pl):	Biblioteka statyczna SCEZ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
SCEZ static library.

%description static -l pl
Biblioteka statyczna SCEZ.

%prep
%setup -q -n %{name}-%{snap}
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/scez

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd scez
install scacr20.h scbasiccard.h sccryptoflex.h scctapi.h sccyberflex.h \
	scdumbmouse.h scgcr400.h scgeldkarte.h scgeneral.h scgpk4000.h \
	scgsmsim.h scintertex.h scmfc.h scmultiflex.h scproton.h \
	scpts.h scquick.h screader.h screflex60.h scsmartcafe.h \
	scsmartcard.h sct0.h sct1.h sctcos.h sctowitoko.h \
	$RPM_BUILD_ROOT%{_includedir}/scez

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc COPYRIGHT COPYRIGHT.sio README README.sio VERSION.sio
%attr(755,root,root) %{_bindir}/bcupload
%attr(755,root,root) %{_bindir}/cafeman
%attr(755,root,root) %{_bindir}/cardcheck
%attr(755,root,root) %{_bindir}/cfupload
%attr(755,root,root) %{_bindir}/crdetect
%attr(755,root,root) %{_bindir}/cyflexman
%attr(755,root,root) %{_bindir}/flexpasswd
%attr(755,root,root) %{_bindir}/gendivkey
%attr(755,root,root) %{_bindir}/getcert
%attr(755,root,root) %{_bindir}/scanclains
%attr(755,root,root) %{_bindir}/scdir
%attr(755,root,root) %{_bindir}/scsh
%attr(755,root,root) %{_bindir}/scwait
%attr(755,root,root) %{_bindir}/simman
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_infodir}/*.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/scez

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
