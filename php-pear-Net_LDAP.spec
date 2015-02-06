%define		_class		Net
%define		_subclass	LDAP
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.5
Release:	7
Summary:	OO interface for searching and manipulating LDAP-entries
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_LDAP/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
%{upstream_name} is a clone of Perl's Net::LDAP object interface to
ldapservers. It does not contain all of Net::LDAP features (ldif
handling, schemas, etc), but has:
- a simple OO interface to connections, searches and entries
- support for TLS and ldap v3
- simple modification, deletion and creation of ldapentries

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/doc/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-5mdv2012.0
+ Revision: 742152
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-4
+ Revision: 679451
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-3mdv2011.0
+ Revision: 613731
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.5-2mdv2010.1
+ Revision: 469029
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.5-1mdv2010.0
+ Revision: 446485
- new version
- drop path patch
- spec cleanup

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-3mdv2010.0
+ Revision: 441468
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2mdv2009.1
+ Revision: 322491
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.3-1mdv2009.1
+ Revision: 305831
- new version
  rediff patch
  don't duplicate spec-helper job
  don't look for non-existing cvs files

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2mdv2009.0
+ Revision: 236989
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-1mdv2008.0
+ Revision: 26232
- fix build
- 0.7.2

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdv2008.0
+ Revision: 15886
- rediffed P0
- 0.7.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-7mdv2007.0
+ Revision: 82356
- Import php-pear-Net_LDAP

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-1mdk
- initial Mandriva package (PLD import)

