# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# Avoid circular dependency with trybuild
%bcond_with check
%global debug_package %{nil}

%global crate zerocopy-derive

Name:           rust-zerocopy-derive
Version:        0.7.35
Release:        1
Summary:        Custom derive for traits from the zerocopy crate
Group:          Development/Rust

License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/zerocopy-derive
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(proc-macro2/default) >= 1.0.1 with crate(proc-macro2/default) < 2.0.0~)
BuildRequires:  (crate(quote/default) >= 1.0.10 with crate(quote/default) < 2.0.0~)
BuildRequires:  (crate(syn/default) >= 2.0.31 with crate(syn/default) < 3.0.0~)
%if %{with check}
BuildRequires:  (crate(static_assertions/default) >= 1.1.0 with crate(static_assertions/default) < 2.0.0~)
BuildRequires:  crate(trybuild/default) >= 1.0.85
BuildRequires:  crate(trybuild/diff) >= 1.0.85
%endif

%global _description %{expand:
Custom derive for traits from the zerocopy crate.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy-derive) = 0.7.35
Requires:       (crate(proc-macro2/default) >= 1.0.1 with crate(proc-macro2/default) < 2.0.0~)
Requires:       (crate(quote/default) >= 1.0.10 with crate(quote/default) < 2.0.0~)
Requires:       (crate(syn/default) >= 2.0.31 with crate(syn/default) < 3.0.0~)
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-BSD
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy-derive/default) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy-derive) = 0.7.35

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
