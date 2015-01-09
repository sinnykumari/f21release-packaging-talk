Name: hello
Version: 0.1
Release: 1%{?dist}
Summary: Fedora packaging example
Group: Development/Tools
License: GPLv3+
URL: http://files.sinny.io/
Source0: http://files.sinny.io/%{name}-%{version}.tar.gz

#BuildRequires: gcc glibc-headers
#Requires: glibc

%description 
Hello example demonstrating basic RPM packaging in Fedora

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_bindir}/hello

%doc 
%{_docdir}/README

%changelog
* Fri Jan 09 2015 Sinny Kumari <ksinnY@gmail.com> 0.1-1
- Initial version of the package