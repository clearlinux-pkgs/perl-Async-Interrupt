#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-Async-Interrupt
Version  : 1.26
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Async-Interrupt-1.26.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Async-Interrupt-1.26.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libasync-interrupt-perl/libasync-interrupt-perl_1.24-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 BSD-2-Clause GPL-1.0 GPL-2.0
Requires: perl-Async-Interrupt-license = %{version}-%{release}
Requires: perl-Async-Interrupt-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Canary::Stability)
BuildRequires : perl(common::sense)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Async::Interrupt - allow C/XS libraries to interrupt perl asynchronously
SYNOPSIS
use Async::Interrupt;

%package dev
Summary: dev components for the perl-Async-Interrupt package.
Group: Development
Provides: perl-Async-Interrupt-devel = %{version}-%{release}
Requires: perl-Async-Interrupt = %{version}-%{release}

%description dev
dev components for the perl-Async-Interrupt package.


%package license
Summary: license components for the perl-Async-Interrupt package.
Group: Default

%description license
license components for the perl-Async-Interrupt package.


%package perl
Summary: perl components for the perl-Async-Interrupt package.
Group: Default
Requires: perl-Async-Interrupt = %{version}-%{release}

%description perl
perl components for the perl-Async-Interrupt package.


%prep
%setup -q -n Async-Interrupt-1.26
cd %{_builddir}
tar xf %{_sourcedir}/libasync-interrupt-perl_1.24-1.debian.tar.xz
cd %{_builddir}/Async-Interrupt-1.26
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Async-Interrupt-1.26/deblicense/

%build
## build_prepend content
export PERL_CANARY_STABILITY_NOPROMPT=1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Async-Interrupt
cp %{_builddir}/Async-Interrupt-%{version}/COPYING %{buildroot}/usr/share/package-licenses/perl-Async-Interrupt/9a56f3b919dfc8fced3803e165a2e38de62646e5 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Async-Interrupt/619cb1524f067eb222c60e4e1513035e67e1a874 || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Async::Interrupt.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Async-Interrupt/619cb1524f067eb222c60e4e1513035e67e1a874
/usr/share/package-licenses/perl-Async-Interrupt/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
