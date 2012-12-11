%define upstream_name    Term-ANSIScreen
%define upstream_version 1.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Term::ANSIScreen - Terminal control using ANSI escape sequences
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Term::ANSIScreen, a Term::ANSIColor clone with supports for
screen mode, cursor control and keyboard mapping sequences.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Term/ANSIScreen.pm
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.420.0-1mdv2010.0
+ Revision: 405538
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.42-6mdv2009.0
+ Revision: 241958
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.42-4mdv2008.0
+ Revision: 25455
- rebuild

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.42-3mdv2008.0
+ Revision: 23833
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.42-2mdk
- Fix SPEC according to Perl Policy
	-Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.42-1mdk
- initial Mandriva package

