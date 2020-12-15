#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : selenium
Version  : 3.141.0
Release  : 58
URL      : https://files.pythonhosted.org/packages/ed/9c/9030520bf6ff0b4c98988448a93c04fcbd5b13cd9520074d8ed53569ccfe/selenium-3.141.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/9c/9030520bf6ff0b4c98988448a93c04fcbd5b13cd9520074d8ed53569ccfe/selenium-3.141.0.tar.gz
Summary  : Python bindings for Selenium
Group    : Development/Tools
License  : Apache-2.0
Requires: selenium-license = %{version}-%{release}
Requires: selenium-python = %{version}-%{release}
Requires: selenium-python3 = %{version}-%{release}
Requires: urllib3
BuildRequires : buildreq-distutils3
BuildRequires : urllib3

%description
Selenium Client Driver
        ======================
        
        Introduction
        ============
        
        Python language bindings for Selenium WebDriver.
        
        The `selenium` package is used to automate web browser interaction from Python.
        
        +-----------+--------------------------------------------------------------------------------------+

%package license
Summary: license components for the selenium package.
Group: Default

%description license
license components for the selenium package.


%package python
Summary: python components for the selenium package.
Group: Default
Requires: selenium-python3 = %{version}-%{release}

%description python
python components for the selenium package.


%package python3
Summary: python3 components for the selenium package.
Group: Default
Requires: python3-core
Provides: pypi(selenium)
Requires: pypi(urllib3)

%description python3
python3 components for the selenium package.


%prep
%setup -q -n selenium-3.141.0
cd %{_builddir}/selenium-3.141.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133780
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/selenium
cp %{_builddir}/selenium-3.141.0/LICENSE %{buildroot}/usr/share/package-licenses/selenium/1f1b33b5dad017e44969d27e2dc819ecc279a498
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
rm -f %{buildroot}%{python_sitelib}/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{python_sitelib}/selenium/webdriver/firefox/x86/x_ignore_nofocus.so
## install_append end

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/selenium/1f1b33b5dad017e44969d27e2dc819ecc279a498

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
