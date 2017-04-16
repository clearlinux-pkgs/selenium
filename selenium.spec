#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : selenium
Version  : 3.3.3
Release  : 33
URL      : https://pypi.debian.net/selenium/selenium-3.3.3.tar.gz
Source0  : https://pypi.debian.net/selenium/selenium-3.3.3.tar.gz
Summary  : Python bindings for Selenium
Group    : Development/Tools
License  : Apache-2.0
Requires: selenium-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
======================
Selenium Client Driver
======================
Introduction
============

%package python
Summary: python components for the selenium package.
Group: Default

%description python
python components for the selenium package.


%prep
%setup -q -n selenium-3.3.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492372460
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
## make_install_append content
rm -f %{buildroot}%{python_sitelib}/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{python_sitelib}/selenium/webdriver/firefox/x86/x_ignore_nofocus.so
## make_install_append end

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
