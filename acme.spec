#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4D17C995CD9775F2 (letsencrypt-client@eff.org)
#
Name     : acme
Version  : 0.28.0
Release  : 40
URL      : https://files.pythonhosted.org/packages/c8/c7/37cf8fef2287eaabf3ee4eee1c42a20e4da6e9d7100900d05fd1889eea69/acme-0.28.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/c7/37cf8fef2287eaabf3ee4eee1c42a20e4da6e9d7100900d05fd1889eea69/acme-0.28.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/c8/c7/37cf8fef2287eaabf3ee4eee1c42a20e4da6e9d7100900d05fd1889eea69/acme-0.28.0.tar.gz.asc
Summary  : ACME protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: acme-license = %{version}-%{release}
Requires: acme-python = %{version}-%{release}
Requires: acme-python3 = %{version}-%{release}
Requires: cryptography
Requires: josepy
Requires: pyOpenSSL
Requires: pyrfc3339
Requires: pytz
Requires: requests-toolbelt
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : enum34-python
BuildRequires : ndg_httpsclient-python
BuildRequires : pyOpenSSL
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pyrfc3339
BuildRequires : pyrfc3339-python
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : pytz
BuildRequires : requests-python
BuildRequires : requests-toolbelt
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

%description python3
python3 components for the acme package.


%prep
%setup -q -n acme-0.28.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541635141
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/acme
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/acme/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/acme/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
