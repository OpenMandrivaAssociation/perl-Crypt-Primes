Name:           perl-Crypt-Primes
Version:        0.50
Release:        %mkrel 6
License:        GPL or Artistic

%define realname        Crypt-Primes
Group:          Development/Perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:        Provable Prime Number Generator suitable for Cryptographic Application
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{realname}-%{version}.tar.bz2
Url:            http://www.cpan.org
Prefix:         %{_prefix}
BuildRequires:  perl-Crypt-Random
Requires:       perl
BuildArch:      noarch

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
%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README
%{_bindir}/largeprimes
%{perl_vendorlib}/*
%{_mandir}/*/*
