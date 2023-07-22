Summary:	Image Viewer and Browser
Summary(pl.UTF-8):	Przeglądarka plików graficznych
Name:		qvv
Version:	4.05
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	https://cade.noxrun.com/projects/qvv/%{name}-%{version}.tar.gz
# Source0-md5:	159be2b898a1d24ef9eb91cbac497623
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		https://cade.noxrun.com/projects/qvv/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 2.016
Requires(post,postun):	desktop-file-utils
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
cd src
%{qmake_qt5} qvv.qt5.pro
%{__make}

%install
cd src
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install qvv $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc ANFSCD HISTORY README
%attr(755,root,root) %{_bindir}/qvv
%{_desktopdir}/qvv.desktop
%{_pixmapsdir}/qvv.png
