%define		pearname	ClassLoader
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 ClassLoader Component
Name:		php-symfony2-ClassLoader
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/ClassLoader/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	4cc13be3aefae3b6a07b268ebc6c1298
URL:		http://symfony.com/doc/2.4/components/class_loader/index.html
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
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/ClassLoader
%{php_pear_dir}/Symfony/Component/ClassLoader/*.php
