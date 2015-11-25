%define		package	ClassLoader
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 ClassLoader Component
Name:		php-symfony2-ClassLoader
Version:	2.7.7
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	f917353e1b04067b3cf17b04873c6676
URL:		http://symfony.com/doc/2.7/components/class_loader/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(hash)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php-pear >= 4:1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ClassLoader Component loads your project classes automatically if
they follow some standard PHP conventions.

%prep
%setup -q -n class-loader-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/ClassLoader
%{php_pear_dir}/Symfony/Component/ClassLoader/*.php
