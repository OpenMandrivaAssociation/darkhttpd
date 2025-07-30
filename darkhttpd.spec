%global debug_package %{nil}

Name:		darkhttpd
Summary:	When you need a web server in a hurry
Version:	1.17
Release:	1
License:	ISC
Group:		System/Servers
Url:		https://github.com/emikulic/darkhttpd
Source0:	https://github.com/emikulic/darkhttpd/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
%{summary}.

%prep
%autosetup -p1

%build
%make_build

%install
install -Dm 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
