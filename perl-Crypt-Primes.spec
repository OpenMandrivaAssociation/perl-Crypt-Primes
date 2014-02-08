%define upstream_name    Crypt-Primes
%define upstream_version 0.50

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Provable Prime Number Generator suitable for Cryptographic Application
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-Random
BuildArch:		noarch

%description
This module implements Ueli Maurer's algorithm for
generating large provable primes and secure parameters
for public-key cryptosystems. The generated primes are
almost uniformly distributed over the set of primes of
the specified bitsize and expected time for generation
is less than the time required for generating a
pseudo-prime of the same size with Miller-Rabin tests.
Detailed description and running time analysis of the
algorithm can be found in Maurer's paper[1].

Crypt::Primes is a pure perl implementation. It uses
Math::Pari for multiple precision integer arithmetic
and number theoretic functions. Random numbers are
gathered with Crypt::Random, a perl interface to
/dev/u?random devices found on most modern Unix operating
systems.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" echo | %__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_bindir}/largeprimes
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.500.0-5mdv2012.0
+ Revision: 765132
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.500.0-4
+ Revision: 763642
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.500.0-3
+ Revision: 676521
- rebuild

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.500.0-2
+ Revision: 653399
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2011.0
+ Revision: 406947
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.50-6mdv2009.0
+ Revision: 241196
- rebuild
- fix no-buildroot-tag
- kill (multiple!) definitions of %%buildroot on Pixel's request

* Mon Jun 25 2007 Buchan Milne <bgmilne@mandriva.org> 0.50-4mdv2008.0
+ Revision: 44159
- Rebuild


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 15:07:54 (58450)
- mkrel
- check section

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 15:01:12 (58442)
Import perl-Crypt-Primes

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.50-2mdk
- rebuild for new perl

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.50-1mdk
- New package

