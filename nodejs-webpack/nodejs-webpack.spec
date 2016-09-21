%global modulename webpack
Name:           nodejs-%{modulename}
Version:        1.13.2
Release:        1%{?dist}
Summary:        Packs CommonJs/AMD modules for the browser

License:        MIT
URL:            https://github.com/webpack/webpack
Source0:        http://registry.npmjs.org/%{modulename}/-/%{modulename}-%{version}.tgz

BuildRequires:   nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Packs CommonJs/AMD modules for the browser.
Allows to split your codebase into multiple bundles, which can be loaded
on demand. Support loaders to preprocess files, i.e. json, jsx, es7, css,
less, ... and your custom stuff.

%prep
%setup -q -n package


%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modulename}
cp -pr bin buildin hot lib web_modules package.json %{buildroot}%{nodejs_sitelib}/%{modulename}/
%nodejs_symlink_deps

%files
%{nodejs_sitelib}/%{modulename}
%license LICENSE
%doc README.md

%changelog
* Tue Sep 20 2016 Sandro Bonazzola <sbonazzo@redhat.com>
- Initial packaging
