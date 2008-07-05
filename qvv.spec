Summary:	Image Viewer and Browser
Summary(pl.UTF-8):	Przeglądarka plików graficznych
Name:		qvv
Version:	0.19
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://cade.datamax.bg/qvv/%{name}-%{version}.tar.gz
# Source0-md5:	89d2ebbef88ec10889d4343e224e1794
Source1:	%{name}.desktop
Source2:	%{name}.png
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

%description -l pl.UTF-8
QVV jest przeglądarką plików graficznych opierającą się na narzędziach
Qt TrollTecha! QVV jest niewielka, prosta i poręczna.

QVV to tylko kilka tysięcy linijek kodu źródłowego, a potrafi obsłużyć
tyle formatów, ile potrafi Qt: JPEG (wszystkie te formaty, które
obsługuje jpeglib), PNG, GIF, XPM i inne...

QVV pozwala przeglądać katalogi w interfejsie w stylu lynksa,
przeglądać kolejno obrazki w oknie obrazów lub liście katalogów.
Zbiorowe Okna obrazków i przeglądarki katalogów mogą być otwierane i
zamykane jednym klawiszem. Łatwo nad tym zapanować strzałkami lub
myszką, a parę innych dodatków również może pomóc.

%prep
%setup -q

%build
QTDIR=%{_prefix}
export QTDIR
qmake
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install qvv $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANFSCD HISTORY README
%attr(755,root,root) %{_bindir}/qvv
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
