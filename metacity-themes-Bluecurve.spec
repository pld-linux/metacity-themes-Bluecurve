Summary:	Bluecurve theme
Summary(pl.UTF-8):   Motyw Bluecurve
Name:		metacity-themes-Bluecurve
Version:	1.0
Release:	3
License:	GPL
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/metacity/MCity-Bluecurve.tar.bz2
# Source0-md5:	ff1d06be187d566a1e62d6c74fd28249
URL:		http://art.gnome.org/
Requires:	metacity
Conflicts:	metacity-theme-Bluecurve-redhat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluecurve theme for metacity.

%description -l pl.UTF-8
Motyw Bluecurve dla metacity.

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
