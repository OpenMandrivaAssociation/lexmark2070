Summary:	Lexmark 2070 Printer B/W driver
Name:		lexmark2070
Version:	0.6
Release:	13
License:	GPLv2
Group:		System/Printing
Url:		http://www.kornblum.i-p.com/2070/Lexmark2070.old.html
Source0:	http://www.kornblum.i-p.com/2070/Lexmark2070.latest.tar.bz2
Patch0:	Lexmark2070-LDFLAGS.diff
BuildRequires:	netpbm-devel
Requires:	c2070

%description
This filter allows to print in B/W a Lexmark 2070 (windows GDI) printer.

%prep
%setup -q -c
%patch0 -p0

%build
make -f makefile CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -m0755 Lexmark2070 %{buildroot}%{_bindir}/

%files
%doc README LICENSE
%{_bindir}/*

