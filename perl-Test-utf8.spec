%{?scl:%scl_package perl-Test-utf8}

Name:           %{?scl_prefix}perl-Test-utf8
Version:        1.01
Release:        17%{?dist}
Summary:        Handy utf8 tests
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-utf8
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKF/Test-utf8-%{version}.tar.gz
# Do not require author's dependencies
Patch0:         Test-utf8-1.01-Drop-useless-build-time-dependencies.patch
# Until the POD has changed, there is no point in regenerating README. This
# saves from a dependency on Module::Install::ReadmeFromPod.
Patch1:         Test-utf8-1.01-Do-no-regenerate-README.patch
Patch2:         Test-utf8-1.01-Use-Module-Install-from-tarball.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
%if ! (0%{?rhel}) && ! (0%{?scl:1})
BuildRequires:  %{?scl_prefix}perl(inc::Module::Install)
BuildRequires:  %{?scl_prefix}perl(Module::Install::Metadata)
BuildRequires:  %{?scl_prefix}perl(Module::Install::WriteAll)
BuildRequires:  sed
%else
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MM_Unix)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
%endif
# Module Runtime
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(charnames)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:  %{?scl_prefix}perl(Test::Builder::Tester) >= 0.09
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Runtime
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%{?perl_default_filter}

%description
This module is a collection of tests that's useful when dealing with utf8
strings in Perl.

%prep
%setup -q -n Test-utf8-%{version}
%patch0 -p1
%patch1 -p1

%if ! (0%{?rhel}) && ! (0%{?scl:1})
# Remove bundled modules
rm -rf ./inc/*
sed -i -e '/^inc\//d' MANIFEST
%else
%patch2 -p1
%endif

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::utf8.3*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-17
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-15
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-12
- Perl 5.28 rebuild

* Wed Apr 11 2018 Petr Pisar <ppisar@redhat.com> - 1.01-11
- Do not regenerate README

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-8
- Perl 5.26 rebuild

* Tue May 16 2017 Petr Pisar <ppisar@redhat.com> - 1.01-7
- Fix building on Perl without "." in @INC (CPAN RT#120706)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-2
- Perl 5.22 rebuild

* Wed Sep 24 2014 Paul Howarth <paul@city-fan.org> - 1.01-1
- Update to 1.01
  - Fix unnecessary warning caused by using /x (CPAN RT#88189,
    https://github.com/2shortplanks/Test-utf8/pull/2)
- Make %%files list more explicit
- Don't need to remove empty directories from the buildroot
- Don't use macros for commands
- Classify buildreqs by usage

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.00-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.00-2
- Perl 5.16 rebuild

* Tue Feb 21 2012 Iain Arnell <iarnell@gmail.com> 1.00-1
- update to latest upstream version
- converted to EU::MM

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 0.02-5
- Perl mass rebuild
- Remove now obsolete Buildroot and defattr

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Jun 26 2010 Iain Arnell <iarnell@gmail.com> 0.02-2
- drop explicit Test::Builder requires

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
