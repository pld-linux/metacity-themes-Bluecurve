Summary:	Bluecurve theme
Summary(pl):	Motyw Bluecurve
Name:		metacity-theme-Bluecurve
Version:	1.0
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/metacity/MCity-Bluecurve.tar.bz2
URL:		http://art.gnome.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluecurve theme for Metacity.

%description -l pl
Motyw Bluecurve dla Metacity.

%prep
%setup -q -n Bluecurve

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/Bluecurve
cp -r metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/Bluecurve

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/Bluecurve/metacity-1
