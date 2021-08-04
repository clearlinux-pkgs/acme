#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4D17C995CD9775F2 (letsencrypt-client@eff.org)
#
Name     : acme
Version  : 1.18.0
Release  : 104
URL      : https://files.pythonhosted.org/packages/f2/92/90e11aca04a6d2a11e355c2ac8e14debf7224c1d7d71e472405eb06db0c2/acme-1.18.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f2/92/90e11aca04a6d2a11e355c2ac8e14debf7224c1d7d71e472405eb06db0c2/acme-1.18.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/f2/92/90e11aca04a6d2a11e355c2ac8e14debf7224c1d7d71e472405eb06db0c2/acme-1.18.0.tar.gz.asc
Summary  : ACME protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: acme-license = %{version}-%{release}
Requires: acme-python = %{version}-%{release}
Requires: acme-python3 = %{version}-%{release}
Requires: chardet
Requires: cryptography
Requires: josepy
Requires: pyOpenSSL
Requires: pytz
Requires: requests
Requires: requests-toolbelt
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : chardet
BuildRequires : cryptography
BuildRequires : josepy
BuildRequires : ndg_httpsclient-python
BuildRequires : pyOpenSSL
BuildRequires : pyRFC3339-python
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : python-mock-python
BuildRequires : pytz
BuildRequires : requests
BuildRequires : requests-python
BuildRequires : requests-toolbelt
BuildRequires : setuptools
BuildRequires : six-python

%description
python -m acme.standalone -p 1234
curl -k https://localhost:1234

%package license
Summary: license components for the acme package.
Group: Default

%description license
license components for the acme package.


%package python
Summary: python components for the acme package.
Group: Default
Requires: acme-python3 = %{version}-%{release}

%description python
python components for the acme package.


%package python3
Summary: python3 components for the acme package.
Group: Default
Requires: python3-core
Provides: pypi(acme)
Requires: pypi(chardet)
Requires: pypi(cryptography)
Requires: pypi(josepy)
Requires: pypi(pyopenssl)
Requires: pypi(pyrfc3339)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(setuptools)

%description python3
python3 components for the acme package.


%prep
%setup -q -n acme-1.18.0
cd %{_builddir}/acme-1.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628087986
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/acme
cp %{_builddir}/acme-1.18.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/acme/d095fa0d394cc9417a65aecd0d28e7d10e762f98
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/acme/d095fa0d394cc9417a65aecd0d28e7d10e762f98

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
