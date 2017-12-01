#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4D17C995CD9775F2 (letsencrypt-client@eff.org)
#
Name     : acme
Version  : 0.19.0
Release  : 13
URL      : https://pypi.debian.net/acme/acme-0.19.0.tar.gz
Source0  : https://pypi.debian.net/acme/acme-0.19.0.tar.gz
Source99 : https://pypi.debian.net/acme/acme-0.19.0.tar.gz.asc
Summary  : ACME protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: acme-bin
Requires: acme-legacypython
Requires: acme-python3
Requires: acme-python
Requires: Sphinx
Requires: cryptography
Requires: nose
Requires: pyrfc3339
Requires: python-mock
Requires: pytz
Requires: setuptools
Requires: six
Requires: tox
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : chardet-python
BuildRequires : cryptography
BuildRequires : enum34-python
BuildRequires : ndg_httpsclient-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pyrfc3339
BuildRequires : pyrfc3339-python
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six-python
BuildRequires : urllib3-python

%description
In order for acme.test_util._guess_loader to work properly, make sure
to use appropriate extension for vector filenames: .pem for PEM and
.der for DER.

%package bin
Summary: bin components for the acme package.
Group: Binaries

%description bin
bin components for the acme package.


%package legacypython
Summary: legacypython components for the acme package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the acme package.


%package python
Summary: python components for the acme package.
Group: Default
Requires: acme-legacypython
Requires: acme-python3

%description python
python components for the acme package.


%package python3
Summary: python3 components for the acme package.
Group: Default
Requires: python3-core

%description python3
python3 components for the acme package.


%prep
%setup -q -n acme-0.19.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512086617
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1512086617
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jws

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
