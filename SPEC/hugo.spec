%define debug_package %{nil}
%define repo github.com/gohugoio/hugo
Name:           hugo
Version:        0.89.4
Release:        1%{?dist}
Summary:        A Fast and Flexible Static Site Generator

Group:          Applications/System
License:        Apache 2.0
URL:            https://%{repo}
Source0:        https://%{repo}/archive/v%{version}.tar.gz

BuildRequires:  git golang

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

%prep
mkdir -p %{_builddir}/src/github.com/gohugoio/
cd %{_builddir}/src/github.com/gohugoio/
tar -xvzf %{_sourcedir}/v%{version}.tar.gz 
mv hugo-%{version} hugo
cd hugo

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/gohugoio/hugo
export GO111MODULE=on 
go get github.com/magefile/mage
mage hugo
mage install
cd %{_builddir}
%{_builddir}/bin/hugo gen autocomplete --completionfile hugo-completion
%{_builddir}/bin/hugo gen man

%install
install -d -p %{buildroot}%{_bindir}
install -Dp -m 0755 %{_builddir}/bin/hugo %{buildroot}%{_bindir}
install -Dp %{_builddir}/hugo-completion %{buildroot}%{_datadir}/bash-completion/completions/hugo
install -Dp %{_builddir}/man/* -t %{buildroot}%{_mandir}/man1

%files
%{_bindir}/hugo
%{_datadir}/bash-completion/completions/hugo
%{_mandir}/man1/*.1*

%changelog
* Wed Nov 17 2021 Martin Vlcek <martin@dontfreakout.eu> 0.89.4-1
- Fix content dir resolution when main project is a Hugo Module
* Tue Nov 16 2021 Martin Vlcek <martin@dontfreakout.eu> 0.89.3-1
- bug-fix release
* Wed Nov 10 2021 Martin Vlcek <martin@dontfreakout.eu> 0.89.2-1
- Fix path resolution in hugo new
- deps update
* Sat Nov 6 2021 Martin Vlcek <martin@dontfreakout.eu> 0.89.1-4
- added man pages and bash completion
- Details at https://github.com/gohugoio/hugo/releases/tag/v0.89.1
* Tue Nov 2 2021 Martin Vlcek <martin@dontfreakout.eu> 0.89.0-1
- All changes at https://github.com/gohugoio/hugo/releases/tag/v0.89.0
* Wed Sep 15 2021 Martin Vlcek <martin@dontfreakout.eu> 0.88.0-1
- Cloned SPEC file from https://copr.fedorainfracloud.org/coprs/daftaupe/hugo/ 
- by Pierre-Alain TORET <pierre-alain.toret@protonmail.com> to release version 0.88.0