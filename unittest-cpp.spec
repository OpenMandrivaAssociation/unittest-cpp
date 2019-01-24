%define major	2
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		unittest-cpp
Version:	2.0.0
Release:	1
Summary:	Lightweight unit testing framework for C++
License:	MIT
Group:		System/Libraries
URL:		https://github.com/unittest-cpp/unittest-cpp
Source0:	https://github.com/unittest-cpp/unittest-cpp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# documentation from 1.4 tarball: docs/UnitTest++.html
Source1:	%{name}.html
# Patch thanks to abucodonosor aka crazy
Patch0:   do-not-break-autoreconf.patch
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:  git
BuildRequires:  autoconf
BuildRequires:  libtool

%description
%{name} is a lightweight unit testing framework for C++.
Simplicity, portability, speed, and small footprint are all
very important aspects of %{name}.

#----------------------------------------------------

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n	%{libname}
%{name} is a lightweight unit testing framework for C++.
Simplicity, portability, speed, and small footprint are all
very important aspects of %{name}.
This package contains library files for %{name}.

#----------------------------------------------------

%package -n	%{devname}
Summary:	Object files for development using %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

#----------------------------------------------------

%prep
%setup -q
%autopatch -p1
export CC=gcc
export CXX=g++

cp -p %{SOURCE1} .

%build
%configure
%make_build

%install
%make_install

# we don't want these
find %{buildroot} -name '*.la' -delete

%check
make check

%files -n %{libname}
%{_libdir}/libUnitTest++.so.%{major}{,.*}

%files -n %{devname}
%doc %{name}.html AUTHORS
%{_includedir}/UnitTest++/
%{_libdir}/libUnitTest++.so
%{_libdir}/pkgconfig/UnitTest++.pc
