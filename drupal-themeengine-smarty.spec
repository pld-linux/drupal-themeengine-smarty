%define		engine smarty
Summary:	Drupal Smarty theme engine
Summary(pl):	Silnik motywów Drupala Smarty
Name:		drupal-themeengine-%{engine}
Version:	4.6.0
Release:	0.11
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{engine}-%{version}.tar.gz
# Source0-md5:	d5fe39d4861f7e59cabddb1bc0f28c56
Patch0:		%{name}-PLD.patch
URL:		http://drupal.org/node/19248
Requires:	Smarty >= 2.6.10-4
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_enginedir	%{_drupaldir}/themes/engines
%define		_cachedir	/var/cache/drupal

%description
A theme engine that allows you to use template files written using
Smarty Template Engine syntax.

The 'default' template for this engine is box_grey_smarty, which is
ported from the original box_grey theme.

%description -l pl
Ten silnik motywów umo¿liwia u¿ywanie plików szablonów napisanych przy
u¿yciu sk³adni silnika szablonów Smarty.

"Domy¶lnym" szablonem dla tego silnika jest box_grey_smarty, który
jest sportowany z oryginalnego motywu box_grey.

%prep
%setup -q -n %{engine}
%patch0 -p1
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_enginedir}/%{engine}/plugins,%{_cachedir}/%{engine}}

install *.tpl $RPM_BUILD_ROOT%{_enginedir}/%{engine}
install *.engine *.php $RPM_BUILD_ROOT%{_enginedir}/%{engine}
install plugins/*.php $RPM_BUILD_ROOT%{_enginedir}/%{engine}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ "$1" = "0" ]; then
	# nuke cache
	rm -f %{_cachedir}/%{engine}/*.php
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%{_enginedir}/%{engine}
%dir %attr(775,root,http) %{_cachedir}/%{engine}
