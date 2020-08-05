Name:           libuv
Epoch:          1
Version:        1.38.1
Release:        1
Summary:        A multi-platform support library with a focus on asynchronous I/O

# the licensing breakdown is described in detail in the LICENSE file
License:        MIT and BSD and ISC
URL:            http://libuv.org/
Source0:        http://dist.libuv.org/dist/v%{version}/%{name}-v%{version}.tar.gz
Source2:        %{name}.pc.in

BuildRequires:  autoconf automake libtool gcc

%description
libuv is a multi-platform support library with a focus on asynchronous I/O. 
It was primarily developed for use by Node.js, but it’s also used by Luvit,
Julia, pyuv, and others.

%package devel
Summary:        Development libraries for libuv
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-static
Provides:       %{name}-static

%description devel
Development libraries for libuv

%package_help


%prep
%autosetup -p1 -n %{name}-v%{version}

%build
./autogen.sh
%configure --disable-silent-rules
%make_build

%install
%make_install
%delete_la

%check
%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}.a
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/uv.h
%{_includedir}/uv/

%files help
%doc README.md AUTHORS CONTRIBUTING.md MAINTAINERS.md SUPPORTED_PLATFORMS.md
%doc ChangeLog

%changelog
* Wed Aug 5 2020 hanxinke <hanxinke@huawei.com> - 1.38.1-1
- update to 1.38.1

* Tue Dec 3 2019 mengxian <mengxian@huawei.com> - 1.23.0-2
- Package init
