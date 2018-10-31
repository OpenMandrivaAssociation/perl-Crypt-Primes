%define modname	Crypt-Primes
%define modver	0.50

Summary:	Provable Prime Number Generator suitable for Cryptographic Application
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	17
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-Random

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
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man1/*
%{_mandir}/man3/*

