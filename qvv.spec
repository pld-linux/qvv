Summary:	Image Viewer and Browser
Summary(pl):	Przegl�darka plik�w graficznych
Name:		qvv
Version:	0.19
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://cade.datamax.bg/qvv/%{name}-%{version}.tar.gz
# Source0-md5:	89d2ebbef88ec10889d4343e224e1794
URL:		http://cade.datamax.bg/qvv/
BuildRequires:	qt-devel >= 3
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QVV is image viewer based on TrollTech's Qt Toolkit! QVV is small,
simple, handy.

QVV is only few hundred lines of source code and handles as much file
formats as Qt does -- JPEG (all sorts of jpegs that jpeglib supports),
PNG, GIF, XPM and more...

QVV allows you to browse directories with lynx-like interface, view
images browse next/prev image while showing image window or in the
directory list, multiple image windows and directory browsers can be
opened/closed with a single key, panning easy with arrow keys or mouse
and few other things as well.

%description -l pl
QVV jest przegl�dark� plik�w graficznych opieraj�c� si� na narz�dziach
Qt TrollTecha! QVV jest niewielka, prosta i por�czna.

QVV to tylko kilka tysi�cy linijek kodu �r�d�owego a potrafi obs�u�y�
tyle format�w ile potrafi Qt -- JPEG (wszystkie te formaty, kt�re
obs�uguje jpeglib), PNG, GIF, XPM i inne...

QVV pozwoli ci przegl�da� katalogi w interfejsie w stylu lynxa,
przegl�da� kolejno obrazki w oknie obraz�w lub li�cie katalog�w.
Zbiorowe Okna obrazk�w i przegl�darki katalog�w mog� by� otwierane i
zamykane jednym klawiszem. �atwo nad tym zapanowa� strza�kami lub
myszk�, a par� innych dodatk�w r�wnie� mo�e pom�c.

%prep
%setup -q

%build
QTDIR=%{_prefix}
export QTDIR
qmake
%{__make} CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install qvv \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANFSCD HISTORY README
%attr(755,root,root) %{_bindir}/qvv
