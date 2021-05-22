#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-bareword-filehandles
Version  : 0.007
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/bareword-filehandles-0.007.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/bareword-filehandles-0.007.tar.gz
Summary  : 'disables bareword filehandles'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-bareword-filehandles-license = %{version}-%{release}
Requires: perl-bareword-filehandles-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::OP::Check::Install::Files)
BuildRequires : perl(ExtUtils::Depends)

%description
NAME
bareword::filehandles - disables bareword filehandles
VERSION
version 0.007

%package dev
Summary: dev components for the perl-bareword-filehandles package.
Group: Development
Provides: perl-bareword-filehandles-devel = %{version}-%{release}
Requires: perl-bareword-filehandles = %{version}-%{release}

%description dev
dev components for the perl-bareword-filehandles package.


%package license
Summary: license components for the perl-bareword-filehandles package.
Group: Default

%description license
license components for the perl-bareword-filehandles package.


%package perl
Summary: perl components for the perl-bareword-filehandles package.
Group: Default
Requires: perl-bareword-filehandles = %{version}-%{release}

%description perl
perl components for the perl-bareword-filehandles package.


%prep
%setup -q -n bareword-filehandles-0.007
cd %{_builddir}/bareword-filehandles-0.007

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-bareword-filehandles
cp %{_builddir}/bareword-filehandles-0.007/LICENSE %{buildroot}/usr/share/package-licenses/perl-bareword-filehandles/8c974f0cc608934d7d9151d1c6a30369cd34b64d
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
/usr/share/man/man3/bareword::filehandles.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-bareword-filehandles/8c974f0cc608934d7d9151d1c6a30369cd34b64d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/bareword/filehandles/filehandles.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/bareword/filehandles.pm
