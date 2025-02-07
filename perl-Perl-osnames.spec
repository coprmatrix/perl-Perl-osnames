#
# spec file for package perl-Perl-osnames
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name Perl-osnames
Name:           perl-Perl-osnames
Version:        0.122.0
Release:        0
# 0.122 -> normalize -> 0.122.0
%define cpan_version 0.122
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        List possible $^O ($OSNAME) values, with description
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.98
Provides:       perl(Perl::osnames) = %{version}
BuildRequires:  (rpm-build-perl or perl-generators or %{_rpmconfigdir}/perl.req)

%undefine       __perllib_provides
BuildRequires:  perl-devel

%description
This package contains '$data' which lists possible values of '$^O' along
with description for each. It also provides some helper functions.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
