#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : selenium
Version  : 3.13.0
Release  : 39
URL      : https://files.pythonhosted.org/packages/6d/4b/30b28589f2b6051b04d6f8014537749dc08fa787a5569cebb33e892d34d3/selenium-3.13.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/4b/30b28589f2b6051b04d6f8014537749dc08fa787a5569cebb33e892d34d3/selenium-3.13.0.tar.gz
Summary  : Python bindings for Selenium
Group    : Development/Tools
License  : Apache-2.0
Requires: selenium-python3
Requires: selenium-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Selenium Client Driver
        ======================
        
        Introduction
        ============
        
        Python language bindings for Selenium WebDriver.
        
        The `selenium` package is used to automate web browser interaction from Python.
        
        +-----------+--------------------------------------------------------------------------------------+

%package python
Summary: python components for the selenium package.
Group: Default
Requires: selenium-python3

%description python
python components for the selenium package.


%package python3
Summary: python3 components for the selenium package.
Group: Default
Requires: python3-core

%description python3
python3 components for the selenium package.


%prep
%setup -q -n selenium-3.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532239723
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## make_install_append content
rm -f %{buildroot}%{python_sitelib}/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{python_sitelib}/selenium/webdriver/firefox/x86/x_ignore_nofocus.so
## make_install_append end

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
