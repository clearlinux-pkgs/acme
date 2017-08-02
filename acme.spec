#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4D17C995CD9775F2 (letsencrypt-client@eff.org)
#
Name     : acme
Version  : 0.17.0
Release  : 11
URL      : https://pypi.debian.net/acme/acme-0.17.0.tar.gz
Source0  : https://pypi.debian.net/acme/acme-0.17.0.tar.gz
Source99 : https://pypi.debian.net/acme/acme-0.17.0.tar.gz.asc
Summary  : ACME protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: acme-bin
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

%description
In order for acme.test_util._guess_loader to work properly, make sure
to use appropriate extension for vector filenames: .pem for PEM and
.der for DER.

%package bin
Summary: bin components for the acme package.
Group: Binaries

%description bin
bin components for the acme package.


%package python
Summary: python components for the acme package.
Group: Default

%description python
python components for the acme package.


%prep
%setup -q -n acme-0.17.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501709093
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1501709093
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

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
