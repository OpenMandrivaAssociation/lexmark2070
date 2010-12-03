Summary:	Lexmark 2070 Printer B/W driver
Name:		lexmark2070
Version:	0.6
Release:	%mkrel 11
License:	GPL
Group:		System/Printing
URL:		http://www.kornblum.i-p.com/2070/Lexmark2070.old.html
Source0:	http://www.kornblum.i-p.com/2070/Lexmark2070.latest.tar.bz2
Patch0:		Lexmark2070-LDFLAGS.diff
Requires:	c2070
BuildRequires:	netpbm-devel
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This filter allows to print in B/W a Lexmark 2070 (windows GDI) printer.

%prep

%setup -q -c
%patch0 -p0

%build
make -f makefile CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 Lexmark2070 %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README LICENSE
%attr(0755,root,root) %{_bindir}/*
