Summary:	Image Viewer and Browser
Summary(pl):	Przegl±darka plików graficznych
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
QVV jest przegl±dark± plików graficznych opieraj±c± siê na narzêdziach
Qt TrollTecha! QVV jest niewielka, prosta i porêczna.

QVV to tylko kilka tysiêcy linijek kodu ¼ród³owego a potrafi obs³u¿yæ
tyle formatów ile potrafi Qt -- JPEG (wszystkie te formaty, które
obs³uguje jpeglib), PNG, GIF, XPM i inne...

QVV pozwoli ci przegl±daæ katalogi w interfejsie w stylu lynxa,
przegl±daæ kolejno obrazki w oknie obrazów lub li¶cie katalogów.
Zbiorowe Okna obrazków i przegl±darki katalogów mog± byæ otwierane i
zamykane jednym klawiszem. £atwo nad tym zapanowaæ strza³kami lub
myszk±, a parê innych dodatków równie¿ mo¿e pomóc.

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
