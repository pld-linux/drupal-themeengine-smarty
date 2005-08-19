%define		modname smarty
Summary:	Drupal Smarty theme engine
Name:		drupal-themeengine-%{modname}
Version:	4.6.0
Release:	0.3
Epoch:		0
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	d5fe39d4861f7e59cabddb1bc0f28c56
Patch0:		%{name}-PLD.patch
URL:		http://drupal.org/node/19248
Requires:	Smarty >= 2.6.2
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enginedir			%{_datadir}/drupal/themes/engines
%define		_cachedir			/var/cache/drupal

%description
A theme engine that allows you to use template files written using
Smarty Template Engine syntax.

The 'default' template for this engine is box_grey_smarty, which is
ported from the original box_grey theme.

%prep
%setup -q -n %{modname}
%patch0 -p1
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_enginedir}/%{modname}/plugins,%{_cachedir}/%{modname}}

install *.tpl $RPM_BUILD_ROOT%{_enginedir}/%{modname}
install *.engine *.php $RPM_BUILD_ROOT%{_enginedir}/%{modname}
install plugins/*.php $RPM_BUILD_ROOT%{_enginedir}/%{modname}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_enginedir}/%{modname}
%dir %attr(775,root,http) %{_cachedir}/%{modname}
