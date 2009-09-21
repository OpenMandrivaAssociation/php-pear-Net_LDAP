%define		_class		Net
%define		_subclass	LDAP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - OO interface for searching and manipulating LDAP-entries
Name:		php-pear-%{_pearname}
Version:	1.1.5
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_LDAP/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{_pearname} is a clone of Perl's Net::LDAP object interface to
ldapservers. It does not contain all of Net::LDAP features (ldif
handling, schemas, etc), but has:
- a simple OO interface to connections, searches and entries
- support for TLS and ldap v3
- simple modification, deletion and creation of ldapentries

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install -m 644 %{_pearname}-%{version}/*.php \
    %{buildroot}%{_datadir}/pear/%{_class}
install -m 644 %{_pearname}-%{version}/%{_subclass}/*.php \
    %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install -d -m 755 %{buildroot}%{_datadir}/pear/packages
install -m 644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/doc
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml
