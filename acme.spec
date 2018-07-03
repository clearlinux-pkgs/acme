#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4D17C995CD9775F2 (letsencrypt-client@eff.org)
#
Name     : acme
Version  : 0.23.0
Release  : 33
URL      : https://pypi.debian.net/acme/acme-0.23.0.tar.gz
Source0  : https://pypi.debian.net/acme/acme-0.23.0.tar.gz
Source99 : https://pypi.debian.net/acme/acme-0.23.0.tar.gz.asc
Summary  : ACME protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: acme-python3
Requires: acme-license
Requires: acme-python
Requires: Sphinx
Requires: cryptography
Requires: josepy
Requires: pyOpenSSL
Requires: pyrfc3339
Requires: pytz
Requires: six
Requires: sphinx_rtd_theme
BuildRequires : certifi
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : enum34-python
BuildRequires : josepy-python
BuildRequires : ndg_httpsclient-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pyrfc3339
BuildRequires : pyrfc3339-python
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : requests-python
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
%setup -q -n acme-0.23.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530386147
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/acme
cp LICENSE.txt %{buildroot}/usr/share/doc/acme/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/acme/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
