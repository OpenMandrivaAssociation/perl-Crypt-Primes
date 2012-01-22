%define upstream_name    Crypt-Primes
%define upstream_version 0.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    Provable Prime Number Generator suitable for Cryptographic Application
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-Crypt-Random
BuildArch:      noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/largeprimes
%{perl_vendorlib}/*
%{_mandir}/*/*
