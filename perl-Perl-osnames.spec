#
# spec file for package perl-Perl-osnames (Version 0.122)
#
# Copyright (c) 125 SUSE LLC
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
Version:        0.122
Release:        0%{?autorelease}
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        List possible $^O ($OSNAME) values, with description
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/%{cpan_name}-%{version}.tar.gz
Source1:     cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl-macros-suse
BuildRequires:  perl-generators
BuildRequires:  perl(Test::More) >= 0.98
%{?perl_requires}

%description
This package contains '$data' which lists possible values of '$^O' along
with description for each. It also provides some helper functions.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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
