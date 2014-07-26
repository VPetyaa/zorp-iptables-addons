Name:			zorp-iptables
Version:		1.0
Release:		1
URL:			https://www.balabit.com/network-security/zorp-gpl
#Source0:		https://www.balabit.com/downloads/files/zorp/3.9.5/source/libzorpll_3.9.4.1.tar.gz
Source0:		iptables-addons_%{version}-1.tar.gz
Summary:		BalaBit Zorp blablabla
License:		GPL-2.0
Group:			System/Daemons
BuildRequires:		iptables
BuildRequires:      automake
BuildRequires:      autoconf
BuildRequires:      gcc-c++
BuildRequires:      python
BuildRequires:      libtool

%if 0%{?fedora} || 0%{?centos}
BuildRequires:		iptables-devel
%else
BuildRequires:		libxtables-devel
%endif


BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BalaBit Zorp is a proxy based firewall

%package devel
Summary:		Cuccok a zorphoz
Group:			System/Daemons
Requires:		zlib-devel
Requires:		glibc-devel
Requires:		libcap-devel
Requires:		glib2-devel
Requires:		%{name} = %{version}


%description devel
This package provides header files for libzorpll

%prep
%setup -q -n zorp-iptables-addons
# %patch0 -p1

%build
autoreconf -i
%configure --disable-werror --enable-debug

%install
make DESTDIR=${RPM_BUILD_ROOT} install
#%if 0%{?fedora} || 0%{?centos}
#rm %{buildroot}/usr/libexec/failure_notify3.9-4
#%else
#rm %{buildroot}/usr/lib/failure_notify3.9-4
#%endif

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root)
%dir %attr(755,root,root) /usr/lib/xtables/
%attr(755,root,root) /usr/lib/xtables/libxt_*

#%files devel
#%dir %attr(755,root,root) /usr/include/zorp
#%attr(644,root,root) /usr/include/zorp/*
#%attr(644,root,root) %{_libdir}/pkgconfig/zorplibll.pc
#%attr(644,root,root) %{_libdir}/libzorpll.*

%changelog
