#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Async-Interrupt
Version  : 1.24
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Async-Interrupt-1.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Async-Interrupt-1.24.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libasync-interrupt-perl/libasync-interrupt-perl_1.24-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 BSD-2-Clause GPL-1.0 GPL-2.0
Requires: perl-Async-Interrupt-lib = %{version}-%{release}
Requires: perl-Async-Interrupt-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Canary::Stability)
BuildRequires : perl(common::sense)

%description
NAME
Async::Interrupt - allow C/XS libraries to interrupt perl asynchronously
SYNOPSIS
use Async::Interrupt;

%package dev
Summary: dev components for the perl-Async-Interrupt package.
Group: Development
Requires: perl-Async-Interrupt-lib = %{version}-%{release}
Provides: perl-Async-Interrupt-devel = %{version}-%{release}

%description dev
dev components for the perl-Async-Interrupt package.


%package lib
Summary: lib components for the perl-Async-Interrupt package.
Group: Libraries
Requires: perl-Async-Interrupt-license = %{version}-%{release}

%description lib
lib components for the perl-Async-Interrupt package.


%package license
Summary: license components for the perl-Async-Interrupt package.
Group: Default

%description license
license components for the perl-Async-Interrupt package.


%prep
%setup -q -n Async-Interrupt-1.24
cd ..
%setup -q -T -D -n Async-Interrupt-1.24 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Async-Interrupt-1.24/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Async-Interrupt
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Async-Interrupt/COPYING
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Async-Interrupt/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Async/Interrupt.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Async::Interrupt.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Async/Interrupt/Interrupt.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Async-Interrupt/COPYING
/usr/share/package-licenses/perl-Async-Interrupt/deblicense_copyright
